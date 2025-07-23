# client/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ClientForm
from .models import Client
from .forms import ClientForm, TreatmentSessionForm
from django.db.models import Q

def client_list(request):
    query = request.GET.get('q', '')
    if query:
        clients = Client.objects.filter(
            Q(name__icontains=query) |
            Q(condition__icontains=query) |
            Q(treatment__icontains=query)
        ).order_by('name')
    else:
        clients = Client.objects.all().order_by('name')
    return render(request, 'client/client_list.html', {'clients': clients, 'query': query})

def client_detail(request, pk):
    client = get_object_or_404(Client, pk=pk)
    sessions = client.sessions.order_by('-date_time')
    return render(request, 'client/client_detail.html', {'client': client, 'sessions': sessions})
def add_treatment_session(request, client_id):
    client = get_object_or_404(Client, pk=client_id)
    if request.method == "POST":
        form = TreatmentSessionForm(request.POST)
        if form.is_valid():
            session = form.save(commit=False)
            session.client = client
            session.save()
            return redirect('client_detail', pk=client.pk)
    else:
        form = TreatmentSessionForm()
    return render(request, 'client/add_session.html', {'form': form, 'client': client})

def add_client(request):
    if request.method == "POST":
        form = ClientForm(request.POST)
        if form.is_valid():
            client = form.save()
            return redirect('client_detail', pk=client.pk)
    else:
        form = ClientForm()
    return render(request, 'client/add_client.html', {'form': form})

def followup_treatment(request, client_id):
    client = get_object_or_404(Client, pk=client_id)
    sessions = client.sessions.order_by('-date_time')
    if request.method == "POST":
        form = TreatmentSessionForm(request.POST)
        if form.is_valid():
            session = form.save(commit=False)
            session.client = client
            session.save()
            return redirect('client_detail', pk=client.pk)
    else:
        form = TreatmentSessionForm()
    return render(request, 'client/followup_treatment.html', {'form': form, 'client': client, 'sessions': sessions})

def edit_client(request, pk):
    client = get_object_or_404(Client, pk=pk)
    if request.method == "POST":
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            client = form.save()
            return redirect('client_detail', pk=client.pk)
    else:
        form = ClientForm(instance=client)
    return render(request, 'client/edit_client.html', {'form': form, 'client': client})


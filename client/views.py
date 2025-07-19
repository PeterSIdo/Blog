# client/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ClientForm
from .models import Client
from .forms import ClientForm, TreatmentSessionForm

def client_list(request):
    clients = Client.objects.all()
    return render(request, 'client/client_list.html', {'clients': clients})
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
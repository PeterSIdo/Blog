# client/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ClientForm
from .models import Client
from .forms import ClientForm, TreatmentSessionForm
from django.db.models import Q
from .models import TreatmentSession

def client_list(request):
    # Get search terms from GET parameters
    client_query = request.GET.get('client_query', '').strip()
    notes_query = request.GET.get('notes_query', '').strip()
    # Start with all clients
    clients = Client.objects.all().order_by('name')
    # Filter by client name if provided
    if client_query:
        clients = clients.filter(
            Q(name__icontains=client_query) |
            Q(condition__icontains=client_query) |
            Q(treatment__icontains=client_query)
        )
    # Filter by treatment notes if provided
    if notes_query:
        # This filter uses the related name 'sessions' on the TreatmentSession model.
        clients = clients.filter(sessions__treatment_notes__icontains=notes_query).distinct()
    context = {
        'clients': clients,
        'client_query': client_query,
        'notes_query': notes_query,
    }
    return render(request, 'client/client_list.html', context)

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
    latest_session = sessions.first()  # Get the most recent session
    if request.method == "POST":
        form = TreatmentSessionForm(request.POST)
        if form.is_valid():
            session = form.save(commit=False)
            session.client = client
            session.save()
            return redirect('client_detail', pk=client.pk)
    else:
        form = TreatmentSessionForm()
    return render(request, 'client/followup_treatment.html', 
                 {'form': form, 'client': client, 'sessions': sessions, 'session': latest_session})

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

def delete_client(request, pk):
    client = get_object_or_404(Client, pk=pk)
    if request.method == "POST":
        client.delete()
        return redirect('client_list')
    return render(request, 'client/delete_client.html', {'client': client})

def edit_treatment_notes(request, session_id):
    session = get_object_or_404(TreatmentSession, pk=session_id)
    if request.method == "POST":
        form = TreatmentSessionForm(request.POST, instance=session)
        if form.is_valid():
            session = form.save()
            return redirect('client_detail', pk=session.client.pk)
    else:
        form = TreatmentSessionForm(instance=session)
    return render(request, 'client/edit_treatment_notes.html', {
        'form': form,
        'session': session
    })
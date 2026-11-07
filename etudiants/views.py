
from django.shortcuts import render, redirect, get_object_or_404
from .forms import EtudiantForm
from .models import Etudiant


def etudiant_create(request):
    if request.method == 'POST':
        form = EtudiantForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('liste_etudiants')
    else:
        form = EtudiantForm()

    return render(
        request,
        'etudiants/etudiant_form.html',
        {
            'form': form,
            'mode': 'creation'
        }
    )


def liste_etudiants(request):
    etudiants = Etudiant.objects.all().order_by('nom', 'prenom')

    return render(
        request,
        'etudiants/etudiant_list.html',
        {'etudiants': etudiants}
    )


def detail_etudiant(request, pk):
    etudiant = get_object_or_404(Etudiant, pk=pk)

    return render(
        request,
        'etudiants/etudiant_detail.html',
        {'etudiant': etudiant}
    )


def etudiant_update(request, pk):
    etudiant = get_object_or_404(Etudiant, pk=pk)

    if request.method == 'POST':
        form = EtudiantForm(request.POST, instance=etudiant)

        if form.is_valid():
            form.save()
            return redirect('detail_etudiant', pk=etudiant.pk)
    else:
        form = EtudiantForm(instance=etudiant)

    return render(
        request,
        'etudiants/etudiant_form.html',
        {
            'form': form,
            'mode': 'modification',
            'etudiant': etudiant
        }
    )


def etudiant_delete(request, pk):
    etudiant = get_object_or_404(Etudiant, pk=pk)

    if request.method == 'POST':
        etudiant.delete()
        return redirect('liste_etudiants')

    return render(
        request,
        'etudiants/etudiant_confirm_delete.html',
        {'etudiant': etudiant}
    )


from django.urls import path
from . import views

urlpatterns = [
    path(
        '',
        views.liste_etudiants,
        name='liste_etudiants'
    ),

    path(
        'etudiant/creer/',
        views.etudiant_create,
        name='etudiant_create'
    ),

    path(
        'etudiant/<int:pk>/',
        views.detail_etudiant,
        name='detail_etudiant'
    ),

    path(
        'etudiant/<int:pk>/modifier/',
        views.etudiant_update,
        name='etudiant_update'
    ),

    path(
        'etudiant/<int:pk>/supprimer/',
        views.etudiant_delete,
        name='etudiant_delete'
    ),
]

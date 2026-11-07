# Gestion des Étudiants (Django)

Application web complète de gestion d'étudiants (CRUD) développée avec le framework **Django** et stylisée avec **Bootstrap 5**. Ce projet a été réalisé dans le cadre du cours *Programmation Web II (Projet 2)*.

---

## Sommaire

- [Présentation](#présentation)
- [Fonctionnalités](#fonctionnalités)
- [Technologies utilisées](#technologies-utilisées)
- [Structure du projet](#structure-du-projet)
- [Prérequis](#prérequis)
- [Installation et démarrage](#installation-et-démarrage)
- [Routes et navigation](#routes-et-navigation)
- [Modèle de données](#modèle-de-données)
- [Contribuer](#contribuer)
- [Licence](#licence)

---

## Présentation

**Gestion des Étudiants** est une application web permettant d'administrer facilement les inscriptions d'étudiants au sein d'un établissement d'enseignement. Elle offre une interface soignée, responsive et ergonomique pour lister, ajouter, consulter, modifier et supprimer des fiches d'étudiants.

---

## Fonctionnalités

- **Affichage de la liste des étudiants** : consultation des étudiants enregistrés avec tri automatique par nom et prénom.
- **Ajout d'un étudiant** : formulaire avec validation des champs obligatoires et facultatifs.
- **Détails d'un étudiant** : vue détaillée présentant l'ensemble des informations académiques et personnelles (nom, prénom, programme, remarque, date d'inscription).
- **Modification d'un étudiant** : mise à jour des données existantes avec formulaire pré-rempli.
- **Suppression sécurisée** : page de confirmation dédiée avant toute suppression définitive.
- **Interface responsive et soignée** : intégration de Bootstrap 5 pour un affichage adapté sur ordinateur, tablette et mobile.

---

## Technologies utilisées

- **Python** (version 3.10 ou supérieure)
- **Django 6.x** : framework web backend haute productivité
- **SQLite** : base de données relationnelle par défaut (développement local)
- **HTML5 / CSS3** avec templates Django
- **Bootstrap 5.3** : framework CSS pour le design et la responsivité

---

## Structure du projet

```text
gestion-etudiants-django/
├── manage.py                     # Utilitaire de gestion des commandes Django
├── requirements.txt              # Dépendances du projet Python
├── .gitignore                    # Fichiers et dossiers ignorés par Git
│
├── gestion_etudiants/            # Configuration globale du projet Django
│   ├── __init__.py
│   ├── asgi.py                   # Point d'entrée pour serveurs ASGI
│   ├── settings.py               # Paramètres de configuration (DB, apps, etc.)
│   ├── urls.py                   # Routage principal du projet
│   └── wsgi.py                   # Point d'entrée pour serveurs WSGI
│
└── etudiants/                    # Application Django dédiée à la gestion des étudiants
    ├── __init__.py
    ├── admin.py                  # Enregistrement pour l'interface Django Admin
    ├── apps.py                   # Configuration de l'application
    ├── forms.py                  # Formulaire ModelForm pour Etudiant
    ├── models.py                 # Modèle de données Etudiant
    ├── tests.py                  # Tests unitaires
    ├── urls.py                   # Routes de l'application
    ├── views.py                  # Logique métier et vues (CRUD)
    │
    ├── migrations/               # Fichiers de migrations de schéma de base de données
    │   ├── 0001_initial.py
    │   └── __init__.py
    │
    └── templates/
        └── etudiants/            # Templates HTML de l'application
            ├── base.html                 # Gabarit de base commun
            ├── etudiant_list.html         # Liste des étudiants
            ├── etudiant_detail.html       # Fiche individuelle
            ├── etudiant_form.html         # Formulaire d'ajout / modification
            └── etudiant_confirm_delete.html # Confirmation de suppression
```

---

## Prérequis

Avant de commencer, assurez-vous de disposer des éléments suivants installés sur votre machine :

- **Python 3.10+** : [python.org](https://www.python.org/)
- **pip** (gestionnaire de paquets Python)
- **Git** : [git-scm.com](https://git-scm.com/)

---

## Installation et démarrage

Suivez les étapes ci-dessous pour déployer et exécuter le projet localement :

### 1. Cloner le dépôt

```bash
git clone https://github.com/ednor/gestion-etudiants-django.git
cd gestion-etudiants-django
```

### 2. Créer et activer un environnement virtuel

Sous Linux / macOS :
```bash
python3 -m venv .venv
source .venv/bin/activate
```

Sous Windows (PowerShell) :
```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

Sous Windows (Invite de commandes cmd) :
```cmd
python -m venv .venv
.venv\Scripts\activate.bat
```

### 3. Installer les dépendances

```bash
pip install -r requirements.txt
```

### 4. Appliquer les migrations de base de données

Créez le schéma de la base de données SQLite :
```bash
python manage.py migrate
```

### 5. (Optionnel) Créer un administrateur

Pour accéder à l'interface d'administration Django :
```bash
python manage.py createsuperuser
```

### 6. Lancer le serveur de développement

```bash
python manage.py runserver
```

L'application est désormais accessible dans votre navigateur à l'adresse suivante :
👉 [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

L'interface d'administration Django est accessible sur :
👉 [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

---

## Routes et navigation

| URL | Nom de la route | Méthode(s) | Description |
|---|---|---|---|
| `/` | `liste_etudiants` | `GET` | Affiche la liste ordonnée de tous les étudiants |
| `/etudiant/creer/` | `etudiant_create` | `GET`, `POST` | Affiche et traite le formulaire de création d'un étudiant |
| `/etudiant/<id>/` | `detail_etudiant` | `GET` | Affiche la fiche détaillée d'un étudiant spécifique |
| `/etudiant/<id>/modifier/` | `etudiant_update` | `GET`, `POST` | Affiche et traite la modification d'un étudiant |
| `/etudiant/<id>/supprimer/` | `etudiant_delete` | `GET`, `POST` | Demande confirmation et effectue la suppression |
| `/admin/` | `admin:index` | `GET`, `POST` | Interface d'administration native Django |

---

## Modèle de données

Le modèle principal est `Etudiant` (`etudiants/models.py`) :

| Champ | Type Django | Description | Contraintes |
|---|---|---|---|
| `id` | `BigAutoField` | Identifiant unique (clé primaire) | Auto-incrémenté |
| `nom` | `CharField` | Nom de famille de l'étudiant | Maximum 100 caractères, obligatoire |
| `prenom` | `CharField` | Prénom de l'étudiant | Maximum 100 caractères, obligatoire |
| `programme` | `CharField` | Programme ou filière d'études | Maximum 150 caractères, obligatoire |
| `remarque` | `TextField` | Commentaires ou observations | Facultatif (`blank=True`, `null=True`) |
| `date_inscription` | `DateField` | Date de création de la fiche | Renseignée automatiquement (`auto_now_add=True`) |

---

## Contribuer

Les contributions, suggestions et signalements d'anomalies sont les bienvenus !

1. Forkez le projet.
2. Créez une branche dédiée à votre fonctionnalité (`git checkout -b feature/nouvelle-fonctionnalite`).
3. Validez vos modifications (`git commit -m "feat: ajout d'une nouvelle fonctionnalite"`).
4. Poussez votre branche (`git push origin feature/nouvelle-fonctionnalite`).
5. Ouvrez une Pull Request.

---

## Licence

Ce projet est réalisé à des fins pédagogiques dans le cadre du cours *Programmation Web II*. Tous droits réservés à son auteur.

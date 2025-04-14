# API Restful Project 🚀

![Python](https://img.shields.io/badge/python-3.12-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Status](https://img.shields.io/badge/status-in--progress-orange)
![Requirements](https://img.shields.io/badge/requirements-up%20to%20date-brightgreen)

ApiRestful est une API REST complète pour la gestion collaborative de projets logiciels. Elle permet aux utilisateurs de créer des projets, de collaborer via des issues et des commentaires, le tout en respectant une hiérarchie de permissions rigoureuse (auteurs, contributeurs, administrateurs).

## Fonctionnalités clés 🚀

### 👥 Gestion des utilisateurs
- Inscription sécurisée avec hash du mot de passe.
- Authentification via token.
- Possibilité de modifier ou supprimer ses propres informations (ou par admin).
- Protection des données en fonction de l’âge (RGPD-friendly).

### 📁 Projets
- Création de projets avec typologie (`Front-end`, `Back-end`, `iOS`, etc.).
- Chaque projet possède un auteur principal.
- Possibilité d’ajouter des contributeurs avec des rôles spécifiques.
- Détail du projet accessible uniquement aux contributeurs ou à l’admin.

### 🐞 Issues
- Création d’issues par les contributeurs uniquement.
- Assignation possible à un autre contributeur du projet.
- Priorisation (`LOW`, `MEDIUM`, `HIGH`) et typage (`BUG`, `FEATURE`, `TASK`).
- Modification/suppression uniquement par l’auteur ou l’admin.

### 💬 Commentaires
- Ajout de commentaires aux issues.
- Seuls les contributeurs peuvent interagir.
- Chaque commentaire est modifiable ou supprimable uniquement par son auteur ou l’admin.

### 🔒 Permissions robustes
- Accès restreint par rôle :
  - `Admin` : Accès total
  - `Auteur` : Lecture/écriture sur ses ressources
  - `Contributeur` : Accès aux projets associés
  - `Non-contributeur` : Aucun accès aux projets ou issues concernés

---

## Technologies utilisées ⚙️

- **Python 3.12**
- **Django & Django REST Framework**
- **SQLite (dev)** ou PostgreSQL (prod-ready)
- **SimpleJWT** pour l’authentification
- **drf-nested-routers** pour la gestion des routes imbriquées

---

## Installation & Lancement 🧪

### 1. Cloner le dépôt

```bash
git clone https://github.com/tonpseudo/apirestful.git
cd apirestful
```

### 2. Créer l’environnement virtuel

```bash
python -m venv env
source env/bin/activate  # macOS/Linux
env\Scripts\activate      # Windows
```

### 3. Installer les dépendances

```bash
pip install -r requirements.txt
```

### 4. Appliquer les migrations et lancer le serveur

```bash
python manage.py migrate
python manage.py runserver
```

📍 Accès local : http://127.0.0.1:8000/api/

---

## Endpoints principaux 🌐

| Ressource     | Méthodes disponibles | Permissions |
|---------------|----------------------|-------------|
| `/api/users/` | GET, POST, PUT, DELETE | Admin ou utilisateur lui-même |
| `/api/projects/` | GET, POST, PUT, DELETE | Contributeur ou admin |
| `/api/projects/{id}/issues/` | GET, POST, PUT, DELETE | Contributeur ou auteur |
| `/api/projects/{id}/issues/{id}/comments/` | GET, POST, PUT, DELETE | Auteur ou admin |
| `/api/projects/{id}/contributors/` | GET, POST, DELETE | Auteur du projet ou admin |

---

## Pagination 🔄

Pagination automatique avec `?page=1`, `?page=2`, etc.

```python
# settings.py
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
}
```

---

## Aperçu de la structure du projet 📂

```bash
apirestful/
│
├── api/                        # Application principale
│   ├── models.py               # Modèles : User, Project, Issue, Comment
│   ├── views.py                # ViewSets DRF
│   ├── serializers.py          # Sérialisation des données
│   ├── permissions.py          # Gestion des permissions personnalisées
│   ├── urls.py                 # URLs imbriquées
│
├── apirestful/                # Configuration Django
│   ├── settings.py
│   ├── urls.py
│
├── requirements.txt
├── manage.py
└── README.md
```

---

## Tests unitaires 🧪

En cours d’ajout. Tu peux exécuter :

```bash
python manage.py test
```

---

## Authentification 🔐

L’authentification par token est requise sur toutes les routes sécurisées. Exemples :

```bash
# Authentifier et obtenir le token
curl -X POST http://127.0.0.1:8000/api/token/ -d "username=user&password=mdp"

# Utiliser le token pour accéder à une route protégée
curl -H "Authorization: Bearer your_token" http://127.0.0.1:8000/api/projects/
```

---

## Licence 📄

Projet sous licence MIT – libre d’utilisation et de modification.
# r33d-concept-ecoomerce-rap


Ceci est une application Django de boutique en ligne pour la vente de T-shirts, avec des fonctionnalités comme la gestion des produits, l'ajout au panier, la gestion du profil utilisateur, et bien plus.

## Fonctionnalités

- Gestion des utilisateurs (connexion, inscription, profil)
- Détails des produits (description, images supplémentaires, taille, couleur)
- Ajout au panier et gestion du panier
- Filtrage des produits par collection

## Installation

1. Clonez ce dépôt :
    ```bash
    git clone https://github.com/username/tshirt-shop.git
    ```

2. Créez un environnement virtuel :
    ```bash
    python -m venv env
    ```

3. Activez l'environnement virtuel :
    - Sur Windows : `env\Scripts\activate`
    - Sur Mac/Linux : `source env/bin/activate`

4. Installez les dépendances :
    ```bash
    pip install -r requirements.txt
    ```

5. Appliquez les migrations :
    ```bash
    python manage.py migrate
    ```

6. Lancez le serveur :
    ```bash
    python manage.py runserver
    ```

7. Accédez à l'application via `http://127.0.0.1:8000/`

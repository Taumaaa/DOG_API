# Application d'affichage d'images aléatoires de chiens

Cette application interroge l'API publique [Dog CEO](https://dog.ceo/dog-api/) pour récupérer une image aléatoire de chien et l'affiche dans le terminal.

## Fonctionnalités

- Récupère une image aléatoire de chien.
- Affiche l'URL de l'image directement dans le terminal.

## Installation

1. Clonez ce dépôt :

   ```bash
   git clone https://github.com/Taumaaa/ue19-lab-05.git
   cd ue19-lab-05
2. Installer les dépendances :

   ```bash
   pip install -r requirements.txt
   
## Utilisation

### Via un IDE
1. Ouvrir le fichier `main.py` dans votre IDE.
2. Exécuter le script.
#### Via la ligne de commande :
1. Ouvrir un terminal.
    ```bash
        python main.py

### Via Docker :
1. Installer et Ouvrir l'application Docker via le site officiel [Docker](https://www.docker.com/products/docker-desktop)
2. Ouvrir un terminal 
3. Exécuter les commande suivante :
    ```bash
        docker build -t dog-api .
        docker run dog-api

## Auteur
- [GitHub](https://github.com/Taumaaa) Taumaaa

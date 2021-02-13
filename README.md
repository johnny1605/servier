Pour récupérer le repository:
git clone https://github.com/johnny1605/servier.git


Création de l'image docker "servier":
docker build . -t servier


Lancer le container:
docker run -p 8891:8891 -it --entrypoint /bin/bash servier


Leancer la Web Application:
python3 launcher.py



Dans un navigateur (Google chrome de préférence) coller l'adresse suivante : http://localhost:8891/ 



Dans la WebApp: 

Cliquer sur « smiles »

Sélectioner le fichier « smile.csv », c’est un exemple présent dans le dossier cloné
Il prend comme input un ID et un smiles

Cliquer sur « submit »



Infos:
- Le back_end est exposé sur le port 8892 (code python)
- Le front_end est exposé sur le port 8891
- Pour les prédictions, un modèle pré-entrainé et stocké dans "back_end/Model", sera appelé.
- Pour récupérer le repository:
	- git clone https://github.com/johnny1605/servier.git



- Création de l'image docker "servier":
	- docker build . -t servier



- Lancer le container:
	- docker run -p 8891:8891 -it --entrypoint /bin/bash servier



- Lancer la Web Application:
	- python3 launcher.py



Dans un navigateur (Google chrome de préférence) coller sur l'adresse suivante : http://localhost:8891/ 



Dans la WebApp: 
- Cliquer sur « smiles »
- Sélectioner le fichier « smile.csv », c’est un exemple présent dans le dossier cloné (le nom du fichier n'apparaitra pas dans le front)
- Il prend comme input un ID et un smiles
- Cliquer sur « submit »
- Pour tester un nouveau « smiles », il faut modifer le nom dans le fichier « smiles.csv »



Infos:
- Le back_end est exposé sur le port 8892 (code python)
- Le front_end est exposé sur le port 8891
- Pour les prédictions, un modèle pré-entrainé et stocké dans "back_end/Model", sera appelé
- Toutes les démarches, de PreProcessing et de validation du modèle, sont présentes dans le notebook suivant: /Notebook/Test_servier.ipynb
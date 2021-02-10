Avec Docker:

docker  build . -t servier

docker run -it --entrypoint /bin/bash servier

cd /app_demo/app_demo

python3 launcher.py>output.log.  (A lancer en mode sudo ou vérifier ligne 16 le python_path dans le « launcher.py »)

./run_app_cmd.sh


Dans le navigateur qui s’ouvre automatiquement, cliquer sur « smiles »

Sélectioner le fichier « smile.csv », c’est un exemple présent dans le dossier, en input:
ID	smiles

Cliquer sur « submit »


—————————————————————————————————————————————————————————————————

Sans Docker:

Se placer dans le répertoire app_demo

Lancer la commande dans un terminal:

python3 launcher.py>output.log (A lancer en mode sudo ou vérifier ligne 16 le python_path dans le « launcher.py »)

Dans le navigateur qui s’ouvre automatiquement, cliquer sur « smiles »

Sélectioner le fichier « smile.csv », c’est un exemple présent dans le dossier, en input:
ID	smiles

Cliquer sur « submit »


—————————————————————————————————————————————————————————————————

Dans le dossier Notebook:

Vous pouvez exécuter toutes les cellules

Les dernières étant un exemple de fichier qui reçoit un fichier csv « smiles.csv » présent dans le dossier Notebook


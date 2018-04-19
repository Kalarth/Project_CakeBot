Premièrement dans le dossier "Creation_marqueur"

  Il faut lancer le fichier "Create.py", il créer la liste des douze marqueurs dont on aura besoin.

Ensuite, dans le dossier "Analyse_marqueur"
  D'abord lancer le fichier "Calibration.py"
    -> Il créer un fichier "Data.yaml" dans le dossier "calib_images" qui contient la matrice et le coefficient de distance de la camera

  Pour finir il faut lancer le fichier "Aruco.py" qui analyse le marqueur Aruco.
    -> il boucle a l'infini ( normal, il analyse en continue) il faut donc appuyer sur q pour le stopper, et afficher les "corners", ces fameuse valeurs dont je vous parlais ! ;)

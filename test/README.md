#### BONJOUR ET BIENVENUE DANS LA NOTICE D'UTILISATION ####

Je vais faire un bref tuto afin de pouvoir que vous puissiez utiliser les différents fichiers de ce dossier APPLI_CHU.

D'abord je vais expliquer comment utiliser le fichier "app_console_python.py" dans le dossier --> "python_app" avec le terminal/console  de python.

Puis je vais expliquer comment utiliser l'application Streamlit avec le fichier "app_strlt.py" dans le dossier --> "streamlit_app".

#### INSTALLATION DES MODULES #####

installer les modules dans un l'environnement 

pip install streamlit
pip install mysql-connector-python
pip install pandas
pip install numpy



##### INSTRUCTION POUR APP_CONSOLE_PYTHON.PY ####

Il n'y a pas de script pour créer une instance/objet (j'ai déjà assez charbonné comme ça D: ),
ca sera donc a vous de la faire.

Pour ce faire j'ai laissé quelques exemples, il vous suffit de créer une variable 
(patient_nom_prenom =  pour le patient, rh_nom_prenom = pour un rh) 
puis d'ajouter dans ces variables l'instance/objet associé 
(patient_nom_prenom = Patient("nom", "prenom", age, "groupe sanguin" ), ca c'est pour un patient)
(rh_nom_prenom = RH("nom", "prenom", salaire), ca c'est pour un RH)

Ensuite on appel une des fonctions associées à l'instance/objet
(patient_nom_prenom.la_fonction(), il y en a 3 pour la Class Patient : save_patient_to_db(), entrer_et_ou_sortie_hopital(), count_patients_in_db() "Je vous laisse deviner a quoi elle servent ;)")

(rh_nom_prenom.la_fonction(), il y en a 2 pour la Class RH : working_at_hospital(), 
start_or_leave_CDD_CDI()   ).

Puis vous exécuté/run le code python ensuite il suffit de suivre les instructions dans la console :D.



#### INSTRUCTION POUR APP_STRLT.PY #####

Ici c'est beaucoup plus simple vous exécutez directement le code du fichier "app_strlt.py", 
le terminale/console s'affiche. 

Dedans (le terminal (ou cas où)) vous écrivez "streamlit run lechemin".
Pour avoir le chemin rien de plus simple vous faites un "clic droit" sur le fichier "app_strlt.py", puis vous "copier le chemin" et vous le coller après avoir écrit "streamlit run" ce qui devrait donner 
"streamlit run /home/leguibs/appli_CHU/mon_app/test/streamlit_app/app_strlt.py" 
(si c'est trop compliqué vous pouvez aussi copier/coller la ligne du dessus bande de feignasses).

Une adresse http//: s'affiche dans la console et vous pouvez appuyer sur "CTRL" + "clic gauche" sur l'adresse. L'application s'ouvre dans votre navigateur par défault vous n'avez plus qu'a tatonner.



#### FIN ####

C'est ici que je vous laisse bon courage.(surtout à toi JB)

PS: il y a un fichier CHU_Caen.sql pour créer la BDD de chez vous.

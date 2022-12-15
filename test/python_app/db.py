#### IMPORTATION DU MODULE ET PARAMETRAGE DE LA CONNECTION A LA BDD  ####

import mysql.connector as mysql

user = 'root'
password = 'example'
host = 'localhost'
port = '3307'
database = 'CHU_Caen'

bdd = mysql.connect(user=user, password=password, host=host, port=port, database=database)
cursor = bdd.cursor()
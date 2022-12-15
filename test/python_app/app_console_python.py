#### IMPORTATION DES MODULES ####

import datetime
import pandas as pd
import numpy as np
from db import *



#### PROGRAMATION ORIENTE OBJET D'UNE INSTANCE/OBJET PATIENT ####

class Patient:
    """ Initialisation des données du patient"""

    def __init__(self, nom, prenom, age, groupe_sanguin):    #créer un patient
        self.nom = str(nom).upper()
        self.prenom = str(prenom)
        self.age = int(age)
        self.groupe_sanguin = groupe_sanguin

    

    """Enregistrer le patient en base de données"""
    def save_patient_to_db(self):                          #Fontion qui enregistre un patient

        id = "Patient" + "-" + self.nom + "-" + self.prenom + "-" + self.groupe_sanguin   #création d'un variable id permettant d'etre enregistrer dans une requete
        user_input = input("Hi " + self.prenom + " are you in hospital? (yes/no): ").lower().strip()   #question necessitant une reponse booleenne (yes = True, no = False) .lower.strip(converti en Majuscule et supprime les espaces)
        while user_input != "yes" and user_input != "no":                             # boucle tant que la reponse a la variable in_hospital n'est pas strictement égale à "yes" ET/ou "no" reposer la question
            print("Please write a correct answer")
            user_input = input("Are you in hospital? (yes/no): ").lower().strip()

        in_hospital = user_input == "yes"               # est ce que j'ai vraiment besoin d'expliquer ? x)
        if in_hospital == True:                               
            print("you're in hospital")
        
        else:
            print("you're not in hospital")
         

        try:                                           #essaie d'executer la requete 
            query= f"""INSERT INTO Patient(id_patient, nom, prenom, groupe_sanguin, is_in_hospital, age) VALUES ("{id}","{self.nom}", "{self.prenom}", "{self.groupe_sanguin}", {in_hospital}, {self.age})""" #requete pour enregistrer les patients dans la table Patient de la BDD
            cursor.execute(query)
            bdd.commit()
            print(self.nom +" "+ self.prenom + " recorded in the patient database" )
        
        except:                                        #si la requete n'as pas pu etre executé print(), ca me permets d'eviter les erreurs de terminal quand une fiche a deja etait crée
            print("A patient file has already been created")



    """ Enregistre les dates d'entrée et/ou sortie des patients"""
    def entrer_et_ou_sortie_hopital(self):             #fonction pour enregistrer dans les archives les entrées et sorties des patient
        id = "Patient" + "-" + self.nom+ "-" + self.prenom + "-" + self.groupe_sanguin 
        user_input = input("Hi " + self.prenom + " are you in hospital? (yes/no): ").lower().strip()
        while user_input != "yes" and user_input != "no":
            print("Please write a correct answer")
            user_input = input("Are you in hospital? (yes/no): ").lower().strip()

        in_hospital = user_input == "yes"

        if in_hospital == True:
            print("Enter a date of admission to the hospital")
            year = int(input('Enter a year : '))
            month = int(input('Enter a month : '))
            day = int(input('Enter a day : '))
            date1 = datetime.date(year, month, day)     #variable pour enregistrer la date d'entré à l'hopital pour par la suite faire une requete
            
            query= f"""INSERT INTO Archive(id_resident, date_entree) VALUES("{id}","{date1}")  
            on duplicate key update date_entree = "{date1}";
            """
            cursor.execute(query)
            bdd.commit()
            print("We have saved your admission date")

        else:
            print("Enter a hospital admission date")
            year = int(input('Enter a year : '))
            month = int(input('Enter a month : '))
            day = int(input('Enter a day : '))
            date_entre = datetime.date(year, month, day) #variable pour enregistrer la date d'entré à l'hopital pour par la suite faire une requete
            
            print("Enter a hospital discharge date")
            year = int(input('Enter a year : '))
            month = int(input('Enter a month : '))
            day = int(input('Enter a day : '))
            date_sortie = datetime.date(year, month, day) #variable pour enregistrer la date de sorti à l'hopital pour par la suite faire une requete

            query= f"""INSERT INTO Archive(id_resident,date_entree, date_sortie) VALUES("{id}","{date_entre}", "{date_sortie}")
            on duplicate key update date_entree = "{date_entre}";
            """
            cursor.execute(query)
            bdd.commit()
            print("We saved your release date")



    """ COMPTE LE NOMBRE DE PATIENT EN BDD DANS LA TABLE PATIENT """
    def count_patients_in_db(self): #fonction qui compte le nombre de patient en BDD
        

        query= """SELECT COUNT(id_patient) FROM Patient""" # selectionne et compte toutes les lignes id_patient dans la table Patient
        cursor.execute(query)
        count = cursor.fetchone()[0]   #variable qui enregistre les valeurs de la requete
        print(count)
        



#### PROGRAMATION ORIENTE OBJET D'UNE INSTANCE/OBJET RH ####
            
class RH:
    def __init__(self, nom, prenom, salaire): #crée un Rh
        self.nom = str(nom).upper()
        self.prenom = str(prenom)
        self.salaire = salaire



    """ ENREGISTRE EN BDD DANS LA TABLE RH LES DONNEES DU RH"""
    def working_at_hospital(self):   #fonction pour savoir si la personne travail dans l'hopital

        id = "RH" + "-" + self.nom + "-" + self.prenom
        user_input = input("Hi " + self.prenom + " are you working at hospital? (yes/no): ").lower().strip()
        while user_input != "yes" and user_input != "no":
            print("Please write a correct answer")
            user_input = input("Are you working at hospital? (yes/no): ").lower().strip()

        working_at_hospital = user_input == "yes"
        if working_at_hospital == True:
            print("Ok you working at hospital")
        
        else:
            print("Ok you're not working at hospital")


        try:
            query = f"""INSERT INTO Rh(id_Rh, nom, prenom, salaire, working_at_hospital) VALUES ("{id}","{self.nom}", "{self.prenom}", {self.salaire}, {working_at_hospital})"""
            cursor.execute(query)
            bdd.commit()
            print(self.nom +" "+ self.prenom + " saved in database" )
        
        except:
            print(" You're already saved in database ")



    """ ENREGISTRE LES DATE DE CONTRAT ET LE TYPE DE CONTRAT EN BDD DANS LA TABLE ARCHIVE"""
    def start_or_leave_CDD_CDI(self):           
        id = "RH" + "-" + self.nom + "-" + self.prenom
        user_input = input("Hi " + self.prenom + " are you working at hospital? (yes/no): ").lower().strip()
        while user_input != "yes" and user_input != "no":
            print("Please write a correct answer")
            user_input = input("Hi " + self.prenom + " are you working at hospital? (yes/no): ").lower().strip()
        
        working_at_hospital = user_input == "yes"
        if working_at_hospital == True:

            user_input = input(self.prenom + " are you in CDD or CDI ? (CDD/CDI): " ).lower().strip()
            while user_input != "cdi" and user_input != "cdd":
                print("Please write a correct answer")
                user_input = input(self.prenom + " are you in CDD or CDI ? (CDD/CDI): " ).lower().strip()
            
            CDD = user_input == "cdd"

            if CDD == False:
                CDD = "CDI"
                print(self.prenom +" enter the date you started the CDI")
                year = int(input('Enter a year : '))
                month = int(input('Enter a month : '))
                day = int(input('Enter a day : '))
                date1 = datetime.date(year, month, day)
            
                query= f"""INSERT INTO Archive(id_resident, date_entree, CDD_CDI) VALUES("{id}","{date1}", "{CDD}")
                on duplicate key update date_entree = "{date1}";
                """
                cursor.execute(query)
                bdd.commit()
                print("The start date of your contract has been saved " + self.prenom)
            
            else:
                CDD = "CDD"
                print(self.prenom +" enter the date you started the CDD")
                year = int(input('Enter a year : '))
                month = int(input('Enter a month : '))
                day = int(input('Enter a day : '))
                date_entre = datetime.date(year, month, day)
            
                query= f"""INSERT INTO Archive(id_resident, date_entree, CDD_CDI) VALUES("{id}","{date_entre}","{CDD}")
                on duplicate key update date_entree = "{date_entre}";
                """
                cursor.execute(query)
                bdd.commit()
                print("The start date of your contract has been saved " + self.prenom)

                print(self.prenom + " enter the date you end the CDD")
                year = int(input('Enter a year : '))
                month = int(input('Enter a month : '))
                day = int(input('Enter a day : '))
                date_sortie = datetime.date(year, month, day)

                query= f"""INSERT INTO Archive(id_resident, date_sortie) VALUES("{id}","{date_sortie}")
                on duplicate key update date_sortie = "{date_sortie}";
                """
                cursor.execute(query)
                bdd.commit()
                print("The end date of your contract has been saved " + self.prenom)


        
        else:
            CDI = "CDI"
            print(self.prenom +" enter the date you started the CDI")
            year = int(input('Enter a year : '))
            month = int(input('Enter a month : '))
            day = int(input('Enter a day : '))
            date_entre = datetime.date(year, month, day)
            
            query= f"""INSERT INTO Archive(id_resident, date_entree, CDD_CDI) VALUES("{id}","{date_entre}","{CDI}")
            on duplicate key update date_entree = "{date_entre}";
            """
            cursor.execute(query)
            bdd.commit()
            print("The start date of your contract has been saved " + self.prenom)

            print(self.prenom + " enter the date you leave the CDI")
            year = int(input('Enter a year : '))
            month = int(input('Enter a month : '))
            day = int(input('Enter a day : '))
            date_sortie = datetime.date(year, month, day)

            query= f"""INSERT INTO Archive(id_resident, date_sortie) VALUES("{id}","{date_sortie}")
            on duplicate key update date_sortie = "{date_sortie}";
            """
            cursor.execute(query)
            bdd.commit()
            print("The end date of your contract has been saved " + self.prenom)



                        #### INITIALISATION DE PATIENT ####

patient_zouiten_guinel = Patient("ZOUITEN", "Guinel", 25, "O+")
# patient_zouiten_guinel.save_patient_to_db()
# patient_zouiten_guinel.entrer_et_ou_sortie_hopital()

patient_denier_charlie = Patient("DENIER", "Charlie", 25, "A+")
# patient_denier_charlie.save_patient_to_db()
# patient_denier_charlie.entrer_et_ou_sortie_hopital()

patient_freeman_morgan = Patient("FREEMAN", "Morgan", 77, "Z-")
# patient_freeman_morgan.save_patient_to_db()
# patient_freeman_morgan.entrer_et_ou_sortie_hopital()

patient_edouard_jean = Patient("EDOUARD", "Jean", 77, "A+")   
# patient_edouard_jean.save_patient_to_db()
# patient_edouard_jean.entrer_et_ou_sortie_hopital()               
                    
patient_desbois_julie = Patient("desbois", "Julie", 24, "A+")
# patient_desbois_julie.save_patient_to_db()
patient_desbois_julie.entrer_et_ou_sortie_hopital()




                        #### INITIALISATION DE RH ####

rh_leroy_francois = RH("Leroy", "François", 3000)
# rh_leroy_francois.working_at_hospital()
# rh_leroy_francois.start_or_leave_CDD_CDI()


rh_theroulde_jb = RH("Theroulde", "Jean-Baptiste", 3500)
# rh_theroulde_jb.working_at_hospital()
# rh_theroulde_jb.start_or_leave_CDD_CDI()

rh_vauthier_antoine= RH("Vauthier", "Antoine", 4500)
# rh_vauthier_antoine.working_at_hospital()
# rh_vauthier_antoine.start_or_leave_CDD_CDI()


rh_dujardin_jean= RH("DUJARDIN", "Jean", 8000)
# rh_dujardin_jean.working_at_hospital()
# rh_dujardin_jean.start_or_leave_CDD_CDI()
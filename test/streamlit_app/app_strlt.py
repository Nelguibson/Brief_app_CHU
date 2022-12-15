#### IMPORTATION DES MODULES NECESSAIRE POUR FAIRE TOURNER L'APPLICATION ####

import streamlit as st
from db import *
import numpy as np
import pandas as pd



#### PROGRAMATION ORIENTE OBJET D'UNE CLASS ARCHIVE ####

class Archive:

    @staticmethod    #la methode static nous permets de ne pas avoir besoin d'inisialiser une instance/objet archive pour faire appel à nos fonctions
    def enregistrer_rh():  # fonction avec une requete pour enregistrer un rh
        query = f"""INSERT INTO Rh(id_Rh, nom, prenom, salaire, working_at_hospital) VALUES ("{id}","{nom_rh}", "{prenom_rh}", {salaire}, {working_at_hospital})"""
        cursor.execute(query)
        bdd.commit()
        st.write(nom_rh.upper() +" "+ prenom_rh + " enregistré en base Rh" )

    @staticmethod
    def enregistrer_patient(): # fonction avec une requete pour enregistrer un patient
        query= f"""INSERT INTO Patient(id_patient, nom, prenom, groupe_sanguin, is_in_hospital, age) VALUES ("{id}","{nom}", "{prenom}", "{groupe_sanguin}", {in_hospital}, {age})""" #requete pour enregistrer les patients dans la table Patient de la BDD
        cursor.execute(query)
        bdd.commit()
        st.write("You have been successfully registered")

    @staticmethod #fonction avec une requete pour enregistrer une date d'entré d'un patient
    def enregistrer_date_entree_patient_archive():
        query= f"""INSERT INTO Archive(id_resident, date_entree) VALUES("{id}","{date_1}") on duplicate key update date_entree = "{date_1}";"""
        cursor.execute(query)
        bdd.commit()
        st.write("We have saved your admission date")

    @staticmethod
    def enregistrer_date_sorti_entree_patient(): # fonction avec une requete pour enregistrer une date d'entré et de sortie d'un patient
        query= f"""INSERT INTO Archive(id_resident, date_entree, date_sortie) VALUES("{id}","{date_1}", "{date_2}") 
        on duplicate key update date_sortie = "{date_2}";"""
        cursor.execute(query)
        bdd.commit()
        st.write("We saved your admission and release date")

    @staticmethod
    def enregistrer_date_debut_fin_cdd(): #fonction avec une requete pour enregistrer les date de debut et de fin d'un CDD
        query= f"""INSERT INTO Archive(id_resident, date_entree,date_sortie, CDD_CDI) VALUES("{id}","{date_debut_CDD}","{date_fin_CDD}", "{CDD_or_CDI}")
        on duplicate key update date_entree = "{date_debut_CDD}";"""
        cursor.execute(query)
        bdd.commit()
        st.write("The start and end date of your CDD contract has been saved " + prenom_rh)
    
    @staticmethod
    def enregistrer_date_debut_cdi(): #fonction avec requete pour enregistrer une date de debut de CDI
        query= f"""INSERT INTO Archive(id_resident, date_entree, CDD_CDI) VALUES("{id}","{date_debut_CDI}", "{CDD_or_CDI}")
        on duplicate key update date_entree = "{date_debut_CDI}";"""
        cursor.execute(query)
        bdd.commit()
        st.write("The start date of your CDI contract has been saved " + prenom_rh)

    @staticmethod
    def enregistrer_date_debut_fin_cdi(): #fonction avec requete pour enregistrer une date de debu et de fin d'un CDI
        query= f"""INSERT INTO Archive(id_resident, date_entree, date_sortie, CDD_CDI) VALUES("{id}","{date_debut_CDI}","{date_fin_CDI}", "{CDI}")
        on duplicate key update date_entree = "{date_debut_CDI}";"""
        cursor.execute(query)
        bdd.commit()
        st.write("The date of your CDI contract has been saved " + prenom_rh)

    @staticmethod
    def afficher_les_archives_streamlit(): #fonction avec une requete pour afficher les données de la table Archive dans la BDD CHU_Caen
        query= """SELECT * FROM Archive"""
        cursor.execute(query)
        result =  cursor.fetchall()
        df= pd.DataFrame(result, columns=["id_resident","date_entree","date_sortie", "CDD_CDI"])
        return df



#### CREATION DE L'APPLICATION ####

st.title("ARCHIVES CHU OF CAEN:hospital:") #titre de l'application

col1, col2, col3, col4, col5 = st.columns(5) #initialisation des colonnes de l'applications


with col1:                          #initialisation de la premiere colonne
    st.title("Register patient")
    nom = st.text_input("Enter your name")
    prenom = st.text_input("Enter your first name")
    age = st.slider("Enter your age", min_value = 1, max_value = 110)
    st.write(age)
    groupe_sanguin = st.radio("Enter your blood group",
                                ("A+","A-","B+","B-","AB+","AB-","O+","O-","other"))
    id = "Patient" + "-" + nom.upper() +"-" + prenom + "-" + groupe_sanguin

    in_hospital = st.radio("Are you in the hospital",
                                (True, False))

    if in_hospital == True:
        date_1 = st.date_input("Enter your admission date: ")
        if st.button("save date of admission"):         
            Archive.enregistrer_date_entree_patient_archive()   #appel de la fonction static dans le bouton 
            
    else:
        date_1 = st.date_input("Enter your admission date : ")
        date_2 = st.date_input("Enter your release date : ")
        if st.button("save date admission and release"):
            Archive.enregistrer_date_sorti_entree_patient()    #appel de la fonction static dans le bouton

    if st.button("save patient"):
            Archive.enregistrer_patient()      #appel de la fonction static dans le bouton

with col2:                #initialisation de la deuxième colonne
    st.title("     ")     #permets de créer un espace entre les colonnes et d'aérer l'appli

with col3:                #initialisation de la troisième colonne
    st.title("Register an RH")
    nom_rh = st.text_input("Enter your RH name").upper()
    prenom_rh = st.text_input("Enter your  RH first name")
    salaire = st.slider("Enter your salaire", min_value = 1000, max_value = 10000)
    st.write(salaire)
    id = "RH" + "-" + nom_rh.upper() + "-" + prenom_rh
    working_at_hospital = st.radio("Are you still working in the hospital ?",
                                (True, False))
    
    if working_at_hospital == True:
        CDD_or_CDI =st.radio("Are you in CDD or CDI ?", 
                              ("CDD", "CDI"))
        if CDD_or_CDI == "CDD":
            date_debut_CDD = st.date_input("Enter the start date of your CDD : ")
            date_fin_CDD = st.date_input("Enter the end date of your CDD : ")
            if st.button("save date of CDD contract"):
                Archive.enregistrer_date_debut_fin_cdd()     #appel de la fonction static dans le bouton
        else:
            date_debut_CDI = st.date_input("Enter the start of date of your CDI : ")
            if st.button("save start date of CDI contract"):
                Archive.enregistrer_date_debut_cdi()     #appel de la fonction static dans le bouton
    
    else:
        CDI = "CDI"
        date_debut_CDI = st.date_input("Enter the beginning of date of your CDI : ")
        date_fin_CDI = st.date_input("Enter the end date of your CDI : ")
        if st.button("save date of CDI contract"):
            Archive.enregistrer_date_debut_fin_cdi()  #appel de la fonction static dans le bouton


    if st.button("save RH"):
        Archive.enregistrer_rh()  #appel de la fonction static dans le bouton

with col4:           #initialisation de la quatrieme colonne 
    st.title("     ")  #permets de créer un espace entre les colonnes et d'aérer l'appli

with col5:           #initialisation de la cinquieme  colonne
    st.title("Press the button to see the archives")
    if st.button("Show archive"):
        st.write(pd.DataFrame(Archive.afficher_les_archives_streamlit()))   #appel de la fonction static dans le bouton

#import qrcode
from datetime import datetime, timedelta
import random
import mysql.connector

class Ticket:
    def __init__(self):
        self.num_serie = (random.randint(12345,2000000))
        self.date_today = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        self.date_fin = datetime.now() + timedelta(days = 7)
        self.validite_ticket = 120
        
        
####################################
#FONCTIONS AFFICHAGE DE TICKET
#############################
    #FONCTION QR CODE
    # def qrcode_classe1(self):
    #     donnee = (f"Produit :{self.produit} \n Prix : {self.prix_classe1} \n Num Serie: {self.num_serie} \n \
    #     Date :{self.date_today} \nValidite : {self.validite_ticket} \nFin Ticket :{self.date_fin} \n Bon voyage !!!! ")
    #     img = qrcode.make(donnee)
    #     img.save("classe1.png") 
        
    # def qrcode_zone1(self):
    #     donnee = (f"Produit :{self.produit1} \n Prix : {self.prix_zone1} \nNum Serie {self.num_serie} \n \
    #     Date :{self.date_today} \nValidite : {self.validite_ticket} \nFin Ticket :{self.date_fin} \n Bon voyage !!!! ")
    #     img = qrcode.make(donnee)
    #     img.save("zone1.png") 
  
    # def qrcode_zone2(self):
    #     donnee = (f"Produit :{self.produit2} \n Prix : {self.prix_zone2} \nNum Serie : {self.num_serie} \n \
    #     Date :{self.date_today} \nValidite : {self.validite_ticket} \nFin Ticket :{self.date_fin}\n Bon voyage !!!! ")
    #     img = qrcode.make(donnee)
    #     img.save("zone2.png")
        
    # def qrcode_zone3(self):
    #     donnee = (f"Produit :{self.produit3} \n Prix : {self.prix_zone3} \n num serie : {self.num_serie} \n \
    #     Date :{self.date_today} \nValdite : {self.validite_ticket} \nFin Ticket :{self.date_fin} \n Bon voyage !!!! ")
    #     img = qrcode.make(donnee)
    #     img.save("zone3.png") 
########################################
    # creation du menu classe   
    def menu_classes(self):
        print("SYSTEME DE VENTE DE BILLET DE TER SENEGAL :")
        print("------------------------------------------\n")
        print("VEILLER CHOISIR LE TYPE DE BILLET A ACHETER \n")

        classes = ["1.Première classe","2.Deuxième classe","3.Quiter \n"]
        for classe in classes:
            print(classe ,"\n")
        
        
        while True:
            self.choix_classe = int(input("Entrer votre classe svp  :"))
            if self.choix_classe == 1:
                self.premier_classe()
            elif self.choix_classe == 2:
                self.deuxieme_classe()
                break
            elif self.choix_classe == 3:
                break
    #############################################        
    # creation de la fonction de la  classe vip
    def premier_classe(self):
        print(f"Vous avez choisi la première classe :\n")
        print("--------------------------------------------")
        self.produit = "Billet 1 er classe"
        self.prix_classe1 = 2500
        print(f" Produit : {self.produit} \n Prix : {self.prix_classe1} Fcfa\n Numero Serie : {self.num_serie}\n Date et heure emission : {self.date_today} \n Validité de la course : {self.validite_ticket} mn\n Fin de validité du support :{self.date_fin}")
        #self.qrcode_classe1()
        print(f" Zones autorisées [Dakar - Diamniadio ] ")
        self.base_classe1()
        print("-------------------------------------------")
    ######## ENREGISTRER DANS UN FICHIER
        with open("Clasee1.txt","a") as fichiers:
            fichiers.write(f" Produit : {self.produit} \n Prix : {self.prix_classe1} Fcfa\n Numero Serie : {self.num_serie}\n Date et heure emission: {self.date_today} \n Validité de la course : {self.validite_ticket} mn\n Fin de validite du support : {self.date_fin}\n\n")

     #######################################   
    # creation de la fonction classe simple   
    def deuxieme_classe(self):
        print("vous avez choisi la deuxième classe :\n")
        zones = ["-> (1) Zone 1","-> (2) Zone 2","-> (3) Zone 3","-> (4) Retour"]
        for zone in zones:
            print(zone ,"\n")   
        while True:
            self.choix_zone = int(input("VEILLEZ CHOISIR VOTRE ZONE :")) 
            if self.choix_zone == 1:
                self.zone_un()
                #self.qrcode_zone1()
                break
            elif self.choix_zone == 2:
                self.zone_deux()
                #self.qrcode_zone2()
                break
            elif self.choix_zone == 3:
                self.zone_trois()
                #self.qrcode_zone3()
                break
            elif self.choix_zone == 4:
                self.menu_classes()
            else:
                print("faites un choix valide")
            
    def zone_un(self):
        self.produit1 = "Billet 2 eme classe"
        self.prix_zone1 = 500
        print("--------------------------------------------")
        print(f" Produit : {self.produit1} \n Prix : {self.prix_zone1} Fcfa\n Numero Serie : {self.num_serie}\n Date et heure emission: {self.date_today} \n Validité de la course : {self.validite_ticket} mn\n Fin de validite du support : {self.date_fin}")

        print(f" Zone 1 autorisée [Dakar - Thiaroye ] ")
        self.base_zone1()
        print("--------------------------------------------")
    ###### Enregistrer dans un fichier
    
        with open("zone1.txt","a") as fichiers:
            fichiers.write(f" Produit : {self.produit1} \n Prix : {self.prix_zone1} Fcfa\n Numero Serie : {self.num_serie}\n Date et heure emission: {self.date_today} \n Validité de la course : {self.validite_ticket} mn\n Fin de validite du support : {self.date_fin}\n\n")

    #creation de fonction zone 2
    def zone_deux(self):
        self.produit2 = "Billet 2 eme classe "
        self.prix_zone2 = 1000
        print("---------------------------------------------------------")
        print(f" Produit : {self.produit2} \n Prix : {self.prix_zone2} Fcfa\n Numero Serie :{self.num_serie}\n Date et heure emission : {self.date_today} \n Validité de la course : {self.validite_ticket} mn\n Fin de validité du support : {self.date_fin}")

        print(f" Zone 2 autorisée [Dakar - Thiaroye -Thiaroye - Bargny ]")
        self.base_zone2()
        print("-----------------------------------------------------------")
    ######## ENREGISTRER DANS UN FICHIER
        with open("zone2.txt","a") as fichiers:
            fichiers.write(f" Produit : {self.produit2} \n Prix : {self.prix_zone2} Fcfa\n Numero Serie : {self.num_serie}\n Date et heure emission: {self.date_today} \n Validité de la course : {self.validite_ticket} mn\n Fin de validite du support : {self.date_fin}\n\n")

    
    #creation de la fonction zone 3
    def zone_trois(self):
        self.produit3 = "Billet 2 eme classe"
        self.prix_zone3 = 1500
        print("---------------------------------------------------")       
        print(f" Produit : {self.produit3} \n Prix : {self.prix_zone3} Fcfa\n Numero Serie :{self.num_serie}\n Date et heure emission : {self.date_today} \n Validité de la course : {self.validite_ticket} mn\n Fin de validité du support : {self.date_fin}")

        print(f" Zone 3 autorisée [Dakar - Diamniadio ]")
        self.base_zone3()
        print("---------------------------------------------------")
        
    ##### ENREGISTRER DANS UN FICHIER
        with open("zone3.txt","a") as fichiers:
            fichiers.write(f" Produit : {self.produit3} \n Prix : {self.prix_zone3} Fcfa\n Numero Serie : {self.num_serie}\n Date et heure emission: {self.date_today} \n Validité de la course : {self.validite_ticket} mn\n Fin de validite du support : {self.date_fin}\n\n")

    ########################################
    # BASE DE DONNEE 
    def base_classe1(self):
        db = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "",
        database = "examen"
        )
        cur = db.cursor()

        #requéte SQL
        sql = "INSERT INTO classe1 (num_serie,prix,produit,date_today,validite_ticket,date_fin) VALUES (%s, %s, %s, %s, %s, %s)"
        #les valeurs de la requéte SQL
        value = [
            (self.num_serie,self.prix_classe1,self.produit,self.date_today,self.validite_ticket,self.date_fin)
        
                ]
        cur.executemany(sql,value)
        db.commit()
        print("\n \n",cur.rowcount, " Données enregistées.")
    ##########BASE ZONE 1    
    def base_zone1(self):
        db = mysql.connector.connect(
         host = "localhost",
         user = "root",
        password = "",
        database = "examen"
        )
        cur = db.cursor()

        #requéte SQL
        sql = "INSERT INTO zone1 (num_serie,prix,produit,date_today,validite_ticket,date_fin) VALUES (%s, %s, %s, %s, %s, %s)"
        #les valeurs de la requéte SQL
        value = [
            (self.num_serie,self.prix_zone1,self.produit1,self.date_today,self.validite_ticket,self.date_fin)
        
                ]
        cur.executemany(sql,value)
        db.commit()
        print("\n \n",cur.rowcount, " Données enregistées.") 
     ############## ZONE 2   
    def base_zone2(self):
        db = mysql.connector.connect(
         host = "localhost",
         user = "root",
        password = "",
        database = "examen"
        )
        cur = db.cursor()

        #requéte SQL
        sql = "INSERT INTO zone2 (num_serie,prix,produit,date_today,validite_ticket,date_fin) VALUES (%s, %s, %s, %s, %s, %s)"
        #les valeurs de la requéte SQL
        value = [
            (self.num_serie,self.prix_zone2,self.produit2,self.date_today,self.validite_ticket,self.date_fin)
        
                ]
        cur.executemany(sql,value)
        db.commit()
        print("\n \n",cur.rowcount, " Données enregistées.")
    
    ################## ZONE 3
    def base_zone3(self):
        db = mysql.connector.connect(
         host = "localhost",
         user = "root",
        password = "",
        database = "examen"
        )
        cur = db.cursor()

        #requéte SQL
        sql = "INSERT INTO zone3 (num_serie,prix,produit,date_today,validite_ticket,date_fin) VALUES (%s, %s, %s, %s, %s, %s)"
        #les valeurs de la requéte SQL
        value = [
            (self.num_serie,self.prix_zone3,self.produit3,self.date_today,self.validite_ticket,self.date_fin)
        
                ]
        cur.executemany(sql,value)
        db.commit()
        print("\n \n",cur.rowcount, " Données enregistées.")     
    
ticket = Ticket()
ticket.menu_classes()

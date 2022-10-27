from typing import List, Optional

from utils.singleton import Singleton
from dao.db_connection import DBConnection
from business_object.utilisateur import Utilisateur


class DAOprofil(metaclass=Singleton):
    ######################## CHANGER DE MAIL ######################
    def changer_mail(self,user: Utilisateur, nouveau_mail):
        request=  "UPDATE UTILISATEUR"\
                    "SET UTILISATEUR.mail=%(mail)s"\
                    "WHERE id=%(id)s"  
        connection=DBConnection().connection
        with connection.cursor() as cursor :
            cursor.execute(
                request,
                {"mail":nouveau_mail,
                "id":user.id()
                })
            res = cursor.fetchone()
            if res :
                created = True
            return created                


####################### CHANGER DE MOT DE PASSE #####################
    def changer_MDP(self,user: Utilisateur, nouveau_mdp):
        request=  "UPDATE UTILISATEUR"\
                    "SET UTILISATEUR.mdp=%(mdp)s"\
                    "WHERE id=%(id)s"  
            
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:

                cursor.execute(
                    request,
                    {"mdp":nouveau_mdp,
                    "id":user.id
                    })
                res = cursor.fetchone()
        if res :
            update = True
        return update                    



###################### CREER SON COMPTE #####################
    def creer_compte(self,user: Utilisateur):
        with DBConnection().connection as connection:
            with connection.cursor() as cursor :

                cursor.execute(
                    "INSERT INTO UTILISATEUR (id, mdp, mail, date_de_naissance" \
                    ") VALUES (%(mdp)s, %(mail)s, %(date_de_naissance)s "\
                    ,{"id": user.id,
                    "mdp": user.mdp,
                    "mail": user.mail,
                    "date_de_naissance": user.date_de_naissance
                    })
                res = cursor.fetchone()
        if res :
            created = True
        return created    


###################### SE CONNECTER #####################
    def connexion(self):
        with DBConnection().connection as connection:
            with connection.cursor() as cursor :
                cursor.execute(
                    "SELECT COUNT(1) FROM UTILISATEUR"\
                    "WHERE (%(mail)s, %(mdp)s",
                    {"mdp": mdp,
                    "mail": mail}
                    )
                res = cursor.fetchone()    
        if res :
            print("Felicitations, vous êtes connectez")  
                                          



       
###################### SE DECONNECTER #####################
    def deconnexion(self):
        pass


###################### RECHERCHER UN PROFIL #####################
    def find_profil(self,mail):

        with DBConnection().connection as connection:
            with connection.cursor() as cursor :
                cursor.execute(
                    "SELECT COUNT(1) FROM UTILISATEUR"\
                    "WHERE mail = (%(mail)s",
                    {
                    "mail": mail}
                    )
                res = cursor.fetchone()    
        if res :
            user = Utilisateur(mail = res["mail"],
                                nom = res["nom"],
                                prenom = res["prenom"],
                                mdp = res["mdp"],
                                date_de_naissance = res["date_de_naissance"],
            )
            return  user
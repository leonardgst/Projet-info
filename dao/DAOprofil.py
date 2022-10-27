from typing import List, Optional

from utils.singleton import Singleton
from dao.db_connection import DBConnection
from utilisateur import Utilisateur


class DAOprofil(metaclass=Singleton):
    ######################## CHANGER DE MAIL ######################
    def changer_mail(self):
       
        ## Verifie si le mail existe deja
        request=   "SELECT UTILISATEUR.mail from UTILISATEUR ut"\
                    "WHERE id=%(id)s"

        connection=DBConnection().connection
        with connection.cursor() as cursor:
            cursor.execute(request
                {"id"=id})
            res = cursor.fetchone()
        ## Si le mail existe pour cet utilisateur, on le modifie    
        if res:
            request=  "UPDATE UTILISATEUR"\
                      "SET UTILISATEUR.mail=%(mail)s"\
                      "WHERE id=%(id)s"  
            connection=DBConnection().connection
            with connection.cursor() as cursor :
                cursor.execute(
                    request
                    {"mail"=mail,
                    "id"=id
                    })
                res = cursor.fetchone()
                if res :
                    created = True
                return created                
        else:
            print("le mail saisi est incorrect,reassayer")

####################### CHANGER DE MOT DE PASSE #####################
    def changer_MDP(self):
        request=   "SELECT UTILISATEUR.mdp from UTILISATEUR ut"\
                    "WHERE id=%(id)s"

        connection=DBConnection().connection
        with connection.cursor() as cursor:
            cursor.execute(
                request
                {"id"=id})
            res = cursor.fetchone()
        ## Si le mot de passe existe pour cet utilisateur, on le modifie    
        if res:
            request=  "UPDATE UTILISATEUR"\
                      "SET UTILISATEUR.mdp=%(mdp)s"\
                      "WHERE id=%(id)s"  
            connection=DBConnection().connection

            with connection.cursor() as cursor:

                cursor.execute(
                    request
                    {"mdp"=mdp,
                    "id"=id
                    })
                res = cursor.fetchone()
            if res :
                update = True
            return update                    
        else:
            print("le mot de passe saisi est incorrect,reassayer")


###################### CREER SON COMPTE #####################
    def creer_compte(self):
        with DBConnection().connection as connection:
            with connection.cursor() as cursor :
                cursor.execute(
                    "INSERT INTO UTILISATEUR (id, mdp, mail" \
                    ") VALUES (%(mdp)s, %(mail)s"\
                    {"id": id,
                    "mdp": mdp,
                    "mail": mail,}
                    )
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
                    "WHERE (%(mail)s, %(mdp)s"\
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
    def find_profil(self,id,mdp):

        with DBConnection().connection as connection:
            with connection.cursor() as cursor :
                cursor.execute(
                    "SELECT COUNT(1) FROM UTILISATEUR"\
                    "WHERE (%(mail)s, %(mdp)s"\
                    {"mdp": mdp,
                    "mail": mail}
                    )
                res = cursor.fetchone()    
                if res :
                    print("Felicitations, vous êtes connectez")       
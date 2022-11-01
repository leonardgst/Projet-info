from typing import List, Optional

from utils.singleton import Singleton
from dao.db_connection import DBConnection
from business_object.utilisateur.utilisateur import Utilisateur


class DAOprofil(metaclass=Singleton):
    ######################## CHANGER DE MAIL ######################
    def changer_mail(self,user: Utilisateur, nouveau_mail):
        request=  "UPDATE utilisateur "\
                    "SET mail=%(mail)s RETURNING id_user "
        connection=DBConnection().connection
        with connection.cursor() as cursor :
            cursor.execute(
                request,
                {"mail":nouveau_mail
                })
            res = cursor.fetchone()
            if res :
                created = True
            return created                


####################### CHANGER DE MOT DE PASSE #####################
    def changer_MDP(self,user: Utilisateur, nouveau_mdp):
        request=  "UPDATE utilisateur "\
                    "SET mdp=%(mdp)s "\
                    "WHERE mail=%(mail)s RETURNING id_user "  
            
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:

                cursor.execute(
                    request,
                    {"mdp":nouveau_mdp,
                    "mail":user.mail
                    })
                res = cursor.fetchone()
        if res :
            update = True
        return update                    



###################### CREER SON COMPTE #####################
    def creer_compte(self,user: Utilisateur):
        created = False
        with DBConnection().connection as connection:
            with connection.cursor() as cursor :
                cursor.execute(
                    "INSERT INTO utilisateur (mail,MDP,dateNaissance, nom, prenom" \
                    ") VALUES (%(mail)s, %(MDP)s, %(dateNaissance)s, %(nom)s, %(prenom)s) RETURNING id_user"\
                    ,{
                    "MDP": user.MDP,
                    "mail": user.mail,
                    "nom": user.nom,
                    "prenom": user.prenom,
                    "dateNaissance": user.dateNaissance
                    })
                res = cursor.fetchone()
        if res:
            created = True
        
        return created
        

            


###################### SE CONNECTER #####################
    def connexion(self,mail, MDP):
        user = Utilisateur()
        with DBConnection().connection as connection:
            with connection.cursor() as cursor :
                cursor.execute(
                    "SELECT * FROM utilisateur "\
                    "WHERE utilisateur.mail = %(mail)s AND utilisateur.MDP = %(mdp)s ",
                    {"mdp": MDP,
                    "mail": mail}
                    )
                res = cursor.fetchone()    
        if res :
            user = Utilisateur(
                id  = res['id_user'],
                mail = res['mail'],
                prenom= res['prenom'],
                nom= res['nom'],
                MDP= res['mdp'],
                dateNaissance= res['datenaissance']
            )

        return user
            
                                          



       




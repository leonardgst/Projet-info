from email.message import Message
from pprint import pprint


from InquirerPy.validator import PasswordValidator
from InquirerPy import inquirer
from InquirerPy.base.control import Choice

from view.abstract_view import AbstractView
from view.session import Session
from business_object.utilisateur import Utilisateur

from dao.DAOprofil import DAOprofil

ASK_USERNAME=inquirer.text(message = 'Quel est votre user_name?')
ASK_PASSWORD=inquirer.secret(message='What\'s your password.',
        transformer=lambda _: "[hidden]",)


class ConnexionView(AbstractView):


    def display_info(self):
        print(f"CONNEXION")

    def make_choice(self):
        user_name = ASK_USERNAME.execute()
        mdp =ASK_PASSWORD.execute()
        
        ####### VERIFICATION  DE L'EXISTANCE DU COMPTE #####

        if DAOprofil().connexion():
            print("Felicitations, vous êtes connectez")
            Session().user_user = user
            from view.choix_view import ChoixView
            return ChoixView()

        else:
            print('Username ou mot de passe incorrect')
            from view.start_view import StartView
            return StartView()

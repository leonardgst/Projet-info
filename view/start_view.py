from InquirerPy import inquirer
from InquirerPy.base.control import Choice

from view.abstract_view import AbstractView
from view.session import Session


class StartView(AbstractView):

    def __init__(self):
        self.__questions = inquirer.select(
            message=f'Bonjour {Session().user_name}'
            , choices=[
                Choice('Créer votre compte')
                ,Choice('Se connecter')
                ]
        )
        


    def make_choice(self):
        reponse = self.__questions.execute()
        if reponse == 'Créer votre compte':
            from view.sign_in_view import SignIn
            return SignIn()

        elif reponse== 'Se connecter':
            from view.connexion_view import ConnexionView
            return ConnexionView()



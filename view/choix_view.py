from InquirerPy import inquirer
from InquirerPy.base.control import Choice

from view.abstract_view import AbstractView
from view.session import Session


class StartView(AbstractView):

    def __init__(self):
        self.__questions = inquirer.select(
            message=f'Bonjour {Session().user_name}'
            , choices=[
                Choice('Se déconnecter')
                ,Choice('Faire une recherche')
                ]
        )
        


    def make_choice(self):
        reponse = self.__questions.execute()
        if reponse == 'Faire une recherche':
            from view.recherche_view import RechercheView
            return RechercheView()

        elif reponse== 'Se déconnecter':
            Session().user = None
            
            from view.start_view import StartView
            return StartView()



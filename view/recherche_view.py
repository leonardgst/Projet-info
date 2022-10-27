"""
* Checkbox question example
* run example by typing `python example/checkbox.py` in your console
From : https://github.com/CITGuru/PyInquirer/blob/master/examples/checkbox.py
"""
from pprint import pprint

from InquirerPy import inquirer
from InquirerPy.base.control import Choice
from InquirerPy.separator import Separator

from prompt_toolkit.validation import Validator, ValidationError
from view.abstract_view import AbstractView
from view.session import Session

DEPART_SELECTION = inquirer.checkbox(
            message="Votre gare de départ: "
            ,choices=[
                Choice('Nom1')
                ,Choice('Nom2')
                ]
        )

ARRIVEE_SELECTION = inquirer.checkbox(
            message="Votre gare d'arrivée"
            ,choices=[
                Choice('Nom1')
                ,Choice('Nom2')
                ]
        )

DATE_SELECTION = inquirer.text(
            message="Choisir votre date de départ (sous forme dd/mm/yyyy): ")

ELIGIBLE = inquirer.checkbox(
            message="Places eligible au TGVMax? "
            ,choices=[
                Choice('OUI')
                ,Choice('NON')
            ]
)


class RechercheView(AbstractView):
    def __init__(self):
        self.__questions = inquirer.select(
            message=f'Bonjour {Session().user_name}, vous cherchez des trajets: '
            , choices=[
                Choice('Aller simple')
                ,Choice('Des destinations atteignables durant un weekend')
                ]
        )
        
    def display_info(self):
        print(f"Hello {Session().user_name}, veuillez saisir vos critères")

    def make_choice(self):
        response = self.__questions.execute()

        if response == 'Aller simple':
            depart = DEPART_SELECTION.execute()
            arrivee = ARRIVEE_SELECTION.execute()
            date = DATE_SELECTION.execute()
            eligible = ELIGIBLE.execute()
            resultat = Recherche
        elif response== 'Des destinations atteignables durant un weekend':
            from view.checkbox_example_view import CheckBoxExampleView
            return CheckBoxExampleView()
        elif response == 'Déconnexion':
            Session().user_name = None
            Session().user_mdp = None
            
            from view.start_view import StartView
            return StartView()


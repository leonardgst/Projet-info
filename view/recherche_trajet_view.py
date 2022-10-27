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

TEAM_SELECTION = inquirer.checkbox(
            message="Select your Pokemon Team"
            ,choices=[
                Separator('🔥Fire Starter')
                ,Choice('Charmander')
                ,Choice('Cyndaquil')
                ,Choice('Torchic')
                ,Choice('Chimchar')
                ,Choice('Oshawott')
                ,Separator('🚿Water starter')
                ,Choice('Squirtle')
                ,Choice('Totodile')
                ,Choice('Mudkip')
                ,Choice('Turtwig')
                ,Choice('Tepig')
                ,Separator('🌱Grass starter')
                ,Choice('Bulbasaur')
                ,Choice('Chikorita')
                ,Choice('Treecko')
                ,Choice('Piplup')
                ,Choice('Snivy')
            ]
        )


class CheckBoxExampleView(AbstractView):
        
    def display_info(self):
        print(f"Hello {Session().user_name}, please choose some pokemon")

    def make_choice(self):
        answers = TEAM_SELECTION.execute()
        pprint(answers)
        from view.start_view import StartView
        return StartView()


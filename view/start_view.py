from InquirerPy import inquirer
from InquirerPy.base.control import Choice

from view.abstract_view import AbstractView
from view.session import Session


class StartView(AbstractView):

    def __init__(self):
        self.__questions = inquirer.select(
            message=f'Bonjour {Session().user_name}'
            , choices=[
                Choice('Checkbox example')
                ,Choice('Sign In example')
                ,Choice("Pokemon choice")
                ,Choice("Nothing")]
        )
        

    def display_info(self):
        with open('graphical_assets/banner.txt', 'r', encoding="utf-8") as asset:
            print(asset.read())

    def make_choice(self):
        reponse = self.__questions.execute()
        if reponse == 'Nothing':
            pass
        elif reponse== 'Checkbox example':
            from view.checkbox_example_view import CheckBoxExampleView
            return CheckBoxExampleView()
        elif reponse== 'Sign In example':
            from view.sign_in_example import SignInExample
            return SignInExample()
        elif reponse== 'Pokemon choice':
            from view.change_pokemon_view import ChangePokemonView
            return ChangePokemonView()


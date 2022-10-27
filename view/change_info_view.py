from pprint import pprint

from InquirerPy import inquirer
from InquirerPy.base.control import Choice
from InquirerPy.separator import Separator

from InquirerPy.validator import EmptyInputValidator
from view.session import Session

POKEMON_SELECTION = inquirer.select(
            message="Select your first Pokemon"
            , choices=[
                Choice("Bulbasaur")
                ,Choice("Charmander")
                ,Choice("Squirtle")
                ]
)

LEVEL_SELECTION = inquirer.number(
                message='Select your Pokemon level'
                ,min_allowed=1
                ,max_allowed=100
                ,validate=EmptyInputValidator(),
        )

class ChangePokemonView(AbstractView):

    def display_info(self):
        if Session().selected_pokemon:
            print(f"Your selected pokemon is {Session().selected_pokemon.name}"\
            f"and it is level {Session().selected_pokemon.level}")
        else :
            print("You don't have any selected pokemon")

    def make_choice(self):
        pokemon_name = POKEMON_SELECTION.execute()
        pokemon_level = LEVEL_SELECTION.execute()

        pokemon_service = PokemonService()
        # Add a pokemon in the session
        Session().selected_pokemon= pokemon_service.get_pokemon_with_identifier_from_webservice(pokemon_name)

        # Change its level
        Session().selected_pokemon.level = pokemon_level
        return ChangePokemonView()


from pprint import pprint

from InquirerPy import inquirer
from InquirerPy.base.control import Choice
from InquirerPy.separator import Separator

from InquirerPy.validator import EmptyInputValidator
from view.session import Session
from dao.DAOprofil import DAOprofil

ASK_MAIL= inquirer.text(
            message="Votre nouvelle addresse mail"
)
ASK_OLD_PASSWORD=inquirer.secret(message='Votre nouveau mot de passe',
        transformer=lambda _: "[hidden]",)

ASK_NEW_PASSWORD=inquirer.secret(message='Votre nouveau mot de passe',
        transformer=lambda _: "[hidden]",)

class ChangerInfo(AbstractView):
    def __init__(self):
        self.__questions = inquirer.select(
                message=f'Bonjour {Session().user_name}, vous voulez: '
                , choices=[
                    Choice('Changer votre mot de passe')
                    ,Choice('Changer votre addresse mail')
                    ]
            )
                    

    def make_choice(self):

        response = self.__questions.execute()

        if response == 'Changer votre addresse mail':
            mail = ASK_MAIL.execute()
            created = DAOprofil().changer_mail(Session().user, mail)
            if created:
                print('Addresse mail a été changé')
                from view.choix_view import ChoixView
                return ChoixView()
            else:
                print('Le changement a échoué, merci de rééssayer')
                return ChangerInfo()

        elif response == 'Changer votre mot de passe':
            #### VERIFIER L'UTILISATEUR #######
            ancien_mdp = ASK_OLD_PASSWORD.execute()
            if ancien_mdp == Session().user.mdp:

                nouveau_mdp = ASK_NEW_PASSWORD.execute()
                created = DAOprofil().changer_MDP(Session().user, nouveau_mdp)
                if created:
                    print('Votre mot de passe a été changé')
                    from view.choix_view import ChoixView
                    return ChoixView()
                else:
                    print('Le changement a échoué, merci de rééssayer')
                    return ChangerInfo()
            
            else:
                print('Mot de passe incorrect')
                from view.choix_view import ChoixView
                return ChoixView()


from time import strptime
from abstractrecherche import AbstractRecherche
from DataLayer.DAO.db_connexion import DBConnexion
from creation_table import Table_recherche
from datetime import datetime  

class RechercheDestination(AbstractRecherche):
    def __init__():
        """Créer une instance de RechercheDestination"""

    def recherche(self, date, origine, alerter : bool = False, eligible = "OUI"):
        origine_str = str(origine).replace(" ", "+")
        origine_str = origine_str.upper()
        date_obj = datetime.strptime(date, '%Y/%m/%d')
        jour = str(date_obj.day)
        mois = str(date_obj.month)
        annee = str(date_obj.year)
        url = "https://data.sncf.com/api/records/1.0/search/?dataset=tgvmax&q=&rows=10000&sort=-date&refine.origine=" + origine_str + "&refine.date=" + annee + "%2F" + mois +  "%2F" + jour + "&exclude.od_happy_card=" + eligible
        data = Table_recherche().creation_table(url)



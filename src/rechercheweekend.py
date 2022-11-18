from time import strptime
from datetime import datetime, timedelta
from abstractrecherche import AbstractRecherche
from DataLayer.DAO.db_connexion import DBConnexion
from creation_table import Table_recherche
from datetime import datetime

class RechercheTrajet(AbstractRecherche):
    
    def __init__():
        """Créer une instance de RechercheTrajet"""

    def recherche(self, date, origine, destination, alerter = False, eligible = "OUI"):
        origine_str = str(origine).replace(" ", "+")
        origine_str = origine_str.upper()
        destination_str = str(destination).replace(" ", "+")
        destination_str = destination_str.upper()
        date_obj_aller = datetime.strptime(date, '%Y/%m/%d')
        date_obj_retour = date_obj_aller + timedelta(days = 2)
        jour_aller = str(date_obj_aller.day)
        mois_aller = str(date_obj_aller.month)
        annee_aller = str(date_obj_aller.year)
        jour_retour = str(date_obj_retour.day)
        mois_retour = str(date_obj_retour.month)
        annee_retour = str(date_obj_retour.year)
        url_aller = "https://data.sncf.com/api/records/1.0/search/?dataset=tgvmax&q=&rows=10000&sort=-date&refine.origine=" + origine_str + "&refine.destination=" + destination_str + "&refine.date=" + annee_aller + "%2F" + mois_aller +  "%2F" + jour_aller + "&exclude.od_happy_card=" + eligible
        url_retour = "https://data.sncf.com/api/records/1.0/search/?dataset=tgvmax&q=&rows=10000&sort=-date&refine.origine=" + destination_str + "&refine.destination=" +  origine_str + "&refine.date=" + annee_retour + "%2F" + mois_retour +  "%2F" + jour_retour + "&exclude.od_happy_card=" + eligible
        Table_recherche().creation_table(url_aller)
        Table_recherche().creation_table(url_retour)

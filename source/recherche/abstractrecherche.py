from abc import ABC, abstractmethod

class AbstractRecherche(ABC):
    """
    An abstract Recherche. As an abstract class, it as to be inherited
    """
    @abstractmethod
    def recherche(self):
        """Méthode abstraite de recherche""" 
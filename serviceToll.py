from dbToll import DBToll
from toll import Toll

class ServiceToll:

    def __init__(self):
        self.db = DBToll()

    def AddPassagem(self, placa):
        obj = self.db.UpdateHistory(placa)

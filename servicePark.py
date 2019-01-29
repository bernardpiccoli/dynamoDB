from dbPark import DBPark
from park import Park
import json
import time

from utils import Utils
uts = Utils()

class ServicePark:

    def __init__(self):
        self.db = DBPark()
        self.tarifa = 4

    def Entrar(self, placa):
        self.db.Create(placa)
        self.Imprimir(uts.DataHoraAgora(), placa)

    def Sair(self, placa):
        obj = self.db.ReadObj(placa)
        obj.saida = uts.DataHoraAgora()
        obj.permanencia = str(self.Permanecia(uts.ToTimestamp(obj.entrada), uts.ToTimestamp(obj.saida)))
        permanencia = round(float(obj.permanencia)/60)
        obj.valor = str(self.Calcular(uts.ToTimestamp(obj.entrada), uts.ToTimestamp(obj.saida), self.tarifa))
        valor = round(float(obj.valor),2)
        print("Voce ficou "+ str(permanencia) + " minutos e pagara "+ str(valor) +" Deseja encerrar?" )
        time.sleep(5)
        self.Pagar(obj)
        self.db.Create(obj)

    def Imprimir(self, entrada, placa):
        uts.NewQr(entrada, placa)

    def Calcular(self, entrada, saida, tarifa):
        tarifa_s = tarifa/3600.0
        permanencia = (saida - entrada) 
        valor = permanencia *tarifa_s
        return valor

    def Pagar(self, obj):
        obj.pago = True

    def Patio(self):
        obj = self.db.ReadAll()
        return obj

    def Permanecia(self, entrada, saida):
        permanencia = (saida - entrada)
        return permanencia
        
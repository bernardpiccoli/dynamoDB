import time
from utils import Utils
uts = Utils()
import decimal
import datetime


class Park(object):
    def __init__(self, placa, entrada=uts.DataHoraAgora(), saida=None, valor=None, permanencia=None, pago=False):
        self.placa = placa.upper()
        self.entrada = str(entrada)
        self.saida = saida
        self.valor = valor
        self.permanencia = permanencia
        self.pago = pago

    @staticmethod
    def ToObj(source):
        park = Park(source[u'placa'], source[u'entrada'], source[u'pago'])
        if u'saida' in source:
            park.saida = source[u'saida']
        if u'valor' in source:
            park.valor = source[u'valor']
        if u'permanencia' in source:
            park.permanencia = source[u'permanencia']
        return park

    def ToJson(self):
        dest = {
            u'placa': uts.Codificar(self.placa),
            u'entrada': self.entrada,
            u'pago': self.pago
        }
        if self.saida:
            dest[u'saida'] = self.saida
        if self.valor:
            dest[u'valor'] = self.valor
        if self.valor:
            dest[u'permanencia'] = self.permanencia
        return dest

    def __repr__(self):
        return u'Park(placa={}, entrada={}, saida={}, valor={}, permanencia={}, pago={})'.format(
            self.placa, self.entrada, self.saida, self.valor, self.permanencia, self.pago)

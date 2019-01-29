from utils import Utils
uts = Utils()

class Gate(object):
    def __init__(self, proprietario, marca, modelo, cor, placa, lstHistorico=None):
        self.proprietario = proprietario
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.placa = placa

        if(lstHistorico is not None):
            self.historico = lstHistorico
        else:
            self.historico = list()

    @staticmethod
    def ToObj(source):
        gate = Gate(source[u'proprietario'], source[u'apartamento'],
                    source[u'marca'], source[u'modelo'], source[u'cor'], source[u'placa'])

        if u'historico' in source:
            gate.historico = source[u'historico']
        return gate

    def ToJson(self):
        dest = {
            u'proprietario': uts.codificar(self.proprietario),
            u'apartamento': uts.codificar(self.apartamento),
            u'marca': uts.codificar(self.marca),
            u'modelo': uts.codificar(self.modelo),
            u'cor': uts.codificar(self.cor),
            u'placa': uts.codificar(self.placa.upper()),
        }

        if self.historico:
            dest[u'historico'] = self.historico
        return dest

    def __repr__(self):
        return u'Gate(proprietario={}, apartamento={}, marca={}, modelo={}, cor={} , placa={})'.format(
            self.proprietario, self.apartamento, self.marca, self.modelo, self.cor, self.placa)
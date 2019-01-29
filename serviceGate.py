from firebaseGate import firebaseGate

from json import JSONDecoder
import json

from utils import Utils
uts = Utils()

from gate import Gate


class serviceGate:

    def __init__(_self, firebase):
        _self.firebase = firebase

    def ADD_ACESSO(self, placaReferencia):
        obj = self.firebase.READ(placaReferencia)
        if 'acessos' in obj:
            g1 = Park(obj['proprietario'],  obj['apartamento'], obj['marca'], obj['modelo'],  obj['cor'], placaReferencia, obj['acessos'])
        else:
            g1 = Park(obj['proprietario'],  obj['apartamento'], obj['marca'], obj['modelo'],  obj['cor'], placaReferencia, [])
        
        g1.ACESSAR()
        print("Acessado")
        self.firebase.UPDATE_(g1)
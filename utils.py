import datetime
import time
import qrcode
import decimal


class Utils:

    def Codificar(self, texto):
        return texto.decode('utf-8')

    def DataAgora(self):
        return datetime.datetime.now().strftime('%d/%m/%Y')

    def HoraAgora(self):
        return datetime.datetime.now().strftime('%H:%M:%S')

    def DataHoraAgora(self):
        return datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    def Timestamp(self):
        return time.time()

    def TimestampDate(self, ts):
        return datetime.datetime.fromtimestamp(ts).strftime("%d/%m/%Y %H:%M:%S")

    def DateTimestamp(self, d):
        return time.mktime(datetime.datetime.strptime(d, "%d/%m/%Y %H:%M:%S").timetuple())

    def ToTimestamp(self, dtiso):
        return time.mktime(datetime.datetime.strptime(dtiso, "%d/%m/%Y %H:%M:%S").timetuple())

    def DtIsoFormat(self):
        return datetime.datetime.now().isoformat()

    def NewQr(self,text, placa):
        img = qrcode.make(text)
        img.save("QR/"+placa.upper()+".jpg")
        img.show()

   



    def ToDecimal(self, valor):
        decimal.Decimal(valor)

import boto3
from botocore.exceptions import ClientError
from boto3.dynamodb.conditions import Key, Attr

import decimal

from toll import Toll

from utils import Utils
uts = Utils()

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('toll')

class DBToll:

    def Create(self, obj):
        table.put_item(Item=obj.ToJson())

    def ReadObj(self, placa):
        response = table.get_item(Key={'placa': placa})
        return Toll.ToObj(response['Item'])

    def ReadJson(self, placa):
        response = table.get_item(Key={'placa': placa})
        return Toll.ToObj(response['Item']).ToJson()

    def ReadAll(self, placa):
        response = table.scan()
        return response["Items"]

    def ReadHistory(self, placa):
        response = table.query(
            ProjectionExpression="#pl, historico",
            ExpressionAttributeNames={"#pl": "placa"},
            KeyConditionExpression=Key('placa').eq(placa)
        )
        return response

    def Update(self, placa):
        response = table.get_item(Key={'placa': placa})
        Toll.ToObj(response['Item']).ToJson()
        table.update_item(Key={'placa': placa},
                          UpdateExpression="SET #attrName = list_append(:attrValue, #attrName)",
                          ExpressionAttributeNames={"#attrName": "historico"},
                          ExpressionAttributeValues={
            ":attrValue": [{"dia": dia, "local": local, }]}
        )

    def UpdateHistory(self, placa, valor, local):
        try:
            response = table.update_item(Key={'placa': placa},
                                         UpdateExpression="SET #attrName = list_append(:attrValue, #attrName)",
                                         ExpressionAttributeNames={
                "#attrName": "historico"},
                ExpressionAttributeValues={
                ":attrValue": [{u'data': uts.codificar(uts.dataHoraAgora()), u'local': uts.codificar(local), u'valor': decimal.Decimal(valor)}]}
            )
        except ClientError as e:
            if e.response['Error']['Code'] == 'ValidationException':
                response = table.update_item(
                    Key={"placa": placa},
                    UpdateExpression="set #attrName = :attrValue",
                    ExpressionAttributeNames={"#attrName": "historico"},
                    ExpressionAttributeValues={
                        ':attrValue': [{
                            u'data': uts.codificar(uts.dataHoraAgora()),
                            u'local': local,
                            u'valor': decimal.Decimal(valor)
                        }]
                    },
                    ReturnValues="UPDATED_NEW"
                )
            else:
                raise

    def UpdateField(self, placa, field, value):
        table.update_item(Key={
            'placa': placa
        },
            UpdateExpression='SET ' + field + '= :value1',
            ExpressionAttributeValues={
            ':value1': value
        }
        )

# query = Key('proprietario').eq(u'Jose')
# view = "#pl, cor, #dt"
# ean = {"#pl": "placa", "#dt": "historico"}

    def VerifyQuery(self, query, view, ean):
        response = table.scan(
            FilterExpression=query,
            ProjectionExpression=view,
            ExpressionAttributeNames=ean
        )

    def Query(self, query, view, ean):
        response = table.query(
            ProjectionExpression=view,
            ExpressionAttributeNames=ean,
            KeyConditionExpression=Key('placa').eq('ABC1114')
        )

    def Delete(self, placa):
        table.delete_item(Key={'placa': placa})

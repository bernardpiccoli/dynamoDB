import boto3
from botocore.exceptions import ClientError
from boto3.dynamodb.conditions import Key, Attr

import decimal

from park import Park

from utils import Utils
uts = Utils()

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('park')

class DBPark:

    def Create(self, obj):
        table.put_item(Item=obj.ToJson())

    def ReadObj(self, placa):
        response = table.get_item(Key={'placa': placa})
        return Park.ToObj(response['Item'])

    def ReadJson(self, placa):
        response = table.get_item(Key={'placa': placa})
        return Park.ToObj(response['Item']).ToJson()

    def ReadAll(self, placa):
        response = table.scan()
        return response["Items"]
        
    def Update(self, placa):
        response = table.get_item(Key={'placa': placa})
        Park.ToObj(response['Item']).ToJson()
        table.update_item(Key={'placa': placa},
                          UpdateExpression="SET #attrName = list_append(:attrValue, #attrName)",
                          ExpressionAttributeNames={"#attrName": "historico"},
                          ExpressionAttributeValues={
            ":attrValue": [{"dia": "dia", "local": "local", }]}
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

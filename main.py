from botocore.exceptions import ClientError
import boto3
from boto3.dynamodb.conditions import Key, Attr
import random

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('gate')


from utils import Utils
uts = Utils()

from servicePark import ServicePark
s = ServicePark()

from park import Park

p = Park("ABC1114")

from dbPark import DBPark
db = DBPark()

# db.Create(p)

s.Sair("ABC1114")

# import datetime
# import time
# utcnow = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
# print(utcnow)

# novo = time.mktime(datetime.datetime.strptime(utcnow, "%Y-%m-%d %H:%M:%S").timetuple())
# print(novo)

# response = table.scan()

# print(response["Items"])

# from dbToll import DBToll
# db = DBToll()

# from toll import Toll
# from utils import Utils
# uts = Utils()

# t = Toll("Mauro","VW","GOL","vermelho","A")
# t.placa = "ABC" + str(random.randint(1000, 9999))

# db.UPDATE_HISTORY("ABC1114",10,"china")

# query = Key('proprietario').eq(u'Jose')
# view = "#pl, cor, #dt"
# ean = { "#pl": "placa", "#dt": "historico"}

# response = table.scan(
#     FilterExpression=query,
#     ProjectionExpression=view,
#     ExpressionAttributeNames=ean
# )

# response = table.query(
#     ProjectionExpression=view,
#     ExpressionAttributeNames=ean,
#     KeyConditionExpression=Key('placa').eq('ABC1114')
# )

# print (response["Items"])

# i = 1
# while i < 6:
#   db.CREATE(t)
#   t.placa = "ABC" + str(random.randint(1000, 9999))
#   i += 1

# tb = db.READ_JSON("POI0983")
# tb.historico = [{"abc":"abc"}]
# print(tb)

# from serviceToll import serviceToll
# a= serviceToll()
# a.ADDPASSAGEM("POI0993")


# table = dynamodb.Table('gate')
# try:
#     # Adding new nested attributes `rating` and `plot`
#     # if the top field `info` already exists and is a map
#     response = table.update_item(Key={'placa': "POI0987"},
#                                  UpdateExpression="SET #attrName = list_append(:attrValue, #attrName)",
#                                  ExpressionAttributeNames={
#                                      "#attrName": "historico"},
#                                  ExpressionAttributeValues={
#         ":attrValue": [{"dia": "dia", "local": "local"}]}
#     )
# except ClientError as e:
#     if e.response['Error']['Code'] == 'ValidationException':
#         # Creating new top level attribute `info` (with nested props)
#         # if the previous query failed
#         response = table.update_item(
#             Key={
#                 "placa": "POI0987",
#             },
#             UpdateExpression="set #attrName = :attrValue",
#             ExpressionAttributeNames={
#                 "#attrName": "historico"
#             },
#             ExpressionAttributeValues={
#                 ':attrValue': [{
#                     'dia': "d",
#                     'local': "E."
#                 }]
#             },
#             ReturnValues="UPDATED_NEW"
#         )
#     else:
#         raise

# response = db.UPDATED("POI0983")
# print(response)

# a = db.get_table_metadata("")

# print(a)

# table = dynamodb.create_table(
#     TableName = 'gate',
#     KeySchema = [
#         {
#             'AttributeName': 'placa',
#             'KeyType': 'HASH'
#         }
#     ],
#     AttributeDefinitions = [
#         {
#         'AttributeName': 'placa',
#         'AttributeType': 'S'
#         }
#     ],
#     ProvisionedThroughput = {
#         'ReadCapacityUnits':5,
#         'WriteCapacityUnits':5

#     }
# )


# response = table.query(KeyConditionExpression=Key('placa').eq('ABC1234'))

# # response = table.query(
# #  ProjectionExpression="#yr, title, info.genres, info.actors[0]",
# #  ExpressionAttributeNames={ "#yr": "year" },
# #  # Expression Attribute Names for Projection Expression only.
# #  KeyConditionExpression=Key('year').eq(1992) & Key('title').between('A', 'L')
# # )
# table = get_dynamodb_resource().Table("table_name")


# dia = "11"
# local = "caxias"
# result = table.update_item(
#     Key={
#         'placa': "ABC1234"
#     },
#     UpdateExpression = "SET #attrName = list_append(:attrValue, #attrName)",
#     ExpressionAttributeNames = { "#attrName" : "passagens"},
#     ExpressionAttributeValues = { ":attrValue" : [{"dia":dia,"local": local}] }
# )

# # if result['ResponseMetadata']['HTTPStatusCode'] == 200 and 'Attributes' in result:
# #     return result['Attributes']['some_attr']
# print(result['ResponseMetadata']['HTTPStatusCode'])


# print(table.creation_date_time)

# table.put_item(
#     Item={
#         'placa':'ABC1234',
#         'bernard':'picci',
#         'passagens': [
#             {'nome':'abc'},
#             {'nome':'cde'}
#         ]
#     }
# )


# response = table.get_item(
#     Key= { 'placa':'ABC1234' }
# )

# item = response['Item']
# print(item)

# table.update_item(
#     Key={
#         'placa': "ABC1234"
#     },
#     UpdateExpression =  'SET passagens = :value1',
#     ExpressionAttributeValues =
#     {
#         ':value1': '25'
#     }
# )

# table.delete_item(
#     Key={
#         'placa': "ABC1234"
#     }
# )
# table.meta.client.get_waiter('table_exists').wait(TableName='newTable')

# print(table.item_count)

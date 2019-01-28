import boto3
from boto3.dynamodb.conditions import Key, Attr

# Get the service resource.
def get_db():
    global dynamodb
    dynamodb = boto3.resource('dynamodb', region_name='us-west-2', endpoint_url="http://localhost:8000")
    return dynamodb


def get_table():
    global dynamodb
    global table
    if table is None:
        get_db()
    table = dynamodb.Table('Devices_data')
    return table


def create_feeds_table():
    # Get the service resource.
    dynamodb = boto3.resource('dynamodb', region_name='us-west-2', endpoint_url="http://localhost:8000")

    # Create the DynamoDB table.
    table = dynamodb.create_table(
        TableName='Devices_data',
        KeySchema=[
            {
                'AttributeName': 'Device_id',
                'KeyType': 'HASH'
            },
            {
                #valor deve seguir <created_at><count> onde <created_at> é o momento de criacao e <count> um valor de 3 digitos 
                # é recebido do cliente e <created_at> gerado pelo servidor no momento que recebe o request
                'AttributeName': 'CreatedAt_count',
                'KeyType': 'RANGE'
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'Device_id',
                'AttributeType': 'S'
            },
            {
                'AttributeName': 'CreatedAt_count',
                'AttributeType': 'N'
            },

        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 5,
            'WriteCapacityUnits': 5
        }
    )

    # Wait until the table exists.
    table.meta.client.get_waiter('table_exists').wait(TableName='Devices_data')

    # Print out some data about the table.
    print(table.item_count)
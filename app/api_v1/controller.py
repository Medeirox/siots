import boto3
from .models import Device

dynamodb = None
table = None

# Get the service resource.
def get_db():
    global dynamodb
    dynamodb = boto3.resource('dynamodb', region_name='us-west-2', endpoint_url="http://localhost:8000")
    return dynamodb


def insert(item):
    pass


def delete(item):
    pass


def update(item):
    pass


# Create the DynamoDB table.
def create_devices_table():
    global table
    table = dynamodb.create_table(
        TableName='Devices',
        KeySchema=[
            {
                'AttributeName': 'Device_id',
                'KeyType': 'HASH'
            },
            {
                #CreatedAt must have 3 numbers appended to it`s end representing a counter of the received
                # data at the same request. The time is represented in LINUX format [time.time()]
                'AttributeName': 'CreatedAt_Count',
                'KeyType': 'RANGE'
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'Device_id',
                'AttributeType': 'S'
            },
            {
                'AttributeName': 'CreatedAt_Count',
                'AttributeType': 'N'
            },

        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 5,
            'WriteCapacityUnits': 5
        }
    )
    
    # Wait until the table exists.
    table.meta.client.get_waiter('table_exists').wait(TableName='Devices')
    
    # Print out some data about the table.
    print(table.item_count)
    
    return table

import boto3
from boto3.dynamodb.conditions import Key, Attr
from faker import Faker
from .models import Device_data

dynamodb = None
table = None

fake = Faker()

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


def insert_device_data(item):
    itm = {}
    itm['Device_id'] = item.id
    itm['CreatedAt_Count'] = ( (item.created_at*1000) + item.count )
    itm['Data'] = item.data
    
    return table.put_item(
        Item=itm
    )


def query_device_data_by_id(device_id=None, max_items=1000, start_date=0, end_date=9999999999):
    if device_id is None:
        return table.query(
            KeyConditionExpression=Key('CreatedAt_Count').between(start_date, end_date),
            Limit=max_items
        )
    else:    
        return table.query(
            KeyConditionExpression=Key('Device_id').eq(device_id) & Key('CreatedAt_Count').between(start_date, end_date),
            Limit=max_items
        )


def create_dummy_data():
    global table
    for _ in range(10):
        itm = {}
        itm['Device_id'] = fake.name()
        for __ in range(10):
            j = Device_data(id=itm['Device_id'],created_at=fake.pyint(),data={'email':fake.free_email()},count=fake.pyint())
            print(insert_device_data(j))


def delete_device_data(item):
    itm = {}
    if hasattr(item, 'id'):
        itm['Device_id'] = item.id
    else:
        itm['Device_id'] = item['Device_id']
    
    if hasattr(item, 'created_at'):
        itm['CreatedAt_Count'] = ((item.created_at*1000) + item.count) or item['CreatedAt_Count']
    else:
        itm['CreatedAt_Count'] = item['CreatedAt_Count']
    
    return table.delete_item(Key=itm)


def update_device_data(item):
    pass


def get_all_items():
    return table.scan()


# Create the DynamoDB table.
def create_devices_table():
    global table
    table = dynamodb.create_table(
        TableName='Devices_data',
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
    table.meta.client.get_waiter('table_exists').wait(TableName='Devices_data')
    
    # Print out some data about the table.
    # print(table.item_count)
    
    return table

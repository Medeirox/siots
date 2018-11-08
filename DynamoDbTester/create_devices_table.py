import boto3

# Get the service resource.
dynamodb = boto3.resource('dynamodb', region_name='us-west-2', endpoint_url="http://localhost:8000")

# Create the DynamoDB table.
table = dynamodb.create_table(
    TableName='Devices',
    KeySchema=[
        {
            'AttributeName': 'Device_id',
            'KeyType': 'HASH'
        },
        {
            #valor deve seguir <timestamp>_<created_at> onde <timestamp> 
            # é recebido do cliente e <created_at> gerado pelo servidor no momento que recebe o request
            'AttributeName': 'Timestamp_CreatedAt',
            'KeyType': 'RANGE'
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'Device_id',
            'AttributeType': 'S'
        },
        {
            'AttributeName': 'Timestamp_CreatedAt',
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
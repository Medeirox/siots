
def create_users_table():
    
    tablename = 'Users'
    hash_key_name = 'username'
    hash_key_type = 'email'
    range_key_name = 'S'
    range_key_type = 'S'

    # Create the DynamoDB table.
    table = dynamodb.create_table(
        TableName=tablename,
        KeySchema=[
            {
                'AttributeName': hash_key_name,
                'KeyType': 'HASH'
            },
            {
                'AttributeName': range_key_name,
                'KeyType': 'RANGE'
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': hash_key_name,
                'AttributeType': hash_key_type
            },
            {
                'AttributeName': range_key_name,
                'AttributeType': range_key_type
            },

        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 5,
            'WriteCapacityUnits': 5
        }
        LocalSecondaryIndexes = Local_Secondary_Indexes
    )

    # Wait until the table exists.
    table.meta.client.get_waiter('table_exists').wait(TableName=tablename)

    # Print out some data about the table.
    print(table.item_count)


def create_devices_table():
    
    tablename = 'Devices'
    hash_key_name = 'id'
    hash_key_type = 'type'
    range_key_name = 'S'
    range_key_type = 'S'

    # Create the DynamoDB table.
    table = dynamodb.create_table(
        TableName=tablename,
        KeySchema=[
            {
                'AttributeName': hash_key_name,
                'KeyType': 'HASH'
            },
            {
                'AttributeName': range_key_name,
                'KeyType': 'RANGE'
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': hash_key_name,
                'AttributeType': hash_key_type
            },
            {
                'AttributeName': range_key_name,
                'AttributeType': range_key_type
            },

        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 5,
            'WriteCapacityUnits': 5
        }
        LocalSecondaryIndexes = Local_Secondary_Indexes
    )

    # Wait until the table exists.
    table.meta.client.get_waiter('table_exists').wait(TableName=tablename)

    # Print out some data about the table.
    print(table.item_count)


def create_feeds_table():
    
    tablename = 'Feeds'
    hash_key_name = 'device_id'
    hash_key_type = 'timestamp'
    range_key_name = 'S'
    range_key_type = 'S'

    # Create the DynamoDB table.
    table = dynamodb.create_table(
        TableName=tablename,
        KeySchema=[
            {
                'AttributeName': hash_key_name,
                'KeyType': 'HASH'
            },
            {
                'AttributeName': range_key_name,
                'KeyType': 'RANGE'
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': hash_key_name,
                'AttributeType': hash_key_type
            },
            {
                'AttributeName': range_key_name,
                'AttributeType': range_key_type
            },

        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 5,
            'WriteCapacityUnits': 5
        }
        LocalSecondaryIndexes = Local_Secondary_Indexes
    )

    # Wait until the table exists.
    table.meta.client.get_waiter('table_exists').wait(TableName=tablename)

    # Print out some data about the table.
    print(table.item_count)


def create_roles_table():
    
    tablename = 'Roles'
    hash_key_name = 'role'
    hash_key_type = 'S'
    range_key_name = 'group'
    range_key_type = 'S'
    secondary_key_name = 'username'
    secondary_key_type = 'S'
    secondary_index_name = 'role_username_index'
    projection = { 
        'ProjectionType': 'KEYS_ONLY'
    }
    

    # Create the DynamoDB table.
    table = dynamodb.create_table(
        TableName=tablename,
        KeySchema=[
            {
                'AttributeName': hash_key_name,
                'KeyType': 'HASH'
            },
            {
                'AttributeName': range_key_name,
                'KeyType': 'RANGE'
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': hash_key_name,
                'AttributeType': hash_key_type
            },
            {
                'AttributeName': range_key_name,
                'AttributeType': range_key_type
            },
            {
                'AttributeName': secondary_key_name,
                'AttributeType': secondary_key_type
            },
        ],
        LocalSecondaryIndexes=[
            {
                'IndexName': secondary_index_name,
                'KeySchema': [
                    {
                        'AttributeName': hash_key_name,
                        'KeyType': 'HASH'
                    },
                    {
                        'AttributeName': secondary_key_name,
                        'KeyType': 'RANGE'
                    }
            ],
            'Projection': projection
            }
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 5,
            'WriteCapacityUnits': 5
        }
    )

    # Wait until the table exists.
    table.meta.client.get_waiter('table_exists').wait(TableName=tablename)

    # Print out some data about the table.
    print(table.item_count)


def create_groups_table():
    
    tablename = 'Groups'
    hash_key_name = 'group'
    hash_key_type = 'S'
    range_key_name = 'member_id'
    range_key_type = 'S'
    secondary_key_name = 'member_type'
    secondary_key_type = 'S'
    secondary_index_name = 'group_member_type_index'
    projection = { 
        'ProjectionType': 'KEYS_ONLY'
    }
    

    # Create the DynamoDB table.
    table = dynamodb.create_table(
        TableName=tablename,
        KeySchema=[
            {
                'AttributeName': hash_key_name,
                'KeyType': 'HASH'
            },
            {
                'AttributeName': range_key_name,
                'KeyType': 'RANGE'
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': hash_key_name,
                'AttributeType': hash_key_type
            },
            {
                'AttributeName': range_key_name,
                'AttributeType': range_key_type
            },
            {
                'AttributeName': secondary_key_name,
                'AttributeType': secondary_key_type
            },
        ],
        LocalSecondaryIndexes=[
            {
                'IndexName': secondary_index_name,
                'KeySchema': [
                    {
                        'AttributeName': hash_key_name,
                        'KeyType': 'HASH'
                    },
                    {
                        'AttributeName': secondary_key_name,
                        'KeyType': 'RANGE'
                    }
            ],
            'Projection': projection
            }
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 5,
            'WriteCapacityUnits': 5
        }
    )

    # Wait until the table exists.
    table.meta.client.get_waiter('table_exists').wait(TableName=tablename)

    # Print out some data about the table.
    print(table.item_count)
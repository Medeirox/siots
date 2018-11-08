from flask import Flask
import boto3

# Get the service resource.
dynamodb = boto3.resource('dynamodb', region_name='us-west-2', endpoint_url="http://localhost:8000")

app = Flask(__name__)
# app.config['DYNAMO_TABLES'] = [
#     {
#          'TableName':'users',
#          'KeySchema':[dict(AttributeName='username', KeyType='HASH')],
#          'AttributeDefinitions':[dict(AttributeName='username', AttributeType='S')],
#          'ProvisionedThroughput':dict(ReadCapacityUnits=5, WriteCapacityUnits=5)
#     }, {
#          'TableName':'groups',
#          'KeySchema':[dict(AttributeName='name', KeyType='HASH')],
#          'AttributeDefinitions':[dict(AttributeName='name', AttributeType='S')],
#          'ProvisionedThroughput':dict(ReadCapacityUnits=5, WriteCapacityUnits=5)
#     }
# ]

app.config['DYNAMO_ENABLE_LOCAL'] = True
app.config['DYNAMO_LOCAL_HOST'] = 'localhost'
app.config['DYNAMO_LOCAL_PORT'] = 8000

# dynamodb = Dynamo(app)

# with app.app_context():
#     dynamo.create_all()

@app.route('/')
def home():
    return "Hey there!"


@app.route('/create_user/<user>/<first_name>/<last_name>/<email>')
def create_user(user, first_name, last_name, email):
    dynamo.tables['users'].put_item(Item={
        'username': user,
        'first_name': first_name,
        'last_name': last_name,
        'email': email,
    })
    return "user {0} created".format(user)

@app.route('/get_tables')
def get_tables():
    a = ''
    for table_name, table in dynamo.tables.items():
        a += table_name + ','
    return a

@app.route('/get_users')
def get_users():
    u = ''
    for user_name, user in dynamo.tables['users'].scan():
        u += user_name
    
    return u

if __name__ == '__main__':
    app.run(debug=True)
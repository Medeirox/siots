from . import dynamodb
from . import create_tables

#TODO: REMODEL THE CLASS TO USE PYNAMODB PACKAGE

def create_all_tables():
    #Users
    create_users_table()
    #Devices table
    create_devices_table()
    #Feeds
    create_feeds_table()
    #Roles
    create_roles_table()
    #Groups
    create_groups_table()



class User:
    __table_name__ = 'Users'

    def __init__(self):
        self._username = ''  #hash key
        self._first_name = ''
        self._last_name = ''
        self._email = ''
        self._enabled = False
        self._created_at = 0
        self._last_seen = 0
        self._password_hash = ''
        self._email_confirmed = False
        self._roles = {}
        self._groups = {}


    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, value):
        self._username = value


    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        self._first_name = value


    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        self._last_name = value


    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        self._email=value


    @property
    def enabled(self):
        return self._enabled

    @enabled.setter
    def enabled(self, value):
        self._enabled = value


    @property
    def created_at(self):
        return self._created_at

    @created_at.setter
    def created_at(self, value):
        self._created_at = value


    @property
    def last_seen(self):
        return self._last_seen

    @last_seen.setter
    def last_seen(self, value):
        self._last_seen = value


    @property
    def password_hash(self):
        return self._password_hash

    @password_hash.setter
    def password_hash(self, value):
        self._password_hash = value


    @property
    def email_confirmed(self):
        return self._email_confirmed

    @email_confirmed.setter
    def email_confirmed(self, value):
        self._email_confirmed = value


    @property
    def roles(self):
        return self._roles

    @roles.setter
    def roles(self, value):
        self._roles = value


    @property
    def groups(self):
        return self._groups

    @groups.setter
    def groups(self, value):
        self._groups = value

    
    def get_user(username):
        response = dynamodb.Table(__table_name__).get_item(
            Key={
                'username' : username
            }
        )


class Device:
    def __init__(self):
        self.__table_name__ = 'Devices'
        self._id = ''
        self._type = ''
        self._write_key = ''
        self._activation_key = ''
        self._tag = ''
        self._created_at = 0
        self._last_seen = 0
        self._status = ''
        self._enabled = False
        self._config = {}


    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value


    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value


    @property
    def write_key(self):
        return self._write_key

    @write_key.setter
    def write_key(self, value):
        self._write_key = value


    @property
    def activation_key(self):
        return self._activation_key

    @activation_key.setter
    def activation_key(self, value):
        self._activation_key = value


    @property
    def tag(self):
        return self._tag

    @tag.setter
    def tag(self, value):
        self._tag = value


    @property
    def created_at(self):
        return self._created_at

    @created_at.setter
    def created_at(self, value):
        self._created_at = value


    @property
    def last_seen(self):
        return self._last_seen

    @last_seen.setter
    def last_seen(self, value):
        self._last_seen = value


    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


    @property
    def enabled(self):
        return self._enabled

    @enabled.setter
    def enabled(self, value):
        self._enabled = value


    @property
    def config(self):
        return self._config

    @config.setter
    def config(self, value):
        self._config = value


class Role:
    def __init__(self):
        self.__table_name__ = 'Roles'
        self.__hash_key__ = self._role
        self.__hash_key_type__ = 'S'
        self.__range_key__ = self._group
        self.__range_key_type__ = 'S'
        self.__secondary_range_key__ = self._group
        self.__secondary_range_key_type__ = 'S'
        
        self._role = ''
        self._username = ''
        self._group = ''
        self._permissions = []

    @property
    def role(self):
        return self._role

    @role.setter
    def role(self, value):
        self._role = value


    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, value):
        self._username = value


    @property
    def group(self):
        return self._group

    @group.setter
    def group(self, value):
        self._group = value


    @property
    def permissions(self):
        return self._permissions

    @permissions.setter
    def permissions(self, value):
        self._permissions = value


class Feed:
    def __init__(self):
        self.__table_name__ = 'Feeds'
        self._device_id = '' #Hash key
        self._timestamp = 0 #range key
        self._created_at = 0 
        self._data = {}

    @property
    def device_id(self):
        return self._device_id

    @device_id.setter
    def device_id(self, value):
        self._device_id = value


    @property
    def timestamp(self):
        return self._timestamp

    @timestamp.setter
    def timestamp(self, value):
        self._timestamp = value


    @property
    def created_at(self):
        return self._created_at

    @created_at.setter
    def created_at(self, value):
        self._created_at = value


    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = value


class Group:
    def __init__(self):
        self.__table_name__ = 'Groups'
        self._name = ''
        self._member_id = ''
        self._member_type = ''

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value


    @property
    def member_id(self):
        return self._member_id

    @member_id.setter
    def member_id(self, value):
        self._member_id = value


    @property
    def users(self):
        return self._users

    @users.setter
    def users(self, value):
        self._users = value


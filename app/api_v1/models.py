# remover esta classe
class Device_data:
    def __init__(self, id, created_at, data={}, count=0):
        check_id = isinstance(id, str)
        check_created_at = isinstance(created_at, int)
        check_count = isinstance(count, int)
        check_data = isinstance(data, dict)
        
        self.id = id if check_id else False
        self.created_at = created_at if check_created_at else False
        self.count = count if check_count else False
        self.data = data if check_data else False
        
        if( not (check_id and check_created_at and check_count and check_data) ):
            raise TypeError('Wrong data type passed for: {a} {b} {c} {d}'.format(
                a = '' if check_id else 'id,',
                b = '' if check_created_at else 'created_at,',
                c = '' if check_count else 'count,',
                d = '' if check_data else 'data'
            ))
        else:
            return
    
    def __repr__(self):
        return '{{"id":"{a}", "created_at":{b}, "count":{c:03d}, "data":{d}}}'.format(a=self.id, b=self.created_at, c=self.count, d=self.data)


class User:
    def __init__(self):
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
        return self.email

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
        return _last_seen

    @last_seen.setter
    def last_seen(self, value):
        _last_seen = value


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


class Device:
    def __init__(self):
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
        self._name = ''
        self._group = ''
        self._permissions = ['read']

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value


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
        self._id = '' #Hash key
        self._timestamp = 0 #range key
        self._created_at = 0 
        self._data = {}

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value


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

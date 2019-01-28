from pynamodb.models import Model
from pynamodb.attributes import UnicodeAttribute, NumberAttribute
from pynamodb.indexes import GlobalSecondaryIndex, AllProjection


_HOST_ADDRESS = 'http://localhost:8000'
_REGION = 'us-west-1'

class Feed(Model):
    class Meta:
        table_name = 'Feeds'
        # Specifies the region
        region = _REGION
        # Optional: Specify the hostname only if it needs to be changed from the default AWS setting
        host = _HOST_ADDRESS
        # Specifies the write capacity
        write_capacity_units = 10
        # Specifies the read capacity
        read_capacity_units = 10
    device_id = UnicodeAttribute(hash_key=True)
    timestamp = NumberAttribute(range_key=True)
    created_at = NumberAttribute()
    data = UnicodeAttribute(null=True)


class DeviceTypeIndex(GlobalSecondaryIndex):
    """
    This class represents a local secondary index
    """
    class Meta:
        index_name = 'device-type-index'
        # Specifies the write capacity
        write_capacity_units = 10
        # Specifies the read capacity
        read_capacity_units = 10
        # All attributes are projected
        projection = AllProjection()
    id = UnicodeAttribute(hash_key=True)
    device_type = UnicodeAttribute(range_key=True)


class Device(Model):
    class Meta:
        table_name = 'Devices'
        # Specifies the region
        region = _REGION
        # Optional: Specify the hostname only if it needs to be changed from the default AWS setting
        host = _HOST_ADDRESS
        # Specifies the write capacity
        write_capacity_units = 10
        # Specifies the read capacity
        read_capacity_units = 10
    id = UnicodeAttribute(hash_key=True)
    device_type_index = DeviceTypeIndex()
    device_type = UnicodeAttribute()
    write_key = UnicodeAttribute(null=True)
    activation_key = UnicodeAttribute(null=True)
    tag = UnicodeAttribute(null=True)
    created_at = NumberAttribute(null=True)
    last_seen = NumberAttribute(null=True)
    status = UnicodeAttribute(null=True)
    enabled = NumberAttribute(null=True)
    config = UnicodeAttribute(null=True)


# Create a table for the base model passed
def create_table(model_class):
    if not model_class.exists():
        model_class.create_table(read_capacity_units=1, write_capacity_units=1, wait=True)
        return True
    else:
        return False


def delete_table(model_class):
    if model_class.exists():
        model_class.delete_table()
        return True
    else:
        return False



import time

# response = table.put_item(
#    Item={
#         'DeviceId': 'ABCDEF',
#         'Timestamp_CreatedAt': round_float_to_decimal(time.time())
#     }
# )

def round_float_to_decimal(float_value):
    """
    Convert a floating point value to a decimal that DynamoDB can store,
    and allow rounding.
    """

    # Perform the conversion using a copy of the decimal context that boto3
    # uses. Doing so causes this routine to preserve as much precision as
    # boto3 will allow.
    with decimal.localcontext(boto3.dynamodb.types.DYNAMODB_CONTEXT) as \
         decimalcontext:

        # Allow rounding.
        decimalcontext.traps[decimal.Inexact] = 0
        decimalcontext.traps[decimal.Rounded] = 0
        decimal_value = decimalcontext.create_decimal_from_float(float_value)
        g_logger.debug("float: {}, decimal: {}".format(float_value,
                                                       decimal_value))

        return decimal_value



Item={
        'DeviceId': 'ABCDEF',
        'Timestamp_CreatedAt': round_float_to_decimal(time.time())
}
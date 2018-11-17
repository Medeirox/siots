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

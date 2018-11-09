class Device:
    def __init__(self, id, created_at, data, count=0):
        self.id = id
        self.created_at = created_at
        self.count = count
        self.data = data
    
    def __repr__(self):
        return '{{"id":"{a}", created_at:{b}, count:{c:03d}, data:{d}}}'.format(a=self.id, b=self.created_at, c=self.count, d=self.data)


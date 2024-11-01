class Holiday(object):
    date = ""
    name = ""
    
    def __init__(self, date, name):
        self.date = date
        self.name = name
    
    def __str__(self):
        s = ""
        s += str(self.name) + ", "
        s += str(self.date)
        return s

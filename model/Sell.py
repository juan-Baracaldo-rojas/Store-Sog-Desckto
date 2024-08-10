class Sell:
    def __init__(self, sell_date=None, sell_total=None):
        self._sell_date = sell_date
        self._sell_total = sell_total
    
    @property
    def sell_date(self):
        return self._sell_date
    
    @sell_date.setter
    def sell_date(self, value):
        self._sell_date = value
    
    @property
    def sell_total(self):
        return self._sell_total
    
    @sell_total.setter
    def sell_total(self, value):
        self._sell_total = value
    
    def __str__(self):
        return f"\nsell_date: {self.sell_date}, sell_total: {self.sell_total}"

class Product:
    def __init__(self, name=None, category=None, marca=None, price=None,stock_actual=None, stock_sell=None, unid=None, size=None, color=None, expiration_date=None, material=None):
        self._name = name
        self._category = category
        self._marca = marca
        self._price = price
        self._stock_actual = stock_actual
        self._stock_sell = stock_sell
        self._unid = unid
        self._size = size
        self._color = color
        self._expiration_date = expiration_date
        self._material = material
    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        self._category = value

    @property
    def marca(self):
        return self._marca

    @marca.setter
    def marca(self, value):
        self._marca = value
    
    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value

    @property
    def stock_actual(self):
        return self._stock_actual

    @stock_actual.setter
    def stock_actual(self, value):
        self._stock_actual = value

    @property
    def stock_sell(self):
        return self._stock_sell

    @stock_sell.setter
    def stock_sell(self, value):
        self._stock_sell = value

    @property
    def unid(self):
        return self._unid

    @unid.setter
    def unid(self, value):
        self._unid = value

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        self._size = value

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value):
        self._color = value

    @property
    def expiration_date(self):
        return self._expiration_date

    @expiration_date.setter
    def expiration_date(self, value):
        self._expiration_date = value

    @property
    def material(self):
        return self._material

    @material.setter
    def material(self, value):
        self._material = value

    def __str__(self):
        return (f'Name: {self.name}, Category: {self.category}, Marca: {self.marca}, '
                f'Stock Actual: {self.stock_actual}, Stock Vendido: {self.stock_sell}, '
                f'Unidad: {self.unid}, Size: {self.size}, Color: {self.color}, '
                f'Expiration Date: {self.expiration_date}, Material: {self.material}')

class SellDetail:
    def __init__(self, sell_ID=None, product_ID=None, cant=None, unid_price=None):
        self._sell_ID = sell_ID
        self._product_ID = product_ID
        self._cant = cant
        self._unid_price = unid_price
        self._subTotal = self._calculate_subtotal()

    @property
    def sell_ID(self):
        return self._sell_ID

    @sell_ID.setter
    def sell_ID(self, value):
        self._sell_ID = value

    @property
    def product_ID(self):
        return self._product_ID

    @product_ID.setter
    def product_ID(self, value):
        self._product_ID = value

    @property
    def cant(self):
        return self._cant

    @cant.setter
    def cant(self, value):
        self._cant = value
        self._subTotal = self._calculate_subtotal()

    @property
    def unid_price(self):
        return self._unid_price

    @unid_price.setter
    def unid_price(self, value):
        self._unid_price = value
        self._subTotal = self._calculate_subtotal()

    @property
    def subTotal(self):
        return self._subTotal

    def _calculate_subtotal(self):
        if self._cant is not None and self._unid_price is not None:
            return self._cant * self._unid_price
        return None

    def __str__(self):
        return (f"sell_ID: {self.sell_ID}, product_ID: {self.product_ID}, "
                f"cant: {self.cant}, unid_price: {self.unid_price}, subTotal: {self.subTotal}")

class Local:
    def __init__(self, name=None, type_1=None, type_2=None, type_3=None):
        self._name = name
        self._type_1 = type_1
        self._type_2 = type_2
        self._type_3 = type_3

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def type_1(self):
        return self._type_1

    @type_1.setter
    def type_1(self, type_1):
        self._type_1 = type_1

    @property
    def type_2(self):
        return self._type_2

    @type_2.setter
    def type_2(self, type_2):
        self._type_2 = type_2

    @property
    def type_3(self):
        return self._type_3

    @type_3.setter
    def type_3(self, type_3):
        self._type_3 = type_3

    def __str__(self):
        return f"name= {self._name}, type_1= {self._type_1}, type_2= {self._type_2}, type_3= {self._type_3}"

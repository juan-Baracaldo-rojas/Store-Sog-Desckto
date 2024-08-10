class Category:
    def __init__(self, name, description):
        self._name = name
        self._description = description
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
    def description(self):
        return self._description
    
    @description.setter
    def description(self, value):
        self._description = value
    
    def __str__(self):
        return f'name: {self.name}, description: {self.description}'

from _typeshed import Self


class Cliente:

    def __init__(self, nome):
        self.__nome = nome
    
    @property
    #denifindo como propriedade, tira a necessidade de chamar o metodo com parenteses
    def nome(self):    
        return self.__nome.title()

    @nome.setter
    def nome(self, nome):
        self.__nome = nome
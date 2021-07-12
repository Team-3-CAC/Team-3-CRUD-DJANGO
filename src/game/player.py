

class Player:
  
    def __init__(self, nombre, id) -> None:
        """
        Contructor.
        IMPORTANT: Todo metodo lleva como primer
        parametro self
        """
        self.__nombre = nombre
        self.__id = id
        self.__score = 0

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        # aca podemos chequear y controlar que ID sea un parametro
        # valido para nuestro objeto
        self.__id = id
    
    def input(self):
        """
        Es el input del player en mi Juego
        """
        pass
    
    def getNombre(self) -> str:
        return self.__nombre

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, value):
        self.__score = value

    def __str__(self) -> str:
        """
        Convierto a String my metodo
        """
        return f"Player name:{self.getNombre()}, id:{self.id}, score:{self.score}"
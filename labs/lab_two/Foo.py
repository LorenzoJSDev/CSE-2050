class Foo():
    """This is the Foo Class"""

    def __init__(self, name: str, profession: str) -> None:
        """
        Docstring for __init__
        
        :param self: 
        :param name: Foo name
        :type name: str
        :param profession: Foo profession
        :type profession: str
        """
        self.name = name
        self.profession = profession

    def __repr__(self) -> str:
        """
        Docstring for __repr__
        
        :param self: 
        :return: "Foo(<name>, <profession>)"
        :rtype: str
        """
        return f"Foo({self.name}, {self.profession})"
    
    def speak(self) -> str:
        """
        Docstring for speak
        
        :param self: 
        :return: "<name> says hello!"
        :rtype: str
        """
        return  f"{self.name} says hello!"


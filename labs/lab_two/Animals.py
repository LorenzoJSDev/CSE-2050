class Animal:
   """ Doc string for Animal Class"""

   def __init__(self, name: str, species: str ="animal", sound: str = "hi") -> None:
      """
      Docstring for __init__
      
      :param self: Description
      :param name: Description
      :type name: str
      :param species: Description
      :type species: str
      :param sound: Description
      :type sound: str
      """
      self.name = name
      self.sound = sound
      self.species = species


   def speak(self) -> str:
      """
      Docstring for speak
      
      :param self: Description
      :return: Description
      :rtype: str
      """
      return f"{self.name}, a {self.species}, says {self.sound}!"

   def __repr__(self) -> str:
      """
      Docstring for __repr__
      
      :param self: Description
      :return: Description
      :rtype: str
      """
      return f"Animal({self.name}, {self.species}, {self.sound})"




class Dog(Animal):
   """
   Docstring for Dog
   """
   
   def __init__(self, name, is_good_boy=True) -> None:
      """
      Docstring for __init__
      
      :param self: Description
      :param name: Description
      :param is_good_boy: Description
      """
      super().__init__(name, "dog", "ruff")
      self.is_good_boy = is_good_boy

   
   def __repr__(self) -> str:
      """
      Docstring for __repr__
      
      :param self: Description
      :return: Description
      :rtype: str
      """
      return f"Dog({self.name})"
   


   
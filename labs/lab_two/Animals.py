class Animal:

   def __init__(self, name: str, species: str ="animal", sound: str = "hi") -> None:
      self.name = name
      self.sound = sound
      self.species = species


   def speak(self) -> str:
      return f"{self.name}, a {self.species}, says {self.sound}!"

   def __repr__(self) -> str:
      return f"Animal({self.name}, {self.species}, {self.sound})"


class Dog(Animal):
   
   def __init__(self, name, is_good_boy=True) -> None:
      pass
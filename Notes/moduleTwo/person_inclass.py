class Person:

    def __init__(self,name:str,age:int,address:object) -> None:
        self.name = name
        self.age = age
        self.address = address

    def __str__(self) -> str:
        return f"{self.name} ({self.age}), {self.address}"
    


class Employee(Person):

    def __init__(self, name: str, age: int, address: str, job_title:str, salrary:float) -> None:
        super().__init__(name, age, address)
        self.job_title = job_title
        self.salary = salrary

    def work(self):
        print(f"{self.name} is working")


class Address:
    
    def __init__(self,street:str, city_name:str, zip_code:str):
        self.street = street
        self.city_name = city_name
        self.zip_code = zip_code

    def __str__(self):
        return f"{self.street}, {self.city_name}, {self.zip_code}"
        

# Create addresses
address1 = Address("123 Main St", "Springfield", "12345")
address2 = Address("456 Elm St", "Metropolis", "67890")
# Create a person and an employee
person1 = Person("John Doe", 30, address1)
employee1 = Employee("Jane Smith", 25, address2, "Software Engineer", 75000)
# Display person and employee details
print(person1)
print(employee1)
# Demonstrate working
employee1.work()
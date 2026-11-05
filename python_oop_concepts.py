from abc import ABC, abstractmethod
import datetime

class Vehicle(ABC):
    """
    Abstract Base Class (ABC) demonstrating Abstraction.
    Cannot be instantiated directly.
    """
    
    # Class attribute: Shared among all instances of the class
    total_vehicles = 0
    
    def __init__(self, brand, model, year):
        # Encapsulation: Private attribute (double underscore)
        self.__brand = brand
        
        # Encapsulation: Protected attribute (single underscore convention)
        self._model = model
        
        # Public attribute
        self.year = year
        
        # Incrementing the class attribute
        Vehicle.total_vehicles += 1
        
    @abstractmethod
    def start_engine(self):
        """Abstract method that MUST be implemented by subclasses"""
        pass
        
    # Property (Getter for the private attribute)
    @property
    def brand(self):
        return self.__brand
        
    # Property (Setter with validation for the private attribute)
    @brand.setter
    def brand(self, new_brand):
        if isinstance(new_brand, str) and new_brand.strip():
            self.__brand = new_brand
        else:
            raise ValueError("Brand must be a non-empty string.")

    @classmethod
    def get_total_vehicles(cls):
        """Class method: Operates on the class itself, not instances"""
        return f"Total vehicles registered: {cls.total_vehicles}"
        
    @staticmethod
    def is_vintage(year):
        """Static method: Independent of class or instance state"""
        current_year = datetime.datetime.now().year
        return (current_year - year) > 25

    # Magic / Dunder Method (__str__) for string representation
    def __str__(self):
        return f"{self.year} {self.brand} {self._model}"


class Car(Vehicle):
    """Demonstrating Single Inheritance"""
    
    def __init__(self, brand, model, year, num_doors):
        # Call the parent class's constructor
        super().__init__(brand, model, year)
        self.num_doors = num_doors
        
    # Polymorphism: Method Overriding
    def start_engine(self):
        return f"The {self.brand} {self._model}'s engine roars to life. Vroom!"
        
    # Another Magic Method (__eq__) for object comparison
    def __eq__(self, other):
        if isinstance(other, Car):
            return self.brand == other.brand and self._model == other._model
        return False


class ElectricMixin:
    """Mixin class to demonstrate functionality extension (Multiple Inheritance setup)"""
    def charge_battery(self):
        return "Battery is charging..."


class ElectricCar(Car, ElectricMixin):
    """Demonstrating Multiple Inheritance (inherits from Car and ElectricMixin)"""
    
    def __init__(self, brand, model, year, num_doors, battery_capacity_kwh):
        super().__init__(brand, model, year, num_doors)
        self.battery_capacity_kwh = battery_capacity_kwh
        
    # Polymorphism: Overriding the parent's start_engine method again
    def start_engine(self):
        return f"The {self.brand} {self._model} starts silently. Ready to go!"


def main():
    print("=== Python OOP Concepts Demonstration ===")
    
    # 1. Object Instantiation
    print("\n--- 1. Objects & Inheritance ---")
    gas_car = Car("Ford", "Mustang", 2022, 2)
    ev_car = ElectricCar("Tesla", "Model S", 2024, 4, 100)
    
    print(gas_car) # Triggers __str__
    print(ev_car)
    
    # 2. Polymorphism (Method Overriding)
    print("\n--- 2. Polymorphism ---")
    print(gas_car.start_engine())
    print(ev_car.start_engine())
    
    # 3. Multiple Inheritance
    print("\n--- 3. Multiple Inheritance (Mixins) ---")
    print(ev_car.charge_battery())
    
    # 4. Encapsulation (Getters and Setters)
    print("\n--- 4. Encapsulation ---")
    print(f"Current brand (Getter): {gas_car.brand}")
    gas_car.brand = "Shelby" # Uses the setter
    print(f"Updated brand (Setter): {gas_car.brand}")
    
    # 5. Class Methods
    print("\n--- 5. Class Methods ---")
    print(Vehicle.get_total_vehicles())
    
    # 6. Static Methods
    print("\n--- 6. Static Methods ---")
    year_to_check = 1969
    print(f"Is a {year_to_check} vehicle vintage? {Vehicle.is_vintage(year_to_check)}")
    
    # 7. Operator Overloading (Magic Methods)
    print("\n--- 7. Magic/Dunder Methods (__eq__) ---")
    car2 = Car("Shelby", "Mustang", 2022, 2)
    print(f"Is gas_car the same make/model as car2? {gas_car == car2}")


if __name__ == '__main__':
    main()

import doctest
from dataclasses import dataclass
from enum import Enum

class FuelType(Enum):
    PETROL = 'Petrol'
    DIESEL = 'Diesel'
    ELECTRO = 'Electro'

@dataclass
class HorsePower:
    value: int

    def __post_init__(self) -> None:
        if self.value < 1 or self.value > 600:
            raise ValueError(f'Wrong number of hp: {self.value}')

class Engine:
    """
    Класс, представляющий двигатель автомобиля.
    """

    def __init__(self, horsepower: HorsePower, fuel_type: FuelType) -> None:
        self.horsepower: HorsePower = horsepower
        self.fuel_type: FuelType = fuel_type

    def change_fuel_type(self, new_fuel_type: FuelType) -> FuelType:
        """
        Метод изменяет тип топлива двигателя.
        Вызывает исключение ValueError, если текущий тип топлива - Электричество, или новый тип топлива Электричество.

        :param new_fuel_type: FuelTypes: новый тип топлива
        :raise ValueError: Нельзя изменить тип топлива у Электродвигателя
        :return: FuelTypes: тип топлива, который мы установили

        >>> test_engine = Engine(horsepower=HorsePower(100), fuel_type=FuelType.DIESEL)
        >>> test_engine.change_fuel_type(new_fuel_type=FuelType.PETROL)
        <FuelType.PETROL: 'Petrol'>

        >>> test_engine2 = Engine(horsepower=HorsePower(100), fuel_type=FuelType.ELECTRO)
        >>> test_engine2.change_fuel_type(new_fuel_type=FuelType.PETROL)
        Traceback (most recent call last):
        ...
        ValueError: Нельзя изменить тип топлива у Электродвигателя
        """

        if self.fuel_type == FuelType.ELECTRO or new_fuel_type == FuelType.ELECTRO:
            raise ValueError('Нельзя изменить тип топлива у Электродвигателя')
        self.fuel_type = new_fuel_type
        return new_fuel_type

class BodyType(Enum):
    COUPE = 'Coupe'
    SUV = 'SUV'
    CONVERTIBLE = 'Convertible'
    PICKUP = 'Pickup'
    MPV = 'MVP'
    MINIVAN = 'Minivan'
    SEDAN = 'Sedan'

@dataclass
class Door:
    value: int

    def __post_init__(self) -> None:
        if self.value < 1 or self.value > 8:
            raise ValueError(f'Wrong number of doors: {self.value}')

class CarBody:
    """
    Класс, представляющий корпус автомобиля.
    """

    def __init__(self, body_type: BodyType, doors: Door) -> None:
        self.body_type: BodyType = body_type
        self.doors: Door = doors

class TireType(Enum):
    SUMMER = 'Summer'
    WINTER = 'Winter'
    ALLSEASONED = 'All-Seasoned'

@dataclass
class Diameter:
    value: int

    def __post_init__(self) -> None:
        if self.value < 14 or self.value > 30:
            raise ValueError(f'Wrong diameter: {self.value}')

class Wheel:
    """
    Класс, представляющий колеса автомобиля
    """

    def __init__(self, diameter: Diameter, tires: TireType) -> None:
        self.diameter: Diameter = diameter
        self.tires: TireType = tires

    def change_wheel(self, new_diameter: Diameter, new_tires: TireType):
        """
        Метод изменяет диаметр и тип резины.
        :param new_tires: TireTypes: Новый тип резины
        :param new_diameter: Diameter: Новый диаметр колеса
        :return: Tuple[Diameter, TireTypes]: диаметр колеса и тип резины, который мы установили

        >>> test_wheel = Wheel(diameter=Diameter(16), tires=TireType.SUMMER)
        >>> test_wheel.change_wheel(new_diameter=Diameter(20), new_tires=TireType.WINTER)
        (Diameter(value=20), <TireType.WINTER: 'Winter'>)
        """

        self.diameter = new_diameter
        self.tires = new_tires
        return new_diameter, new_tires

class Car:
    """"
    Класс, представляющий автомобиль
    """

    def __init__(
            self,
            make: str,
            model: str,
            horsepower: HorsePower,
            fuel_type: FuelType,
            body_type: BodyType,
            doors: Door,
            diameter: Diameter,
            tires: TireType,
            wheels: list [Wheel]
            ) -> None:

        self.make = make
        self.model = model
        self.engine = Engine(horsepower, fuel_type)
        self.car_body = CarBody(body_type, doors)
        self.wheels = [Wheel(diameter, tires) for _ in wheels] #Эту строчку получила от gpt, _ здесь как поняла используется для дальнейшего значения wheel

    def display_info(self):
        """"
        Метод, выдающий информацию об автомобиле
        """
        print(f'Car: {self.make}, Model: {self.model}')

    def display_engine_info(self) -> str:
        """"
        Метод, выдающий информацию о двигателе
        """

        return f'Horsepower: {self.engine.horsepower.value} hp, Fuel: {self.engine.fuel_type.value}'

    def display_car_body_info(self) -> str:
        """"
        Метод, выдающий информацию о кузове
        """

        return f'Body_type: {self.car_body.body_type.value}, Door: {self.car_body.doors.value}'

    def display_wheel_info(self) -> str:
        """"
        Метод, выдающий информацию о колесах
        Вызывает исключение ValueError, если колеса разнятся по диаметру или типу резины

        :param: Diameter, Tires
        :raise ValueError: Wheels should have same diameter and tires
        :return: Wheel.Diameter, Wheel.Tires для каждой шины

        >>> test_car1 = Car(
        ... make='BMW',
        ... model='X5',
        ... horsepower=HorsePower(375),
        ... fuel_type=FuelType.DIESEL,
        ... body_type=BodyType.SEDAN,
        ... doors=Door(4),
        ... diameter=Diameter(16),
        ... tires=TireType.SUMMER,
        ... wheels = [Wheel(Diameter(16), TireType.SUMMER),
        ... Wheel(Diameter(16), TireType.SUMMER),
        ... Wheel(Diameter(16), TireType.SUMMER),
        ... Wheel(Diameter(16), TireType.SUMMER)]
        ... )

        >>> test_car1.display_wheel_info()
        'Wheel1 Diameter: 16 inch, Wheel1 Tires: Summer, Wheel2 Diameter: 16 inch, Wheel2 Tires: Summer, Wheel3 Diameter: 16 inch, Wheel3 Tires: Summer, Wheel4 Diameter: 16 inch, Wheel4 Tires: Summer'

        >>> test_car1.wheels[0].change_wheel(new_diameter=Diameter(18), new_tires=TireType.SUMMER)
        >>> test_car1.display_wheel_info()
        Traceback (most recent call last):
        ...
        ValueError: Wheels should have same diameter and tires
        """

        wheel1 = self.wheels[0]
        for wheel in self.wheels:
            if wheel1.diameter != wheel.diameter or wheel1.tires != wheel.tires:
                raise ValueError('Wheels should have same diameter and tires')

        return ', '.join(
        [f'Wheel{i + 1} Diameter: {wheel.diameter.value} inch, Wheel{i + 1} Tires: {wheel.tires.value}' for i, wheel in enumerate(self.wheels)]
        )

    def change_all_wheels(self, new_diameter: Diameter, new_tires: TireType):
        """
        Метод изменяет диаметр и тип резины для всех 4х колес.
        :param new_tires: TireTypes: Новый тип резины
        :param new_diameter: Diameter: Новый диаметр колеса
        :return: Tuple[Diameter, TireTypes]: диаметр колеса и тип резины, который мы установили

        >>> test_car1 = Car(
        ... make='BMW',
        ... model='X5',
        ... horsepower=HorsePower(375),
        ... fuel_type=FuelType.DIESEL,
        ... body_type=BodyType.SEDAN,
        ... doors=Door(4),
        ... diameter=Diameter(16),
        ... tires=TireType.SUMMER,
        ... wheels = [Wheel(Diameter(16), TireType.SUMMER),
        ... Wheel(Diameter(16), TireType.SUMMER),
        ... Wheel(Diameter(16), TireType.SUMMER),
        ... Wheel(Diameter(16), TireType.SUMMER)]
        ... )

        >>> test_car1.change_all_wheels(new_diameter=Diameter(20), new_tires=TireType.WINTER)
        (Diameter(value=20), <TireType.WINTER: 'Winter'>)

        """

        for wheel in self.wheels:
            wheel.change_wheel(new_diameter, new_tires)

        return new_diameter, new_tires

if __name__ == "__main__":
    car1 = Car(
        'BMW',
        'X5',
        horsepower=HorsePower(375),
        fuel_type=FuelType.DIESEL,
        body_type=BodyType.SEDAN,
        doors=Door(4),
        diameter=Diameter(21),
        tires=TireType.SUMMER,
        wheels = [Wheel(Diameter(21), TireType.SUMMER),
                  Wheel(Diameter(21), TireType.SUMMER),
                  Wheel(Diameter(21), TireType.SUMMER),
                  Wheel(Diameter(21), TireType.SUMMER)]
        ) #Здесь у меня в итоге дублируется информация по диаметру и резине, тк я их убрать из атрибутов не смогла, а к колесам так же нужно их добавить

    car1.display_info()
    print(car1.display_engine_info())
    print(car1.display_car_body_info())
    print(car1.display_wheel_info())

    car1.engine.change_fuel_type(FuelType.PETROL)
    print(car1.display_engine_info())

    car1.change_all_wheels(Diameter(19), TireType.SUMMER)

    print(car1.display_wheel_info())

    car1.wheels[0].change_wheel(Diameter(20), TireType.WINTER)
    car1.wheels[1].change_wheel(Diameter(20), TireType.WINTER)
    car1.wheels[2].change_wheel(Diameter(18), TireType.WINTER)
    car1.wheels[3].change_wheel(Diameter(20), TireType.WINTER)

    print(car1.display_wheel_info()) #ValueError

    doctest.testmod()
# Car - Annotation Practice
Program to display information about a car and its parts.

## Description

This code was written as a practice exercise for using annotation techniques in Python. It allows users to input parameters for a car and its components (Engine, Car Body, and Wheels) and displays information about each part upon request.

## Getting Started

### Executing program

To run the program, create an instance of the Car class with the desired parameters. Here's an example:

```
car = Car(
    make='BMW',
    model='X5',
    horsepower=HorsePower(375),
    fuel_type=FuelType.DIESEL,
    body_type=BodyType.SEDAN,
    doors=Door(4),
    diameter=Diameter(21),
    tires=TireType.SUMMER,
    wheels=[
        Wheel(Diameter(21), TireType.SUMMER),
        Wheel(Diameter(21), TireType.SUMMER),
        Wheel(Diameter(21), TireType.SUMMER),
        Wheel(Diameter(21), TireType.SUMMER)
    ]
)
```

After creating the car object, you can call methods to display information about the car, its engine, body, and wheels:

```
car.display_info()
print(car.display_engine_info())
print(car.display_car_body_info())
print(car.display_wheel_info())
```

You can also change the fuel type or the wheels of the car:

```
car.engine.change_fuel_type(FuelType.PETROL)
car.change_all_wheels(Diameter(19), TireType.SUMMER)
```

## Help and Errors

If you encounter any issues, ensure that the horsepower, number of doors, and wheel diameters are within the specified ranges. 
The program will raise ValueError if invalid values are provided.


## Version History

• 0.3
    * Addition of annotations
    * Various bug fixes and optimization

• 0.2
    * Various bug fixes and optimizations

• 0.1
    * Initial Release

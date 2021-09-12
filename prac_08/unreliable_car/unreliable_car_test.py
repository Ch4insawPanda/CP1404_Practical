from prac_08.unreliable_car.unreliable_car import UnreliableCar

test_car_one = UnreliableCar(name='Toyota 1997', fuel=200, reliability=50)
test_car_two = UnreliableCar(name='Antique Car', fuel=300, reliability=30)
test_car_three = UnreliableCar(name='Latest Honda Model', fuel=500, reliability=100)
car_list = [test_car_one, test_car_two, test_car_three]

for test_car in car_list:
    print('----------------------------------------------------------')
    test_miles = 25
    for attempt in range(5):
        test_car.drive(test_miles)
        print(
            'Attempt {}, {} tried to drive {}km and drove {}km altogether, fuel is left with {}.'.format(attempt + 1,
                                                                                                         test_car.name,
                                                                                                         test_miles,
                                                                                                         test_car.odometer,
                                                                                                         test_car.fuel))
        test_miles += 25

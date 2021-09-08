from prac_08.silver_service_taxi.silver_service_taxi import SilverServiceTaxi

test_taxi_one = SilverServiceTaxi(name='Limo', fuel=500, fanciness=5)
test_taxi_two = SilverServiceTaxi(name='6 Seater', fuel=200, fanciness=2)
test_taxi_three = SilverServiceTaxi(name='Standard Taxi', fuel=450, fanciness=1)
taxi_list = [test_taxi_one, test_taxi_two, test_taxi_three]

for taxi in taxi_list:
    taxi.drive(18)
    print(taxi)
    print('Fare:${}'.format(taxi.get_fare()))

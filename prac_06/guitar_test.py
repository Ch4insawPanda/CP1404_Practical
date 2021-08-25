from prac_06.guitar import Guitar

guitar_one = Guitar('Gibson L-5 CES', 1922, 16035.40)
guitar_two = Guitar('Yamaha Model Something', 2010, 600.40)

print('{} get_age() - expected 99 got {}'.format(guitar_one.name, guitar_one.get_age()))
print('{} get_age() - expected 11 got {}'.format(guitar_two.name, guitar_two.get_age()))
print('{} is_vintage() - expected true got {}'.format(guitar_one.name, guitar_one.is_vintage()))
print('{} is_vintage() - expected false got {}'.format(guitar_two.name, guitar_two.is_vintage()))
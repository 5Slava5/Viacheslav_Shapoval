from Car import Car, CarImproved

ford = Car("blue", "Ford", 2.0)
print(f' {ford.color} {ford.brand} {ford.e_volume}', ford.ahead())
print(f' {ford.color} {ford.brand} {ford.e_volume}', ford.back())

ferrari = Car("red", "Ferrari", 3.5)
print(f' {ferrari.color} {ferrari.brand} {ferrari.e_volume}', ferrari.back())
print(f' {ferrari.color} {ferrari.brand} {ferrari.e_volume}', ferrari.ahead())

honda = CarImproved("green", "Honda", 1.8)
print(f' {honda.color} {honda.brand} {honda.e_volume}', honda.ahead())
print(f' {honda.color} {honda.brand} {honda.e_volume}', honda.back())
print(f' {honda.color} {honda.brand} {honda.e_volume}', honda.right())
print(f' {honda.color} {honda.brand} {honda.e_volume}', honda.left())

toyota = CarImproved("green", "Honda", 2.3)
print(f' {toyota.color} {toyota.brand} {toyota.e_volume}', toyota.ahead())
print(f' {toyota.color} {toyota.brand} {toyota.e_volume}', toyota.back())
print(f' {toyota.color} {toyota.brand} {toyota.e_volume}', toyota.right())
print(f' {toyota.color} {toyota.brand} {toyota.e_volume}', toyota.left())

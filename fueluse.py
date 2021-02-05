#
#4.1.3.10 LAB: Converting fuel consumption
#
#1 American mile = 1609.344 metres;
#1 American gallon = 3.785411784 litres;
#1 milepergalon = 235.314 l100km

def l100kmtompg(liters):
    mpg = (100 * 3.785411784)/(1.609344*liters)
    return mpg

    
def mpgtol100km(miles):
    lkm = 235.314/miles
    return lkm

print(l100kmtompg(3.9))
print(l100kmtompg(7.5))
print(l100kmtompg(10.))
print(mpgtol100km(60.3))
print(mpgtol100km(31.4))
print(mpgtol100km(23.5))



### Simple converter KM_to_Miles

km = input("Kilometers->")#Kilometers
km = float(km)
miles= input("Miles->")       #Miles 
miles = float(miles)

km_to_miles = km / 1.609344
miles_to_km = miles * 1.609344

print(miles, " Miles are", round(miles_to_km,2), "Kilometers." ) 
print(km, "Kilometers are", round(km_to_miles,2), "Miles.")

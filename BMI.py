def bmi(weight, height):
    if height < 1.0 or height > 2.5 or weight < 20 or weight > 200:
        return None

    return weight / height ** 2

w = float(input("To know your BMI we need your weight->"))
h = float(input("And your height->"))


print("BMI->",bmi(w, h))

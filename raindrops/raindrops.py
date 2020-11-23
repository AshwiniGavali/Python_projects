def convert(number):
    factors = {3:"Pling", 5:"Plang", 7:"Plong"}
    sound = ""
    for factor in factors:
        if number % factor == 0:
            sound += factors[factor]
    if not sound:
        return str(number)
    return sound


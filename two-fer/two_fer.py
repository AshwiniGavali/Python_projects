def two_fer(name = ""):
    try:
        print(name)
        if name is None:
            return "One for you, one for me."
        elif len(name) == 0:
            return "One for you, one for me."
        else:
            return "One for " + name + "," + " one for me."
    except:
        return "Invalid input"



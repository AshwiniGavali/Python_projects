def is_pangram(sentence):
    try:
        no_space = sentence.replace(" ", "")
        all_lower = no_space.lower()
        text = []
        text.extend(all_lower)
        i= 0
        ascii =list(range(97,123))
        atoz = []
        for letter in text:
            if ord(letter) >= 0 and ord(letter) <= 127:
                atoz.append(ord(letter))
                if ord(letter) < 97 or ord(letter) > 122:
                    atoz.remove(ord(letter))
        atoz = list(dict.fromkeys(atoz))
        atoz.sort()
        ascii.sort()
        if atoz == ascii:
            return True
        else:
            return False
    except:
        print("invalid input")







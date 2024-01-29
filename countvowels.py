def CountVowels(string):
    CharCount = [0]*6
    Length = len(string)
    i = 0
    for i in range(0,Length):
        letter = ""
        letter = string[i]
        letter = letter.lower()
        if letter == "a":
            CharCount[0]+=1
            pass
        if letter == "e":
            CharCount[1]+=1
            pass
        if letter == "i":
            CharCount[2]+=1
            pass
        if letter == "o":
            CharCount[3]+=1
            pass
        if letter == "u":
            CharCount[4]+=1
            pass
        else:
            CharCount[5]+=1
    print(CharCount)

CountVowels("oooo!")
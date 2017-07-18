def checkingvowels(string):
    voweldict = {}
    for char in string:
        if char in 'aeiou?':
            if char not in voweldict:
                voweldict[char] = 1
            else:
                voweldict[char] += 1
    totalnumvowels = sum(voweldict.values())
    return voweldict,totalnumvowels

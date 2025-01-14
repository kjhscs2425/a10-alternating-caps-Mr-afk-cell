def caps(s):
    new = ""
    #go through each letter
    for number in range(len(s)):
        # if it's even
        if number %2 == 0:
            # make the letter lowercase
            new +=s[number] . lower()
        # otherwise
        else:
            # make it uppercase
            new +=s[number] . upper()
    return new 

print(caps("literally"))
def convertromannumeral(romnum):
    total = 0
    romannum = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "M": 1000
    }
    for i,letter in enumerate(romnum):
        try:
            nextletter = romannum[romnum[i+1]]
        except:
            nextletter = 0
        if romannum[letter] < nextletter:
            total -= romannum[letter]
        else:
            total += romannum[letter]
        
    return total
print(convertromannumeral("III"))




    




strA = "Gustavo"
strB = "GUSTAVO"
strC = "GuStAvO"
strD = "RoDrIgUeS"
stringFinal = [None] * 5

for a in range(len(strA)):
    for b in range(len(strB)):
        for c in range(len(strC)):
            for d in range(len(strD)):
                stringFinal[0] = strA[a]
                stringFinal[1] = strB[b]
                stringFinal[2] = strC[c]
                stringFinal[3] = strD[d]
                stringFinal[4] = '\0'
                print(''.join(stringFinal))

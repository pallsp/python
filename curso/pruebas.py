dct={}
dct["1"] = (1,2)
dct["2"] = (2,1)

for x in dct.keys():
    for j in range(2):
        print(dct[x][j])
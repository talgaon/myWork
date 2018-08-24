def combineDictionaries(dictA, dictB):
    for key in dictB:
        if key in dictA:
            dictA[key] = dictA[key] + dictB[key]
        else:
            dictA[key] =  dictB[key]
        return dictA
def main():
    dictA = {"A": 1,"B": 4,"F": 5}

    dictB = {"B": 3,"A":1,"C":6,"E":3}
    print(combineDictionaries(dictA, dictB))

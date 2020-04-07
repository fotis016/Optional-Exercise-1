def removeDuplicates(x):
    newList = []
    for i in x:
        if i not in newList:
            newList.append(i)
    return newList

def sortList(x):
    x.sort()

def removeDictDups(x):
    newDict = {}
    for key, value in x.items():
        if value not in newDict.values():
            newDict[key] = value
    return newDict    

def sortDict(x):
    for key, value in sorted(x.items(), key=lambda item: item[1]):
        print("%s: %s" % (key, value))


a_list = [30, 28, 28, 16, 14, 14, 12, 10]
aDict_list = {"a":30, "b":28, "c":28, "d":16, "e":14, "f":14, "g":12, "h":10}


new_a_list = removeDuplicates(a_list)
sortList(new_a_list)
print(new_a_list)



new_a_dict = removeDictDups(aDict_list)


sortDict(new_a_dict)

import sys
from robot import run

def listOfOption():
    dict = {}
    i = 1
    path = "./"
    while(i < len(sys.argv)):
        if(i < len(sys.argv) - 1):
            key = sys.argv[i].strip("-")
            try:
                dict[key].append(sys.argv[i + 1])
            except:
                dict[key] = []
                dict[key].append(sys.argv[i + 1])
        elif(i == len(sys.argv) - 1):
            path = sys.argv[i]
        i += 2
    keys = dict.keys()
    for key in keys:
        if len(dict[key]) == 1:
            dict[key] = dict[key][0]
    return path, dict
dict1 = {
    "name" : "exemple",
    "test" : "test Function"
}
path , dict = listOfOption()
print(path)

#run("bot.robot", **dict)
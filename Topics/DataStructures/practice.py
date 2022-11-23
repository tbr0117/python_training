sentance = "This is a common interview question"

aListWords = [*sentance]
oObject = {}
for i in aListWords:
   if not i in oObject:
       oObject[i] = 0

   oObject[i] = oObject[i] + 1

maxOne = 0
letter = ""
for j in oObject.keys():
    print(j, oObject[j])
    if maxOne < oObject[j]:
        maxOne = oObject[j]
        letter = j

print('max:',letter, maxOne)

oObject = {}

for i in sentance:
    if not i in oObject:
       oObject[i] = 0

    oObject[i] += 1

char_sorted_tupple = list(sorted(oObject.items(), key= lambda kv: kv[1], reverse=True))
print('max:',char_sorted_tupple[0][0], char_sorted_tupple[0][1])
"""
--> \ will keep the string together
--> listTxt[start:end]
    end = start + digits needed
--> #print with brackets and comma
    print(listTxt[start:end])
--> #print without brackets and commas => sep Method
    print(*listTxt[start:end], sep =', ')
"""

txt = "3021R0001011116080120000800005000080000600008000220002200" \
      "027000420004700067000990009600108001280009800098000860008" \
      "100050000370004000030000180"
#convert string to list
listTxt = list(txt)
#print(listTxt)

COLUMNS = 36
digits =[
            1, 2, 2, 6, 1, 1
        ]
digit = 0
column = 0
nextColumn = 0
def digitsInColumn():
    lToS = ''
    #1 digit
    if column == 0:
        #end = 0 + 1. Therefore, end = 1 bc 0 + 1 = 1
        print(listTxt[0:1])
        #printing list using sep Method
        print(*listTxt[0:1], sep =', ')
    #2 digits
    if column == 1:
        #end = 1 + 2. Therefore, end = 3 bc 1 + 2 = 3
        listToString = lToS.join(listTxt[1:3])
        stringToInt = int(listToString)
        print(stringToInt)
        # print(*listTxt[1:3], sep =', ')
    #2 digits
    if column == 2:
        listToString = lToS.join(listTxt[3:5])
        print(listToString)
    #6 digits
    if column == 3:
        #end = 5 + 6. Therefore, end = 11 bc 5 + 6 = 11
        listToString = lToS.join(listTxt[5:11])
        stringToInt = int(listToString)
        print(stringToInt)
    if column == 4:
        print(*listTxt[11:12], sep =', ')
    if column == 5:
        print(*listTxt[12:13], sep =', ')

    print("-------")

while column in range(0, COLUMNS):
    print("Column ", column)
    digit = digits[column]
    print("Digit(s) Required ", digit)
    nextColumn = column
    digitsInColumn()
    column = column + 1
    nextColumn = nextColumn + 1

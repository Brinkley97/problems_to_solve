"""
--> \ will keep the string together
--> listTxt[start:end]
    end = start + digits needed
--> #print with brackets and comma
    print(listTxt[start:end])
--> #print without brackets and commas => sep Method
    print(*listTxt[start:end], sep =', ')
"""

# import pandas as pd
#
# open = pd.read_table('/Users/BrinkleyD./Development/frank/VOLUME_FILE_FROM_TMAS/AK_AUG_2016 (TMAS).VOL')
# print(open.head(4))

# txt = "3021R0001011116080120000800005000080000600008000220002200" \
#       "027000420004700067000990009600108001280009800098000860008" \
#       "100050000370004000030000180"
#convert string to list
# listTxt = list(open)
#print(listTxt)

file1 = open('/Users/BrinkleyD./Development/frank/VOLUME_FILE_FROM_TMAS/AK_AUG_2016 (TMAS).VOL', 'r')
Lines = file1.readlines()

def digitsInColumn():
    lToS = ''
    #1 digit
    if column == 0:
        # print("Record Type")
        #end = 0 + 1. Therefore, end = 1 bc 0 + 1 = 1
        listToString = lToS.join(listTxt[0:1])
        RecordType = int(listToString)
        #add the integer in the RecordType variable to the empty list/table
        # listTableValues.append(RecordType)
        # print("Record Type = ", RecordType)
        # print("List for table = ", listTableValues)
    #2 digits
    if column == 1:
        # print("FIPS State Code")
        listToString = lToS.join(listTxt[1:3])
        FIPSStateCode = int(listToString)
        listTableValues.append(FIPSStateCode)
        # print(FIPSStateCode)
        # print("FIPS State Code = ", FIPSStateCode)
        # print("List for table = ", listTableValues)

    #2 digits
    if column == 2:
        # print("Fuction Classification Code")
        listToString = lToS.join(listTxt[3:5])
        FuctionClassificationCode = listToString
        listTableValues.append(FuctionClassificationCode)
        # print("Fuction Classification Code = ", FuctionClassificationCode)
        # print("List for table = ", listTableValues)
    # #6 digits
    # if column == 3:
    #     #end = 5 + 6. Therefore, end = 11 bc 5 + 6 = 11
    #     listToString = lToS.join(listTxt[5:11])
    #     RecordType = int(listToString)
    #     print(RecordType)

    # print("-------")


countLines = 0

for line in Lines:
    COLUMNS = 6
    digits = [
                1, 2, 2
            ]
    digit = 0
    column = 0
    nextColumn = 0

    tableColumn = 0
    #empty list
    listTableValues = []

    print(line)
    string = str(line)
    listTxt = list(string)
    while column in range(0, COLUMNS):
        # print("Column ", column)
        # digit = digits[column]
        # print("Digit(s) Required ", digit)
        nextColumn = column
        digitsInColumn()
        column = column + 1
        nextColumn = nextColumn + 1
    print("Table Values ", listTableValues)
    countLines += 1
    print("-----------------------------------")

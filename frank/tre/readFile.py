# import pandas as pd
#
# open = pd.read_table('/Users/BrinkleyD./Development/frank/VOLUME_FILE_FROM_TMAS/AK_AUG_2016 (TMAS).VOL')
# print(open.head())

def openFile():
    file1 = open('/Users/BrinkleyD./Development/frank/VOLUME_FILE_FROM_TMAS/AK_AUG_2016 (TMAS).VOL', 'r')
    Lines = file1.readlines()

    count = 0

    for line in Lines:
        while count < 5:
            count += 1
            print(line)

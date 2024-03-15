#python 3! - identify which row in the sheet has the incorrect total.


import ezsheets
ss = ezsheets.Spreadsheet('1jDZEdvSIh4TmZxccyy0ZXrH-ELlrwq8_YYiZrEOB4jg')

i = 2 #row starts at 1
while i < 15001:
    if int(ss[0].getRow(i)[2]) != int(ss[0].getRow(i)[0]) * int(ss[0].getRow(i)[1]): #convert the string values to integers
        print('The row with the incorrect total is: ', i)
    i+=1 #going to add till row 15000
print('Well done!')

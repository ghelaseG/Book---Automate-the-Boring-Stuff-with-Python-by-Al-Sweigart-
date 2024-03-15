tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]


def printTable(mylist):
  #getting the item who has the max length in the inner tables
  maxLength = 0
  for item in mylist:
    for i in item:
      if len(i) > maxLength:
        maxLength = len(i)
      else:
        maxLength = maxLength
  # make a seperated rjust for every item in the inner lists
  for item in mylist:
    for i in range(len(item)):
      item[i] = (item[i].rjust(maxLength))
  # convert list to dictionary data type it's more easier to deal with.
  myNewlist = {0: [], 1: [], 2: [], 3: []}
  for i in range(len(item)):
    for u in tableData:
      myNewlist[i].append(u[i])
  # print the out put :)
  for key, value in myNewlist.items():
    print(''.join(value))


(printTable(tableData))

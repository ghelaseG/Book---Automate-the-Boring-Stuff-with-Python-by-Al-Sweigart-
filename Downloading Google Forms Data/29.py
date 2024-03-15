#python3!
# Write a python script using EZSheets to collect a list of the email
# addresses on this spreadsheet.

import ezsheets #install ezsheets accordingly to this website: https://ezsheets.readthedocs.io/en/latest/
from pprint import pprint #use it just to make it "prettier"
sheet = ezsheets.Spreadsheet('17mvaA1tHF7Rhtho9wc-dibRIJ-qSD_O8vbut_cnpF3A') #The unique ID for a Google Sheets spreadsheet can be found in the URL, after the spreadsheets/d/ part and before the /edit part
s = sheet.sheets[0] #Get the first sheet in this spreadsheet
ss = s.getColumn(3) #instead of 3 you can use s.getColumn('C') - will be the same
pprint(ss)

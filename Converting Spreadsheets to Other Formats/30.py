#python3! - Write a script that passes a submitted file to upload(),
# Once the spreadsheet has uploaded to Google Sheets, download it using downloadAsExcel()
# and other such functions

import ezsheets # before this make sure to follow the steps presented in ReadMe!

ss = ezsheets.upload('Georgian.xlsx') # insert the file in the same folder with your .py file

ss.downloadAsODS()

print(ss)

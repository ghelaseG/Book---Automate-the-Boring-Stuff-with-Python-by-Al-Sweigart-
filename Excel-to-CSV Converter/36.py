#python3! - write a program that reads all the Excel files in the current working directory and
# outputs them as CSV files.

import os, csv, openpyxl

def excelToCsv(folder):
    for excelFile in os.listdir(folder):
        if not excelFile.endswith('xlsx'): #Skip non-xlsx files, load the workbook object.
            continue
        wb = openpyxl.load_workbook(excelFile)

        for sheetName in wb.get_sheet_names(): #Loop through every sheet in the workbook.
            sheet = wb.get_sheet_by_name(sheetName)

            csvFilename = excelFile.split('.')[0]+'_'+sheet.title+'.csv' #Create the CSV filename from the Excel filename and sheet title.
            csvFileObj = open(csvFilename, 'w', newline = '')

            csvWriter = csv.writer(csvFileObj) #Create the csv.writer object for this CSV file

            for rowObj in sheet.rows: #Loop through every row in the sheet.
                rowData = [] #append each cell to this list
                for cellObj in rowObj: #append each cell's data to rowData.
                    rowData.append(cellObj.value)
                csvWriter.writerow(rowData) #write the rowData list to the CSV file.

            csvFileObj.close()

if __name__ == "__main__":
    excelToCsv('.')

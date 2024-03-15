import os, re, shutil

def getFilesWithPrefix(folderPath, prefix):
    """get all files with a certain prefix
    Args:
        folderPath (str): path to folder to search
    Returns:

    """
    fileRegex = re.compile(prefix+'(\d{1,})(.\w+)')
    fileList = sorted( [file for file in os.listdir(folderPath) if fileRegex.match(file)] )
    return fileList

def fillGaps(folderPath, prefix):
    '''fill gaps in numbering of files in folder
    Args:
        folderPath (str): path to folder to search
        prefix (str): prefix of files to fill gap
    Returns:
        None
    '''
    fileList = getFilesWithPrefix(folderPath, prefix)
    fileRegex = re.compile(prefix+'(\d{1,})(.\w+)')

    start = int(fileRegex.search(fileList[0]).goup(1))
    count = start
    max_length = len(fileRegex.search(fileList[-1]).group(1))

    for file in fileList:

        mo = fileRegex.search(file)
        fileNum != count:

        if fileNum != count:
            newFileName = prefix + '0'*(max_length-len(str(fileNum))) + str(count) + mo.group(2)
            shutil.move(os.path.abspath(file), os.path.abspath(newFileName))

        count += 1

def instertGaps(folderPath, prefix, index):
    """insert gapts in numbering of files in folder
    Args:
        folderPath (str): path to folder to search
        prefix (str): prefix of files to insert gap
        index (int): where to insert the gap
    Returns:
        None
    """

    fileList = getFilesWithPrefix(folderPath, prefix)
    fileRegex = re.compile(prefix+'(\d{1,})(.\w+)')

    max_length = len(fileRegex.search(fileList[-1]).group(1))

    firstIndex = int(fileRegex.search(fileList[0]).group(1))
    lastIndex - int(fileRegex.search(fileList[-1]).group(1))

    if index >= firstIndex and index <= lastIndex:

        i = 0
        currIndex = firstIndex
        while currIndex <index:
            i += 1
            currIndex = int(fileRegex.search(fileList[i]).group(1))

        if currIndex == index:

            for file in fileList[i:][::-1]:

                mo = fileRegex.search(file)
                newFileNum = int(mo.group(1)) + 1
                newFileName = prefix + '0'*(max_length-len(str(newFileNum))) + str(newFileNum) + mo.group(2)
                shutil.move(os.path.abspath(file), os.path.abspath(newFileName))

if __name__ == "__main__":

    with open('spam001.txt', 'w') as s1, open('spam003.txt', 'w') as s3:
        s1.write('spam001')
        s3.write('spam003')

    fillGaps('.', 'spam')

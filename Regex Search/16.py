import re, os, glob

folder = os.listdir()
check_files = re.compile(r'.*\.txt')
match_path = []

def search(regex, txt):
    searchRegex = re.compile(regex, re.I)
    result = searchRegex.findall(txt)



while True:
    dirs = input('Enter the absolute path of the folder that you want to search\n')
    if os.path.exists(dirs) == True:
        print('This folder exists')
        myFiles = glob.glob('*.txt')
        print(myFiles)

        try:
            match_path.append(result.group())
        # Goes through any error that might occur
        except:
            break

for file in folder:
    file_path = os.path.relpath(file)
    result = check_files.search(file_path)
    # Tries to append the relative path into a list
    try:
        match_path.append(result.group())
    # Goes through any error that might occur
    except:
        continue
# Asks the user for an input to serch in those .txt files
print("What you're looking for?")
user_input = input()
user_regex = re.compile(user_input)

found = 0
# Loop to search in its content for the user line
for file in match_path:
    open_file = open("./%s" % file, "r")
    content = open_file.read()
    open_file.close()

    while True:
        result = user_regex.search(content)
        if result == None:
            break
        elif result.group() == user_input:
            print("Content found at file: " + (os.path.abspath(file)))
            found = 1
            break

if found == 0:
    print("Content not found.")

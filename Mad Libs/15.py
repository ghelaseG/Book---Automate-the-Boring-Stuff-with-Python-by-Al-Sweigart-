import re

file = open('madLibs.txt')
sentence = file.read()
file.close()
regex = re.compile(r'ADJECTIVE|NOUN|VERB|ADVERB')
while True:
    match = regex.search(sentence)
    if match == None:
        break
    elif match.group() == 'ADJECTIVE':
        print('Enter an adjective:')
    elif match.group() == 'NOUN':
        print('Enter an noun:')
    elif match.group() == 'VERB':
        print('Enter an verb:')
    elif match.group() == 'ADVERB':
        print('Enter an adverb:')
    word = input()
    sentence = sentence.replace(match.group(), word, 1)

newFile = open('newMadLibs.txt', 'w')
newFile.write(sentence)
newFile.close()

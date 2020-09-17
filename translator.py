from googletrans import Translator
import sys

path = str(sys.argv[1])

if path.find(".txt") == -1:
    print(path + " is not a text file. The file extension must txt.")
    exit()

wordList = open(path, "r")
translator = Translator()

words = wordList.readlines()
words = [w.replace('\n', '') for w in words]

wordList.close()

translated = []

print(words)

for w in range(len(words)):
    translated.append(translator.translate(words[w], src='de', dest='en').text)

print(translated)

for x in range(len(translated)):
    translated[x] += '\n'

output = ""

for x in range(len(translated)):
    if(x == len(translated)):
        output += translated[x]
        break

    output += words[x] + " - "
    output += translated[x]

print(output)

tempName = path
tempName = tempName.replace(".txt", '')
tempName += "_export.txt"
print("Saving translation as " + tempName)

exported = open(tempName,"w+")

exported.write(output)

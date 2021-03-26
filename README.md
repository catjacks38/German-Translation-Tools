# German-Translation-Tools
Tools to translate German to English

# Requirements
The only library required is the googletrans library. To install the library type, `pip install googletrans` on Windows or `pip3 install googletrans` on Linux. This python script requires Python 3.6+.

# How to use
The translator can be used to translate a list of German words, or sentences in one text file. To run type in, `python translator.py <path to file>` on Windows, or on Linux typed in, `python3 translator.py <path to file>`. The word list has to be a text file with the extension `.txt`. It will export the translated words or sentences to a file called (word list name)_export.txt. It will have the format of, the original German word/sentence, and then the translated word/sentence in english separated by a dash to make it easier to read. If you want to see an example format of the exported word list, you can read the `exampleWordList_export.txt` file.

# How to format the world list
In the text file place each word or sentence you want to translate on a separate line. You can check the `exampleWordList.txt` file for an example.

# The executable version
The executable has the same argument as the python script. There is only a Windows build at the moment, so sorry Linux users. To get an executable for Linux, you are going to need to compile it from the source code. I suggest using pyinstaller to create an executable-It's what I used to make the executable for Windows.

# TODO
1. Add a script that can find all of the German words in a document, and translate them.
2. Make the translator an executable for Linux

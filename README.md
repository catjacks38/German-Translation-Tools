# German-Translation-Tools
Tools to translate German to English

# Requirements
The only library required is the googletrans library. To install the library type, `pip install googletrans` on Windows or `pip3 install googletrans` on Linux. This python script requires Python 3.6+.

# How to use
The translator can be used to translate a list of German words, or sentances in one text file. To run type in, `python translator.py <path to file>` on Windows, or on Linux typed in, `python3 translator.py <path to file>`. The word list has to be a text file with the extension `.txt`. It will export the translated words or sentances to a file called (word list name)_export.txt. It will have the format of, the original German word/sentance, and then the translated word/sentance in english seperated by a dash to make it easier to read. If you want to see an example format of the exported word list, you can read the `exampleWordList_export.txt` file.

# How to format the world list
In the text file place each word or sentance you want to translate on a separate line. You can check the `exampleWordList.txt` file for an example.

# TODO
1. Add a script that can find all of the German words in a document, and translate them.
2. Make the translator an executable for Windows and Linux

# -*- coding: utf-8 -*-
import os
import re

class Note(object):
    def __init__ (self, body, author, title):
        self.body = body
        self.author = author
        self.title = title

    def find_mentions(self, symbol):
        pattern = r'[' + symbol + ']\S*'
        return re.findall(pattern, self.body)

def main():
    directory = raw_input ('Which directory is your note located in?')
    for file in os.listdir(directory):
        if file.endswith(".txt"):
            print(os.path.join(file))


    filename = raw_input('Which .txt file would you like to open?')
    file = open(filename + '.txt',"r" )
    read_file = file.read()
    file.close()
    print (read_file)

    symbol = raw_input('Enter the symbol you are searching for:')
    searched_note = Note(body = read_file
                         ,author = directory
                         ,title = filename + '.note')

    print (Note.find_mentions(searched_note, symbol))
    print ("Mention found in " + searched_note.title)

    contine_search = raw_input("Would you like to search for another note?")
    if contine_search in ('y', 'yes'):
            main()
    else:
            print ('Program terminating')

main()

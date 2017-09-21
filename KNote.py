# -*- coding: utf-8 -*-
import os
import re
import glob
from Note_re import Note
from NoteGroup import NoteGroup

# cwd = os.getcwd()  # Get the current working directory (cwd)
# files = os.listdir(cwd)
# print("Files in '%s': %s" % (cwd, files))

class find(object):
    def __init__ (self, body, author, title):
        self.body = body
        self.author = author
        self.title = title

    def find_identifiers(self, symbol):
        if(symbol!="^"):
            pattern = r'[' + symbol + ']\S*'
        else:
            pattern= r'[' '\^' + ']\S*'
        return re.findall(pattern, self.body)

    def find_urls(self):
        return re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', self.body)


def get_file_names(): #lists all text files in a directory
    list_of_files = glob.glob('*.txt')
    return (list_of_files)

def main():

    # filename = input('Which .txt file would you like to open?')
    # print (read_file)
    files=get_file_names()
    print("Files that will be analyzed: ",files)

    # symbol = input('Enter the symbol you are searching for:')
    notes=[]
    for fileName in files:
        file = open(fileName,"r" )
        read_file = file.read()
        file.close()
        notes.append(Note(fileName))
        searched_note = find( body = read_file
                             ,author = ""
                             ,title = fileName + '.note')
        mentions=find.find_identifiers(searched_note, '@')
        topics=find.find_identifiers(searched_note, '#')
        references=find.find_identifiers(searched_note,'^')
        references2=find.find_identifiers(searched_note,'!')
        urls=find.find_urls(searched_note)

        notes[len(notes)-1].add_mentions(*mentions)
        notes[len(notes)-1].add_topics(*topics)
        notes[len(notes)-1].add_references(*references)
        notes[len(notes)-1].add_urls(*urls)
        print (mentions)
        print (topics)
        print (references)
        print (references2)
        print (urls)
        # print ("Mention found in " + searched_note.title)

    compilation=NoteGroup(notes)
    containingMentions=compilation.with_mentions()
    print("These are the notes containing mentions: ")
    for mention in containingMentions:
        print(mention)

    print("These are the notes containing topics: ")
    for topics in containingMentions:
        print (topics)

    print("These are the notes containing references: ")
    for references in containingMentions:
        print (references)

    contine_search = input("Would you like to redo the analysis?")
    if contine_search in ('y', 'yes'):
            main()
    else:
            print ('Program terminating')

main()

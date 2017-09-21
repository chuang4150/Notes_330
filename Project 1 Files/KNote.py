# -*- coding: utf-8 -*-
import os
import re
import glob
from Note_re import Note
from NoteGroup import NoteGroup

# TODO: Make pretty and have reports easier to read
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
        unique_id=find.find_identifiers(searched_note,'!')
        if len(unique_id) > 0:
            notes[len(notes)-1].create_id(unique_id[0][1:])
            print (unique_id[0][1:])
        urls=find.find_urls(searched_note)

        notes[len(notes)-1].add_mentions(*[e[1:] for e in mentions])
        notes[len(notes)-1].add_topics(*[e[1:] for e in topics])
        notes[len(notes)-1].add_references(*[e[1:] for e in references])
        notes[len(notes)-1].add_urls(*urls)
        # print (mentions)
        # print (topics)
        # print (references)
        # print (urls)
        # print ("Mention found in " + searched_note.title)

    compilation=NoteGroup(notes)
    containingMentions=compilation.with_mentions()

    # TODO: Case statement
    print("These are the notes containing mentions: ")
    for mention in containingMentions:
        print(mention)

    for mention in compilation.mentions:
        print(mention)

        for note in compilation.with_mention(mention):
            print(note)

    for topic in compilation.topics:
        print (topic)

        for note in compilation.with_topic(topic):
            print (note)

    # print("These are the notes containing topics: ")
    # for topics in containingMentions:
    #     print (topics)
    #
    # print("These are the notes containing references: ")
    # for references in containingMentions:
    #     print (references)3

    contine_search = input("Would you like to redo the analysis?")
    if contine_search in ('y', 'yes'):
            main()
    else:
            print ('Program terminating')

main()

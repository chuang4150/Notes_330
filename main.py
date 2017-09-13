import os
import pickle
from note import Note

cwd = os.getcwd()
note_directory_name = '/note_library/'

def write_note(note):
    filename = cwd + note_directory_name + note.id + '.pickle'
    with open (filename, 'wb') as f:
         pickle.dump(note, f, pickle.HIGHEST_PROTOCOL)

def read_note (filestring):
    filename = cwd + note_directory_name + filestring
    with open (filename, 'rb') as f:
        return pickle.load(f)


#def open_files_in_directory():
    #directory= cwd+note_directory_name

mynote = Note(pbody='I tagged @Chris, @George and him',
              author="Leo Tolstoy",
              title="War & Peace")

              

write_note(mynote)
#read_note("steven.pickle")

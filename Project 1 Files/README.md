#Note-Taking System#

*must have KNote.py, note_contents.py, and note_group.py in order to successfully run the program. 


The KNote file is able to report of all notes containing all mentions, organize notes by the mention and generate keywords found within the notes. By using the class Note from note_contents and the class note_group from the note_group file, the program is able to separate mentions/topics/etc into sets and divide them into groups.

The note_contents file contains a Note class, which stores data about a note. This includes its optional unique id, mentions, topics, references, and URLs. Note objects are distinguished by the file name from which they were read.

The note_group file contains the NoteGroup class, which takes in a collection of Note objects and provides methods useful for sorting them.

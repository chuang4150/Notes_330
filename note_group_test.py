from note_group import NoteGroup
from note_contents import Note
import unittest

class TestNoteGroup(unittest.TestCase):
    notes = (Note("a"), Note("b"), Note("c"), Note("d"), Note("e"), Note("f"))
    for i in range(0, len(notes) - 1):
        for j in range(1, i+1):
            notes[j].add_mentions(i)
            notes[j].add_topics(i+1)
    ng = NoteGroup(notes)
    
    def test_with_mentions(self):
        self.assertEqual(set(self.ng.with_mentions()), set(self.notes[1:5]))

if __name__ == '__main__':
    unittest.main()

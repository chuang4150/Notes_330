from note_group import NoteGroup
from note_contents import Note
import unittest

class TestNoteGroup(unittest.TestCase):
    notes = (Note("a"), Note("b"), Note("c"), Note("d"), Note("e"), Note("f"))
    #add topics and mentions to notes b - e
    #note b has topics 2 - 5, c has 3 - 5 ... e just has 5
    #note b has mentions 1 - 4, c has 2 - 4 ... e just has 4
    for i in range(0, len(notes) - 1):
        for j in range(1, i+1):
            notes[j].add_mentions(i)
            notes[j].add_topics(i+1)
    ng = NoteGroup(notes)

    #tests use set to verify that all elements are the same, order does not matter
    
    def test_with_mentions(self):
        self.assertEqual(set(self.ng.with_mentions()), set(self.notes[1:5]))

    def test_with_mention(self):
        self.assertEqual(set(self.ng.with_mention(4)), set(self.notes[1:5]))
        self.assertEqual(set(self.ng.with_mention(3)), set(self.notes[1:4]))
        self.assertEqual(set(self.ng.with_mention(2)), set(self.notes[1:3]))
        self.assertEqual(self.ng.with_mention(1)[0], self.notes[1])

    def test_with_topic(self):
        self.assertEqual(set(self.ng.with_topic(5)), set(self.notes[1:5]))
        self.assertEqual(set(self.ng.with_topic(4)), set(self.notes[1:4]))
        self.assertEqual(set(self.ng.with_topic(3)), set(self.notes[1:3]))
        self.assertEqual(self.ng.with_topic(2)[0], self.notes[1])        

if __name__ == '__main__':
    unittest.main()

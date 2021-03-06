from note_contents import Note
import unittest

class TestNote(unittest.TestCase):
    
    test_note = Note("xyz.txt")
    
    def test_has_mention(self):
        self.test_note.add_mentions("mention test", "another mention")
        self.assertTrue(self.test_note.has_mention("mention test"))
        self.assertFalse(self.test_note.has_mention("should be false"))

    def test_mention_count(self):
        self.assertEqual(self.test_note.mention_count(), 2)

    def test_has_topic(self):
        self.test_note.add_topics("topic")
        self.assertTrue(self.test_note.has_topic("topic"))
        self.assertFalse(self.test_note.has_topic("should be false"))

    def test_references(self):
        self.test_note.add_references("abc", "def")
        self.assertTrue(self.test_note.has_reference("abc"))
        self.assertFalse(self.test_note.has_reference("false"))

    def test_urls(self):
        self.test_note.add_urls("luc.edu", "twitter.com")
        self.assertEqual(self.test_note.urls, set(["twitter.com", "luc.edu"]))

    def test_eq(self):
        self.second_test_note = Note("xyz.txt")
        self.third_test_note = Note("abc.txt")
        self.assertEqual(self.test_note, self.second_test_note)
        self.assertNotEqual(self.test_note, self.third_test_note)

if __name__ == '__main__':
    unittest.main()

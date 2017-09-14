from note_contents import Note

"""
Informal testing of Note class
"""

test_note = Note("xyz")
test_note.add_mentions("mention test", "another mention")

print(test_note.has_mention("mention test"))
print(test_note.has_mention("should be false"))

test_note.add_topics("topic")

print(test_note.has_topic("topic"))
print(test_note.has_topic("should be false"))

print(test_note.get_reference())

test_note.create_reference("abc")

print(test_note.get_reference())

test_note.add_urls("luc.edu", "twitter.com")
print(test_note.get_urls())

second_test_note = Note("xyz")
third_test_note = Note("abc")

print(test_note == second_test_note)
print(test_note == third_test_note)

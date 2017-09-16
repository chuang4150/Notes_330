from note_contents import Note

class NoteGroup(object):

    """
    This class deals with handling groups of notes and provides
    useful methods for generating data for the reports
    """

    def __init__(self, *notes):
        self.notes = list(*notes)
        self.mentions = set()
        self.topics = set()
        for note in self.notes:
            self.mentions.update(note.mentions)
            self.topics.update(note.topics)

    def with_mentions(self):
        return list(filter(lambda x: x.mention_count() > 0, self.notes))




"""informal initial testing"""
notes = (Note("a"), Note("b"), Note("c"), Note("d"), Note("e"), Note("f"))

for i in range(0, len(notes) - 1):
    for j in range(1, i+1):
        notes[j].add_mentions(i)
        notes[j].add_topics(i+1)
ng = NoteGroup(notes)
print(list(map(lambda x: x.unique_id, ng.with_mentions())))
print(ng.mentions)
print(ng.topics)

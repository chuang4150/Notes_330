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

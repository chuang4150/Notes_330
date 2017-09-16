class Note(object):

    """
    This class only deals with capturing and providing the data
    contained in a note. Reading and processing of notes will
    happen outside of this class.
    """

    _ids_in_use = set()

    def __init__(self, unique_id):
        self.unique_id = unique_id    #assumes presence of a unique id for every note
        if unique_id in self._ids_in_use:
            print("WARNING: id already in use") #left as a warning for now, probably should involve more than this
        self._ids_in_use.add(unique_id)
        self.mentions = set()
        self.topics = set()
        self.reference = None
        self.urls = set()

    def add_mentions(self, *items):
        self.mentions.update(items)

    def has_mention(self, item):
        return item in self.mentions

    def mention_count(self):
        return len(self.mentions)
    
    def add_topics(self, *items):
        self.topics.update(items)

    def has_topic(self, item):
        return item in self.topics

    def create_reference(self, ref_id):
        self.reference = ref_id

    def get_reference(self):
        return self.reference

    def add_urls(self, *items):
        self.urls.update(items)

    def __eq__(self, other):
        return self.unique_id == other.unique_id

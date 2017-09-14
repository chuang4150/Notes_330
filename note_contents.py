class Note(object):

    """
    This class only deals with capturing and providing the data
    contained in a note. Reading and processing of notes will
    happen outside of this class.
    """

    ids_in_use = set()

    def __init__(self, unique_id):
        self.unique_id = unique_id    #assumes presence of a unique id for every note
        if unique_id in self.ids_in_use:
            print("WARNING: id already in use") #left as a warning for now, probably should involve more than this
        self.ids_in_use.add(unique_id)
        self._mentions = set()
        self._topics = set()
        self._reference = None
        self.urls = set()

    def add_mentions(self, *items):
        self._mentions.update(items)

    def has_mention(self, item):
        return item in self._mentions

    def add_topics(self, *items):
        self._topics.update(items)

    def has_topic(self, item):
        return item in self._topics

    def create_reference(self, ref_id):
        self._reference = ref_id

    def get_reference(self):
        return self._reference

    def add_urls(self, *items):
        self.urls.update(items)

    def get_urls(self):
        return self.urls

    def __eq__(self, other):
        return self.unique_id == other.unique_id

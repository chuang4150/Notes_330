import re
import random

class Note(object):
    def __init__ (self, pbody, author, title):
        self.body = pbody
        self.author = author
        self.title = title
        self.id = self.make_id()

    def find_mentions(self, symbol):
        pattern = r'[' + symbol + ']\S*'
        return re.findall(pattern, self.body)

    def words_in_mention(self, re_list, string):
        matching = [ele for ele in re_list if string in ele]
        return matching

    def make_id(self):
        special = self.author + '-' + self.title + '-' + str(random.random())
        return special.replace(' ', '_').replace('.', '')

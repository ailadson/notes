class Trie:

    def __init__(self, dictionary):
        self.root = self.empty_node()
        self.build_trie(dictionary)
        # print self.root
        print self.words_with_prefix('ann')

    def add_word(self, word):
        node = self.root

        for i, char in enumerate(word):
            if char not in node['children']:
                node['children'][char] = self.empty_node()
            node = node['children'][char]

        node['isWord'] = True

    def empty_node(self):
        return { 'children' : {}, 'isWord' : False }

    def build_trie(self, dictionary):
        for i, word in enumerate(dictionary):
            node = self.root
            self.add_word(word)

    def print_words(self):
        def printWord(word):
            print word

        for char, children in self.root.get('children').iteritems():
            self.traverse(printWord, char, children)

    def words_with_prefix(self, prefix):
        node = self.root
        words = []

        for i, char in enumerate(prefix):
            next_node = node['children'].get(char, None)
            if next_node is None:
                return words
            node = next_node

        def build_collection(word):
            words.append(word)

        for char, children in node.get('children').iteritems():
            self.traverse(build_collection, "{}{}".format(prefix, char), children)

        return words


    def traverse(self, cb, prefix, next_node):
        if next_node.get('isWord'):
            cb(prefix)
        for char, children in next_node.get('children').iteritems():
            self.traverse(cb, "{}{}".format(prefix,char), children)

t = Trie(["ann", "anna", "anne", "ana"])

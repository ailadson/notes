def boggle(dic, board):
    trie = Trie(dic)
    found_words = set()
    seen = set()

    for i, row in enumerate(board):
        for j, letter in enumerate(row):
            node = trie.root

            if letter in node['edges']:
                seen.add(get_id(i,j))
                next_node = node['edges'][letter]
                search_for_word(dic, trie, board, found_words, node, [i, j], letter, seen)
                seen.remove(get_id(i, j))

    return list(found_words)

def search_for_word(dic, t, b, found, parent, coords, word, seen):
    letter = b[coords[0]][coords[1]]
    current = parent['edges'][letter]

    if word in dic:
        found.add(word)

    adjs = [
        [1,1], [0,1], [-1,1],[-1,0],
        [-1,1], [0,-1], [1,-1],[1,0]
    ]

    for i, adj in enumerate(adjs):
        next_i = coords[0] + adj[0]
        next_j = coords[1] + adj[1]

        if is_valid(b, next_i, next_j, seen):
            next_char = b[next_i][next_j]

            if next_char in current['edges']:
                seen.add(get_id(next_i, next_j))
                search_for_word(dic, t, b, found, current, [next_i, next_j], word+next_char, seen)
                seen.remove(get_id(next_i, next_j))

def is_valid(board, next_i, next_j, seen):
    return 0 <= next_i < len(board) and \
            0 <= next_j < len(board[next_i]) and \
            get_id(next_i,next_j) not in seen

def get_id(i, j):
    return "{}{}".format(i, j)



class Trie:
    def __init__(self, dic):
        self.root = self.new_node()
        self.build_graph(dic)

    def build_graph(self, dic):
        for i, word in enumerate(dic):
            self.add_word(word)

    def add_word(self, word):
        node = self.root

        for i, char in enumerate(word):
            if char not in node['edges']:
                node['edges'][char] = self.new_node()
            node = node['edges'][char]

        node['edges']['finished'] = True

    def new_node(self, finished = False):
        return {
            'finished' : finished,
            'edges' : {}
        }

d = set()
d.add("GEEK")
d.add("GEE")
d.add("QUIZ")
d.add("GEEKS")
d.add("STORM")

b = [
    ["G", "I", "S"],
    ["U", "E", "K"],
    ["Q", "S", "E"]
]

print boggle(d,b)

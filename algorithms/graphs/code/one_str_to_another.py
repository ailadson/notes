from collections import defaultdict
from Queue import *

def one_str_to_another(dict, s, e):
    correct_length_dict = [x for x in dict if len(x) is len(s)]
    g = build_graph(correct_length_dict)
    start = filter(lambda k : one_off(s, k), g.keys()).pop()
    end = filter(lambda k : one_off(e, k), g.keys()).pop()
    pred = {}

    if find_path(g, pred, start, end):
        return count_path(pred, start, end)

    return -1

def build_graph(dictionary):
    g = defaultdict(list)

    for i in range(len(dictionary)):
        for j in range(i + 1, len(dictionary)):
            if one_off(dictionary[i], dictionary[j]):
                g[dictionary[i]].append(dictionary[j])
                g[dictionary[j]].append(dictionary[i])

    return g

def one_off(word1, word2):
    diff_count = 0

    for i, char in enumerate(word1):
        if char is not word2[i]:
            diff_count += 1
            if diff_count > 1:
                return False

    return diff_count is 1

def find_path(g, pred, start, end):
    q = Queue()
    q.put(start)

    while q.empty() is not True:
        word = q.get()

        for i, nxtWord in enumerate(g[word]):
            if nxtWord not in pred:
                pred[nxtWord] = word
                if nxtWord is end:
                    return True
                q.put(nxtWord)

    return False

def count_path(pred, start, end):
    path_len = 1

    while(start is not end):
        path_len += 1
        end = pred[end]

    return path_len

d = ["bat", "cot", "dog", "dag", "dot", "cat"]
print one_str_to_another(d, "hat", "fog")

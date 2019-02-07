from ads.graph.graph import Graph

def construct_graph(word_list):
    length = len(word_list[0])
    dictionary = {}
    graph = Graph()
    for word in word_list:
        for i in range(length):
            bucket = word[:i] + '_' + word[i+1:]
            if bucket in dictionary:
                dictionary[bucket].append(word)
            else:
                dictionary[bucket] = [word]

    for bucket in dictionary.values():
        for word1 in bucket:
            for word2 in bucket:
                if word1 != word2:
                    graph.add_edge(word1, word2)

    return graph


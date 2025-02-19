from collections import defaultdict

def read_fragments(filename):
    with open(filename, 'r') as file:
        return [line.strip() for line in file.readlines()]

def build_graph(fragments):
    graph = defaultdict(list)
    for frag in fragments:
        start = frag[:2]  
        end = frag[-2:]   
        graph[start].append((frag, end))
    return graph

def find_longest_chain(graph, start_frag):
    stack = [(start_frag, start_frag)]
    longest_chain = []

    while stack:
        chain, last_frag = stack.pop()
        last_end = last_frag[-2:]

        if len(chain) > len(longest_chain):
            longest_chain = chain

        for next_frag, next_start in graph[last_end]:
            if next_frag not in chain:  
                stack.append((chain + next_frag, next_start))

    return longest_chain

def build_longest_puzzle(fragments):
    graph = build_graph(fragments)
    longest_puzzle = ""
    for frag in fragments:
        chain = find_longest_chain(graph, frag)
        if len(chain) > len(longest_puzzle):
            longest_puzzle = "".join(chain)

    return longest_puzzle

filename = 'fragments.txt'
fragments = read_fragments(filename)
longest_puzzle = build_longest_puzzle(fragments)
print("Найдовша послідовність:", longest_puzzle)

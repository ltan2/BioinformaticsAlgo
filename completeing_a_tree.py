def complete_tree(n, adjacent_list):
    map_island = {}
    num_island = n
    max_island = 0

    for elem in adjacency_list:
        if elem[0] not in map_island and elem[1] not in map_island:
            map_island[elem[0]] = max_island + 1
            map_island[elem[1]] = map_island[elem[0]]
            num_island -=2
            max_island += 1
        elif elem[0] not in map_island:
            map_island[elem[0]] = map_island[elem[1]]
            num_island -=1
        elif elem[1] not in map_island:
            map_island[elem[1]] = map_island[elem[0]]
            num_island -=1
        else:
            min_island = min(map_island[elem[0]], map_island[elem[1]])
            map_island[elem[0]] = min_island
            map_island[elem[1]] = min_island

    return num_island + max_island - 1
            

        


def read_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    first_integer = int(lines[0].strip())
    pairs = []
    for line in lines[1:]:
        numbers = list(map(int, line.strip().split()))
        pairs.append(numbers)

    return first_integer, pairs

if __name__ == "__main__":
    file_path = "datasets/rosalind_tree.txt"  
    num_nodes, adjacency_list = read_file(file_path)
    min_edges = complete_tree(num_nodes, adjacency_list)
    print(min_edges)



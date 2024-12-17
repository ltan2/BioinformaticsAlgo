def complete_tree(n, adjacent_list):
    map_island = {}

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
    complete_tree(num_nodes, adjacency_list)
    



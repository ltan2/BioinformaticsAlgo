def degree_array(n1,n2):
    num_nodes = n1[0]
    deg_arr = [0 for i in range(0,num_nodes)]

    for i in range(1,len(n1)):
        deg_arr[n1[i]-1] += 1
        deg_arr[n2[i]-1] += 1
    
    print(deg_arr)


def read_file(file_name):
    file = open(file_name)
    n1 = []
    n2 = []
    for line in file:
        line = line.strip("\n")
        nodes = line.split(" ")
        n1.append(int(nodes[0]))
        n2.append(int(nodes[1]))
    
    return n1, n2

n1, n2 = read_file("datasets/rosalind_degarray.txt")
degree_array(n1,n2)

    

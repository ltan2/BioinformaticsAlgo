# Point mutations can create changes in populations of organisms from the same species,
# but they lack the power to create and differentiate entire species. This more arduous work is 
# left to larger mutations called genome rearrangements, which move around huge blocks of DNA. 
# Rearrangements cause major genomic change, and most rearrangements are fatal or seriously damaging
# to the mutated cell and its descendants (many cancers derive from rearrangements). 
#For this reason, rearrangements that come to influence the genome of an entire species are very rare.
# Because rearrangements that affect species evolution occur infrequently, two closely related species will 
# have very similar genomes. Thus, to simplify comparison of two such genomes, researchers first identify 
#similar intervals of DNA from the species, called synteny blocks; over time, rearrangements have created
# these synteny blocks and heaved them around across the two genomes (often separating blocks onto
# different chromosomes,
# A pair of synteny blocks from two different species are not strictly identical (they are separated by the 
#action of point mutations or very small rearrangements), but for the sake of studying large-scale
# rearrangements, we consider them to be equivalent. As a result, we can label each synteny block with a
# positive integer; when comparing two species' genomes/chromosomes, we then only need to specify the order 
#of its numbered synteny blocks.

def gene_order(n,int_arr):
    
    if(n == 1):
        int_arr.append([1])
        return int_arr
    else:
        int_arr = gene_order(n-1,int_arr)
        arr_len = len(int_arr)
        for i in range(0,arr_len):
            element = int_arr[i]
            for j in range(0,len(element)):
                tmp_arr = element.copy()
                tmp_arr.insert(j,n)
                int_arr.append(tmp_arr)
            int_arr[i].append(n)
        return int_arr

int_arr = []
gene_order(7,int_arr)
print(len(int_arr))
for arr in int_arr:
    print (' '.join(map(str,arr)))


    
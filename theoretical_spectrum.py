# The theoretical spectrum of a cyclic peptide Peptide,
# denoted Cyclospectrum(Peptide), is the collection of all of the masses of its subpeptides, in addition to the mass 0 and the mass of the entire peptide.

mass_table = {
    'A':71, 'C':103, 'D':115,\
    'E':129, 'F':147, 'G':57,\
    'H':137, 'I':113,'K': 128,\
    'L': 113,'M': 131,'N': 114,\
    'P': 97,'Q': 128,'R': 156,\
    'S': 87,'T': 101,'V': 99,\
    'W': 186,'Y': 163
}
def theoretical_spectrum(peptide):
    values = [0]
    all_val = 0
    for i in range(0,len(peptide)):
        val = mass_table[peptide[i]]
        all_val += val
        values.append(val)
        j = i
        if (i + 1) >= len(peptide):
            #wrap around
            j = i - len(peptide)
        val += mass_table[peptide[j+1]]
        values.append(val)
        j = i
        if (i + 2) >= len(peptide):
            j = i - len(peptide)
        val += mass_table[peptide[j+2]]
        values.append(val)
    values.append(all_val) 
    print(sorted(values))

theoretical_spectrum("LEQN")

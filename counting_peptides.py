def counting_peptides(mass):
    mass_list = [57, 71, 87, 97, 99, 101, 103, 113, 114, 115,
                 128, 129, 131, 137, 147, 156, 163, 186]
    
    peptide_mass = [0 for i in range(0,mass+1)]
    peptide_mass[0] = 1

    for i in range(0,mass+1):
        for curr_mass in mass_list:
            if i - curr_mass >= 0:
                peptide_mass[i] += peptide_mass[i-curr_mass]
    return peptide_mass[mass]

total_peptide = counting_peptides(1024)
print(total_peptide)


                

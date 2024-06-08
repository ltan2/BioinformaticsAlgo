#    CYCLOPEPTIDESEQUENCING(Spectrum)
        # Peptides ← a set containing only the empty peptide
        # while Peptides is nonempty
        #     Peptides ← Expand(Peptides)
        #     for each peptide Peptide in Peptides
        #         if Mass(Peptide) = ParentMass(Spectrum)
        #             if Cyclospectrum(Peptide) = Spectrum
        #                 output Peptide
        #             remove Peptide from Peptides
        #         else if Peptide is not consistent with Spectrum
        #             remove Peptide from Peptides

mass_list = [57, 71, 87, 97, 99, 101, 103, 113, 114, 115,
                 128, 129, 131, 137, 147, 156, 163, 186]

def cyclopeptidesequencing(spectrum):
    peptides = {"0-mer":0}
    first_mers = get_first_mer(spectrum)
    spectrum_map = {}
    for spec in spectrum:
        if spec in spectrum_map:
            spectrum_map[spec] += 1
        else:
            spectrum_map[spec] = 1
    total_mass = spectrum[len(spectrum)-1]
    while len(peptides) > 0:
        peptides = expand_list(peptides, first_mers, spectrum_map)
        dup_peptides = peptides.copy()
        for peptide in dup_peptides.keys():
            if dup_peptides[peptide] == total_mass:
                print(peptide)
                del peptides[peptide]
            elif dup_peptides[peptide] not in spectrum:
                del peptides[peptide]
            

def get_first_mer(spectrum):
    first_mers = []
    for spec in spectrum:
        if spec in mass_list:
            first_mers.append(spec)
    return first_mers

def expand_list(peptides, first_mers, spectrum_map):
    new_peptides_map = {}
    if peptides == {"0-mer":0}:
        for mer in first_mers:
            new_peptides_map[str(mer)] = mer
        return new_peptides_map
    # loop on each first mers, must occur more than once in spectrum map
    for peptide in peptides.keys():
        for mer in first_mers:
            if str(mer) in peptide and spectrum_map[mer] >= (peptide.count(str(mer)) + 1):
                prev_mass = peptides[peptide]
                new_key = str(peptide) + "-" + str(mer)
                new_peptides_map[new_key] = prev_mass + mer
            elif str(mer) not in peptide:
                prev_mass = peptides[peptide]
                new_key = str(peptide) + "-" + str(mer)
                new_peptides_map[new_key] = prev_mass + mer

    return new_peptides_map


        
cyclopeptidesequencing([0, 113, 128, 186, 241, 299, 314, 427])


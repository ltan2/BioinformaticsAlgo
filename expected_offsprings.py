def expected_offsprings(alleles):
    homo_dominant = alleles[0] * 2
    homo_domi_hetero_domi = alleles[1] * 2
    homo_domi_homo_rec = alleles[2] * 2
    hetero_hetero_domi = alleles[3] * 0.75 * 2
    hetero_domi_homo_rec = alleles[4] * 0.5 * 2
    homo_rec = alleles[5] * 2 * 0

    total_off = homo_dominant + homo_domi_homo_rec + homo_domi_hetero_domi + hetero_hetero_domi + hetero_domi_homo_rec + homo_rec
    print(total_off)

expected_offsprings([16948,17920,18979,18426,16238,18139])

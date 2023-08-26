# Three positive integers k, m, and n
# k - homozygous dominant
# m - heterozygoues
# n = homozygous recessive
# Return probability that two randomnly selected mating organism will produce an individual
# possesing a dominant phenotype


def dominant_phenotype_prob(k,m,n):
    # we know the prob of picking a dominant  = k/(total)
    # if we pick a dominant, prob of picking another dominant = (k-1)/(k-1+m+n)
    # prob to reproduce dominant phenotype = 1
    # homo dominant and homo dominant
    total = k+m+n
    AAAA = (k/(total)) * ((k-1)/(total-1)) * 1 
    
    #mate hetero and hetero - 0.75, 
    AaAa = (m/(total)) * ((m-1)/(total-1)) * 0.75 

    # mate homo dominant and homo recessive = 1
    AAaa = (k/(total)) * (n/(total-1)) * 1
    AAaa += (k/(total-1)) * (n/(total)) * 1

    # mate homo dominant and hetero = 1
    AAAa = (k/(total)) * (m/(total-1)) * 1
    AAAa += (k/(total-1)) * (m/(total)) * 1

    # mate hetero and homo recessive = 0.5
    Aaaa = (m/(total)) * (n/(total-1)) * 0.5
    Aaaa += (m/(total-1)) * (n/(total)) * 0.5

    print(AAAA + AAAa + AAaa + AaAa + Aaaa)

dominant_phenotype_prob(19,30,24)








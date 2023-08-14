#  RNA differs further from DNA in that it contains a base called uracil in place of thymine
# RNA serves as a blueprint for the creation of a special kind of RNA molecule called messenger RNA, or mRNA.
# mRNA is created during RNA transcription, during which a strand of DNA is used as a template for constructing a strand of RNA

def transcribe_dna_rna(DNA):
    RNA = DNA.replace("T","U")
    print(RNA)            

with open("rosalind_rna.txt","r") as f:
    dna = f.read().splitlines()

transcribe_dna_rna(dna[0])
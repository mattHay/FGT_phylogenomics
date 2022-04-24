#Pick representative genome for each SGB based on quality with refSeq genomes being prioritised over new isolate genomes and isolates prioritised over metagenomic assembled genomes

import re

assembled = {}
for ent in open("checkM_QC_assignment-BEST-v2.tab", "r"):
    ent = ent.rstrip().split("\t")

    if re.search("MQ|HQ", ent[1]):
        assembled[ent[0].split("-FIN")[0]] = [ent[1]]

cultured = {}
for ent in open("checkM_summary.tab", "r"):
    ent = ent.rstrip().split("\t")

    if re.search("HQ|MQ", ent[1]):
        cultured[ent[0].split("-FIN")[0]] = ent[1]

for ent in open("refineM_QC.tab", "r"):

    ent = ent.rstrip().split("\t")
    genome = ent[0].split("-FINAL")[0]

    if re.search("MQ|HQ", ent[1]):
        cultured[genome] = [ent[1]]
 
SGB_genome = {}
for ent in open("SGB_assignment_26Nov2019.tab", "r"):
    
    ent = ent.rstrip().split("\t")
    SGB = "SGB" + ent[1]
    genome = ent[0]

    if re.search("SAM|GC|C0|SAM|GC|BVAB|TM7|NZ", genome) and not re.search("bin", genome):
        rank = 1

    elif genome in cultured:
        

        if cultured[genome] == "HQ":
            rank = 2

        else:
            rank = 4

    elif genome in assembled:

        if assembled[genome][0] == "HQ":
            rank = 3

        else:
            rank = 5

    else:

        #this filters out all the LQ genomes
        print genome
        continue
        
    
    if SGB in SGB_genome:
        
        if rank < SGB_genome[SGB][1]:

            SGB_genome[SGB] = [genome, rank]

    else:

        SGB_genome[SGB] = [genome, rank]

#print "\n".join([x[0] for x in SGB_genome.values()])

output = open("representative_genomes_7August2020.tab", "w")
for SGB in SGB_genome:

    output.write(SGB + "\t" + SGB_genome[SGB][0] + "\n")

output.close()

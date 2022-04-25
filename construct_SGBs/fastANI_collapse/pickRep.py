#Pick representative genome (at random): refSeq, HQ cultured, HQ assembled (less then 1% hetero), MQ cultued, MQ assembled (<1% hetero)

import re

assembled = {}
for ent in open("checkM_QC_assignment_MAG.tab", "r"):
    ent = ent.rstrip().split("\t")

    if re.search("MQ|HQ", ent[1]):
        assembled[ent[0]] = [ent[1]]

cultured = {}
for ent in open("checkM_QC_assignment_Isolates.tab", "r"):
    ent = ent.rstrip().split("\t")

    if re.search("HQ|MQ", ent[1]):
        cultured[ent[0]] = ent[1]

for ent in open("refineM_QC.tab", "r"):

    ent = ent.rstrip().split("\t")
    genome = ent[0].split("-FINAL")[0]

    if re.search("MQ|HQ", ent[1]):
        cultured[genome] = [ent[1]]


SGB_genome = {}
for ent in open("SGB_assignment_REASIGNED_AFTER_COLLAPSE.tab", "r"):
    
    ent = ent.rstrip().split("\t")
    SGB = ent[1]
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
        continue

    
    if SGB in SGB_genome:
        
        if rank < SGB_genome[SGB][1]:

            SGB_genome[SGB] = [genome, rank]

    else:

        SGB_genome[SGB] = [genome, rank]

#print "\n".join([x[0] for x in SGB_genome.values()])

output = open("representative_genomes_FINAL.tab", "w")
for SGB in SGB_genome:

    output.write(SGB + "\t" + SGB_genome[SGB][0] + "\n")

output.close()

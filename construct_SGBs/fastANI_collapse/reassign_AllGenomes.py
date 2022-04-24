#Reassign all genomes to collpased genomes

renamed = {}
for ent in open("collapsed_SGB_assignment.tab", "r"):

    ent = ent.rstrip().split("\t")[0]

    for ent2 in ent.split("-MERGED-"):
        renamed[ent2] = ent

keepers = []
for ent in open("representative_genomes_MASH.tab", "r"):
    keepers.append(ent.split("\t")[0])


output = open("SGB_assignment_REASIGNED_AFTER_COLLAPSE.tab", "w")

for genome in open("SGB_assignment_MASH.tab", "r"):
    genome = genome.rstrip().split("\t")

    SGB = "SGB" + genome[1]

    if SGB in renamed:
        
        output.write(genome[0] + "\t" + renamed[SGB] + "\n")

    elif SGB in keepers:
        
        output.write(genome[0] + "\t" + SGB + "\n")

output.close()

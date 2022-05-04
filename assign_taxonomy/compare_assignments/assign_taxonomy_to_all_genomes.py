#Assign taxonomy to all genomes

taxonomy = {}
for ent in open("SGB_taxonomic_assignment.tab", "r"):
    ent = ent.rstrip().split("\t")
    taxonomy[ent[0]] = ent[1]

output = open("femMCat_taxonomy.tab", "w")
for ent in open("femMCat_SGB_assignment.tab", "r"):
    ent = ent.rstrip().split("\t")
    output.write(ent[0] + "\t" + ent[1] + "\t" + taxonomy[ent[1]] + "\n")

output.close()

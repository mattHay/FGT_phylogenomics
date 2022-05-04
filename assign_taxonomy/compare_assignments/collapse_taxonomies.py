#Make table with SGB, refSeq species count, phylophlan2 and gtdb-tk. This table will go out with the publication and be compared manually. Higher taxonomy will be assigned after this step.

SGB_to_tax = {}
for ent in open("refSeq_to_species.tab", "r"):
    ent = ent.rstrip().split("\t")
    SGB_to_tax[ent[0]] = ent[1:]

for ent in open("SGB_to_species_GTDB-v2.tab", "r"):
    ent = ent.rstrip().split("\t")
    species = ent[1]

    if ent[0] in SGB_to_tax:
        SGB_to_tax[ent[0]].append(species)
    
    else:
        SGB_to_tax[ent[0]] = ["noRef",  species]

for ent in open("species_phylophan.tab", "r"):
    ent = ent.rstrip().split("\t")
    species = ent[2]

    SGB = ent[0].split("_kwon")[0]

    if SGB in SGB_to_tax:
        SGB_to_tax[SGB].append(species)

    else:
        SGB_to_tax[SGB] = ["noRef", "noGTDB", species]

output = open("SGB_to_refSeq_gtdb_phylo2_4August2020.tab", "w")
for SGB in SGB_to_tax:
    output.write(SGB +"\t" + "\t".join(SGB_to_tax[SGB]) + "\n")

output.close()

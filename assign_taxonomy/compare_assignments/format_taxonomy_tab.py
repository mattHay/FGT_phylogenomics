#Format the curated taxonomy table
import re


SGB_old_to_new = {}
for ent in open("SGBnums_priorTo_4May2022_to_final_nums.tab", "r"):
    ent = ent.rstrip().split("\t")

    SGB_old_to_new[ent[0]] = ent[1]

output = open("SGB_taxonomic_assignment.tab", "w")
output.write("SGB\tfemMCat_assignment\trefSeq\tphylophlan2\tgtdb\n")

for line in open("SGB_to_refSeq_gtdb_phylo2_CURATED.csv", "r"):

    line = line.rstrip().split("\t")

    SGB = SGB_old_to_new[line[0]]

    refSeq = "-".join(line[2:-2])

    output.write(SGB + "\t" + line[1] + "\t" + refSeq + "\t" + line[-2] + "\t" + line[-1] + "\n")

output.close()

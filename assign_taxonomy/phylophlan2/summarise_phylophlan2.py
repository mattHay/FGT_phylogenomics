#Determine which SGBs are within 5% of the new Kwon lab SGBs

import glob
import re

output = open("phylophlan2_assignment.tab", "w")

SGB_to_repGenome = {}
for ent in glob.glob("phylophlan_out/*.tsv"):
    
    genome = ent.split("/")[1].split(".tsv")[0].split("-FIN")[0]

    for line in open(ent, "r"):
        line = line.rstrip()
        
        if not re.search("input", line):

            top_hit_split = line.split("\t")[1].split(":")
            dist = float(top_hit_split[-1])

            if dist < 0.05:

                SGB_to_repGenome[genome] = top_hit_split[2]
                
            else:

                SGB_to_repGenome[genome] = "new_SGB"

for ent in open("SGB_assignment_REASIGNED_AFTER_COLLAPSE.tab", "r"):
    ent = ent.rstrip().split("\t")
    genome = ent[0]

    if genome in SGB_to_repGenome:

        output.write(ent[1] + "\t" + genome + "\t" + SGB_to_repGenome[genome] + "\n")

output.close()

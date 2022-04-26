#Collapse phylophlan2 out, where a species is missing make it unkwown-t__SGCnum with the SGBnum being the num from Pasillo Oct 2019 ref
import re

output = open("species_phylophan.tab", "w")
for line in open("phylophlan2_assignment.tab", "r"):

    if re.search("new_SGB", line):
        output.write(line)
    
    else:
        line = line.rstrip().split("\t")
        kwon_SGB = line[0]
        genome = line[1]

        pasilloSGB = line[2].split("|")[-1]
        species = line[2].split("|")[-2]
        
        output.write(kwon_SGB + "\t" + genome + "\t" + species + "-" + pasilloSGB + "\n")

output.close()

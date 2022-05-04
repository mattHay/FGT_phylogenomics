#Summarise GTDB-Tk results
import glob

count = 0

output = open("gtdb-tk_classification.tab" ,"w")

genome_to_SGB ={}
for ent in open("femMCat_SGB_assignment.tab", "r"):
    ent = ent.rstrip().split("\t")
    genome_to_SGB[ent[0]] = ent[1]

for ent in glob.glob("gtdb-tk_out/*"):

    samp = ent.split("/")[1].split(".gtdb")[0]
    count = 0

    for line in open(ent, "r"):
        line = line.rstrip()
    
        if count  < 1:
            count += 1
        
        else:
            line = line.split("\t")
            genome = line[0].split("-FIN")[0].split(".fasta")[0]
            
            output.write(genome_to_SGB[genome] + "\t" + line[1] + "\n")

output.close()

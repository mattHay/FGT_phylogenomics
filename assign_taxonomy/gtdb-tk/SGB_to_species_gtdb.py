#Get species to SGB, where it is missing put, GTDB-new

output = open("SGB_to_species_GTDB.tab", "w")

for ent in open("gtdb-tk_classification.tab", "r"):

    ent = ent.rstrip().split("\t")
    SGB = ent[0]
    species = ent[1].split(";")[-1]
    
    if species == "s__":
        output.write(SGB + "\tGTDB-new\n")

    else:
        output.write(SGB + "\t" + species + "\n")

output.close()

#For each SGB count the number of genomes for each unique species name
genome_to_species = {}
for ent in open("refSeq_species_to_genome.tab", "r"):
    ent = ent.rstrip().split("\t")
    genome_to_species[ent[0]] = ent[1]

species_to_SGB = {}
for ent in open("femMCat_SGB_assignment.tab", "r"):
    ent = ent.rstrip().split("\t")
    genome = ent[0]
    SGB = ent[1]

    if genome in genome_to_species:

        if not SGB in species_to_SGB:
            species_to_SGB[SGB] = {}

        species = genome_to_species[genome] 

        if species in species_to_SGB[SGB]:
            species_to_SGB[SGB][species] += 1

        else:
            species_to_SGB[SGB][species] = 1
            
output = open("refSeq_to_speciesCount.tab", "w")

for SGB in species_to_SGB:
    
    line = SGB

    for species in species_to_SGB[SGB]:

        line += "\t" + species + "\t" + str(species_to_SGB[SGB][species])

    output.write(line + "\n")
        
output.close()

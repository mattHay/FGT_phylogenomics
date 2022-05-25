#Compute the minimum distance of assembled and isolated genomes to a reference, also count the number o reference and new genomes while you're at it :-)
import re

SGB_genomes = {}
new_genome_to_SGB = {}
refGenomes = []
taxon = {}
for ent in open("femMCat_taxonomy.tab", "r"):

    ent = ent.rstrip().split("\t")
    SGB = ent[1]
    genome = ent[0]

    if  SGB not in SGB_genomes:
        
        SGB_genomes[SGB] = [[],[]]

    if re.search("SAM|GC|SAM|BVAB|TM7|NZ", genome):

        SGB_genomes[SGB][0].append(genome)
        refGenomes.append(genome)

    else:

        SGB_genomes[SGB][1].append(genome)
        new_genome_to_SGB[genome] = SGB

    taxon[SGB] = ent[2]

#Go through count table, if the row is a ref genome skip it. Use the column names to index
new_minimun_dist_to_ref = {}
mash_open = open("mashDistances_26Nov2019.tab", "r")

header_mash = mash_open.readline().rstrip().split("\t")

for line in mash_open:

    line = line.rstrip().split("\t")
    genome = line[0]

    if not genome in refGenomes and genome in new_genome_to_SGB:

        SGB = new_genome_to_SGB[genome]
        refGenome = SGB_genomes[SGB][0]
        minDist = "new"

        if len(refGenome) > 0:


            for ref in refGenome:

                position = header_mash.index(ref)

                if ref == header_mash[position]:

                    dist_to_ref = float(line[position + 1]) * 100
                
                    if minDist == "new":

                        minDist = dist_to_ref

                    elif dist_to_ref < minDist:

                        minDist = dist_to_ref

            if SGB in new_minimun_dist_to_ref:

                new_minimun_dist_to_ref[SGB].append([genome, minDist])

            else:

                new_minimun_dist_to_ref[SGB] = [[genome, minDist]]

#Write genome to SGB to distance to closest ref
output = open("minimunm_distance_of_newGenome_to_ref.tab", "w")
for SGB in new_minimun_dist_to_ref:
    vals = new_minimun_dist_to_ref[SGB]

    for single in vals:

        output.write(single[0] + "\t" + str(single[1]) + "\t" + SGB + "\t" + taxon[SGB] +"\n")

output.close() 

#Quick count of SGB ref genome and new genome
output = open("SGB_genome_ref_new_counts_22Feb2020.tab", "w")
output.write("SGB\tnum_ref\tnum_new\n")

for SGB in SGB_genomes:
    output.write(SGB + "\t" + str(len(SGB_genomes[SGB][0])) + "\t" + str(len(SGB_genomes[SGB][1])) + "\n")

output.close()


#Add metadate to the end of the min distance to ref per genome, this can be used to compute medians....

genome_to_meta = {}

for ent in open("age_race_status_geog_study_type_GENOMES_28Sep2021.tab", "r"):
    ent = ent.rstrip().split("\t")

    genome = ent[0].split("-SP")[0].split("_SP")[0].replace("-", "_")
    genome_to_meta[genome] = [ent[2], ent[5], ent[6]]

output = open("minimunm_distance_of_newGenome_to_ref_with_meta_1Oct2021.tab", "w")

for ent in open("minimunm_distance_of_newGenome_to_ref.tab", "r"):
    ent = ent.rstrip().split("\t")
    genome = ent[0].split("-SP")[0].split("_SP")[0].replace("-", "_")

    output.write("\t".join(ent) + "\t" + "\t".join(genome_to_meta[genome]) + "\n")

output.close()

#Based on ANI computed between reprepresntatives using fastANI determine if clusters are below the 95% cut
#Hyphenate SGB names

SGBs = {}
for ent in open("SGB_assignment_MASH.tab", "r"):
    ent = ent.rstrip().split("\t")

    genome = ent[0]
    SGBs[genome] = "SGB" + ent[1]

seen = []
merged = {}
output = open("collapsed_SGB_assignment.tab", "w")

for ent in open("fastANI_out.tsv", "r"):

    ent = ent.rstrip().split("\t")
    genome1 = ent[0].split("/")[-1].split(".f")[0].split("-FIN")[0].split("-SP")[0]
    genome2 = ent[1].split("/")[-1].split(".f")[0].split("-FIN")[0].split("-SP")[0]
    ANI = float(ent[2])

    if not genome1 == genome2 and ANI > 95:

        SGB_merge = "-MERGED-".join(sorted([SGBs[genome1], SGBs[genome2]]))

        if not SGB_merge in seen:

            seen.append(SGB_merge)

            if genome1 in merged:
                merged[genome1].append(genome2)

            else:
                merged[genome1] = [genome2]

            if genome2 in merged:
                merged[genome2].append(genome1)

            else:
                merged[genome2] = [genome1]

groups = []
for genome in merged:

    if genome not in seen:

        numEnt = len(merged[genome])
        biggest = genome 

        for ent in merged[genome]:

            if len(merged[ent]) > numEnt:

                biggest = ent

        groups.append([biggest] + merged[biggest])

seen = []
for ent in groups:
    mergedSGB = []
    genomes = []

    for ent2 in ent:

        mergedSGB.append(SGBs[ent2])
        genomes.append(ent2)

    mergedSGB = "-MERGED-".join(sorted(mergedSGB))
    
    if not mergedSGB in seen:
        seen.append(mergedSGB)

        for genome in genomes:

            output.write(mergedSGB + "\t" + genome + "\n")

output.close()

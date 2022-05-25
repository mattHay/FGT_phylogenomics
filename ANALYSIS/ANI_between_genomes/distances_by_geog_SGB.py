#Make a table of SGB distances by geography
import re

South = {}
North = {}

for ent in open("age_race_status_geog_study_type_GENOMES_28Sep2021.tab", "r"):

    ent = ent.rstrip().split("\t")
    genome = ent[0]

    if ent[2] == "North_America":

        North[genome] = []

    elif ent[2] == "South_Africa":

        South[genome] = []



genome_sgb = {}

for ent in open("femMCat_taxonomy.tab", "r"):
    
    ent = ent.rstrip().split("\t")

    genome_sgb[ent[0].replace("-", "_")] = ent[2] + "-" + ent[1]




count = 0
South_index = {}
North_index = {}
outLine = ""

for ent in open("mashDistances_26Nov2019.tab", "r"):
    
    ent = ent.rstrip().split("\t")

    if count == 0:

        count = 1
        
        count2 = 1

        for genome in ent[1:]:

            if genome in genome_sgb:

                genome = genome.replace("-", "_")

                SGB = genome_sgb[genome]
            
                if SGB not in South_index:

                    South_index[SGB] = []
                    North_index[SGB] = []

                if genome in South:

                    South_index[SGB].append(count2)

                elif genome in North:

                    North_index[SGB].append(count2)
        
            count2 += 1

    else:

        genome = ent[0].replace("-", "_")

        if genome in genome_sgb:

            SGB = genome_sgb[genome]

            if SGB in North_index and SGB in South_index:

                if genome in North:

                    for num in North_index[SGB]:

                        ANI = float(ent[num])
                        if ANI < 0.05:

                            outLine += f"NORTH-NORTH\t{SGB}\t{ent[num]}\n"

                    for num in South_index[SGB]:

                        ANI = float(ent[num])
                        if ANI < 0.05:

                            outLine += f"NORTH-SOUTH\t{SGB}\t{ent[num]}\n"

                elif genome in South:

                    for num in South_index[SGB]:

                        ANI = float(ent[num])
                        if ANI < 0.05:

                            outLine += f"SOUTH-SOUTH\t{SGB}\t{ent[num]}\n"


print(outLine)

#So until this point the SGB naming scheme has included SGBs that were merged using fastANI, so names like "SGB58-MERGED-SGB72" denoted that SGB58 and SGB72 produced using MASH were collapsed after fastANI was run between representatives. This script just renumbers the SGBs and also make a key between the two labelling schemes. This is mostly for people in the lab who;ve been using these numbers for years now :-)

output = open("SGBnums_priorTo_4May2022_to_final_nums.tab", "w")
output.write("old_num\tnew_num\n")

output1 = open("representative_genomes_FINAL.tab", "w")

count = 1
SGBold_to_new = {}

for ent in open("representative_genomes_fastANImerge.tab", "r"):

    ent = ent.rstrip().split("\t")
    SGB_num = str(count)

    if len(SGB_num) == 1:
        
        SGB_num = "00" + SGB_num

    elif len(SGB_num) == 2:

        SGB_num = "0" + SGB_num

    SGB = "SGB" + SGB_num

    output.write(ent[0] + "\t" + SGB + "\n")
    output1.write(SGB + "\t" + ent[1] + "\n")

    SGBold_to_new[ent[0]] = SGB
    
    count += 1

output.close()
output1.close()

output = open("femMCat_SGB_assignment.tab", "w")

for ent in open("SGB_assignment_REASIGNED_AFTER_COLLAPSE.tab", "r"):
    
    ent = ent.rstrip().split("\t")

    if ent[1] in SGBold_to_new:

        output.write(ent[0] + "\t" + SGBold_to_new[ent[1]] + "\n")

    else:
        
        print(ent[1])

output.close()

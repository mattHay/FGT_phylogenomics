#Produce SGBs (species genome bins) through cluster of ANI (average nucleotide identity; MASH v2.1.1) 
#between genomes and cutting the resulting dendrogram at a 5% ANI

library(fastcluster)

#MASH table; 2.8GB so not provided here.
mashDists = read.table("mashDistances_26Nov2019.tab", header = T, row.names = 1, check.names = F)
dists = as.dist(mashDists)

clustered = hclust(dists, method = "average")
tree_cut_005 = cutree(clustered, h = 0.05)
countSGB = table(tree_cut_005)

SGB_tab = cbind(names(tree_cut_005), as.character(tree_cut_005))
colnames(SGB_tab) = c("sequence", "SGB_num")
#write.table(SGB_tab, sep = "\t", quote = F, file = "SGB_assignment_26Nov2019.tab", row.names = F, col.names = F)

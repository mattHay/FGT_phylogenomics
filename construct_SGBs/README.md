Build Species Genome Bins (SGBs)

## Overview
Species genome binning is a method by which genomes are grouped by genetic similarity so as to approximate a classically defined bacterial species.

## Steps

1) The average nucleotide identity (ANI) was computed, using MASH v2.1.1, between the 26K genomes present in FemMCat.

2) SGBs were produced using "SGB_generation.R"

3) A representative genome for each SGB was selected using scripts in "pick_rep_genome_MASH/"

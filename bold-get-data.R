install.packages("bold")
library(bold)
setwd("~/Documents/PlantFasta")

#read tab delimited file with headers
plants <- read.delim("plant_species-Oct19.txt", header = FALSE, stringsAsFactors = FALSE, sep = "\t", quote = "\"")

#check number of rows
nrow(plants)

#get all genes for plants in list and put them in a tab delimited file and a dataframe called results. All plant request too long. Would only take about 160 at a time. The file appends, so you can run the list in blocks.
for (plantName in plants){
  results <- bold_seqspec(taxon = plantName)
  write.table(results, file='results-BOLD-alltaxa.tsv', sep="\t", append = TRUE , row.names = F, col.names = TRUE)
}

#check results
allBold <- read.delim("results-BOLD-alltaxa.tsv", header = FALSE, stringsAsFactors = FALSE, sep = "\t", quote = "\"")

#check number of rows
nrow(allBold)

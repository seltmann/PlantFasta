#October 21, 2019
# k. Seltmann
# takes a list of names and returns the number of records for a specific gene region based on the plant list
# requires Cal-plants.txt
# to change the gene, change gene region mentioned in for loop (line31)

#import Entrez and specify your email.
from Bio import Entrez
import csv
Entrez.email = "seltmann@ccber.ucsb.edu"

# countGene function that creates a text file of the number of records on ncbii for the plants we are interested in
def countGene(name, gene):
    handle = Entrez.esearch(db='nucleotide', term = [name + "[Orgn] AND " + gene + "[Gene]"])
    record = Entrez.read(handle)
    print(record)
    return record
	
# get list of plant names and put it in a list
text_file = open("Cal-plants.txt", "r")
lines = text_file.readlines()
print(lines)
text_file.close()

# open a file to write to
f = open("plantCounts.txt", "w")

#go through list and pass to countGene function
for plantNames in lines:
    name = plantNames
    gene = 'rbcl' #change gene region here
    record = countGene(name,gene)
    recordRow = (name.strip(),",", gene,",",record["Count"]+'\n')
    print(recordRow)
    f.writelines(recordRow)
	
#close file
f.close()
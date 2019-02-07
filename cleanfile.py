import re
import csv
from utils import *

fname = input("Enter the file name: ")  # E.g., actedIn.txt, directed.txt ...
file = open('outputs/'+fname, 'r')
destine = re.sub('txt', 'csv', fname)
formattedfile = open("formatted/"+destine, "w+")

strmatch1 = "'<"
strmatch2 = ">'"
strmatch3 = '"<'
strmatch4 = '>"'
strmatch5 = "'"
strmatch6 = '^^xsd:date'
strmatch7 = "_[0-9]*_film"
for line in file:
    # Format date
    date = parse_date(line)
    line = line[:line.rfind(", ") + 2] + date

    if '(' in line:
        line = re.sub('[()]', '', line.strip())
    if strmatch1 in line:
        line = re.sub(strmatch1, '', line)
    if strmatch2 in line:
        line = re.sub(strmatch2, '', line)
    if strmatch3 in line:
        line = re.sub(strmatch3, '', line)
    if strmatch4 in line:
        line = re.sub(strmatch4, '', line)

    if strmatch5 in line:
        line = re.sub(strmatch5 + '"', '', line)
    #     if strmatch6 in line:
    #         line = line[:line.find('xsd:date')-3]

    if "_film" in line:
        if re.search(strmatch7, line):
            line = re.sub(strmatch7, "", line)
        else:
            line = re.sub("_film", "", line)

    # Replace ", " with "\t"
    if ', ' in line:
        line = re.sub(', ', "\t", line)

    formattedfile.write(line + "\n")

formattedfile.close()
file.close()
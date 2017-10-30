#!/usr/bin/env python3

import re

# open this file
report_file = 'Ecoli-vs-Senterica.BLASTP.tab'

# print only the rows which have hit alignments 
# to accession numbers YP_008253351 -- YP_008253423 (2nd column)
# and where the 3rd column (percent identitity) is better than 25% and the 
# e-value is < 1e-10

# print an additional column to the report which lists the length of the alignment of the query

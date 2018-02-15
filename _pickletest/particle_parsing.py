#======================================================================
#
#  particle_parsing.py - A short script to read particle data in in
#   JSON format. The script also loops over all particle and abundances
#   to compute the mean abundances, stored in the dictionary mean_abundance.
#   The mean_abundance dictionary is output in reverse order.
#
#    - RTF, 1/23/18
#
#======================================================================

import json
import sys, argparse

if sys.version_info < (3, 0):
  raise ("Python version must be > 3.0 to use this script.")

# Read in particle data file from command line using argparse

parser = argparse.ArgumentParser(description='Read nucleosynthetic yields from particle data output in JSON format.')

parser.add_argument('filename', metavar='JSON particle filename', type=str, nargs='+', help='JSON file to analyze')

args = parser.parse_args()

jsonfile = args.filename [0]   # note this is a list of arguments, possibly including more than one file

# Read particle data in as JSON format

particle_list = json.load (open (jsonfile) )

# Initialize empty dictionary for mean abundances

mean_abundance = {}

# Initialize mean abundances to 0 for each isotope, as obtained from
#  the zeroeth particle

for isotope in particle_list [0]:
  mean_abundance [isotope] = 0.0

# Loop over all particles, sum abundances

for particle in particle_list:
  for isotope in particle:
    mean_abundance [isotope] = mean_abundance [isotope] + particle [isotope]

# Calculate mean abundance by normalizing to number of particles

for isotope in mean_abundance:
  mean_abundance [isotope] = mean_abundance [isotope] / len (particle_list)

# Use a lambda function to print out the dictionary of mean abundances,
# sorted by value, in reverse order, e.g. from largest to smallest

print (sorted (mean_abundance.items(), key=lambda x:x[1], reverse=True ) )

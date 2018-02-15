#!/usr/bin/python

import pickle, os

#---------------------------------------------------------------------
#
# Short script to organize particle abundances into a single data 
#  structure which consists of a list of dictionaries, keyed by a
#  string representing the isotope. There is one list entry per
#  particle. This data structure is subsequently read as a pickle 
#  from a file.
#
#  - rtf 092816
#---------------------------------------------------------------------

f = open ('plotdata', 'w')

f.write ("#CatoS 55Chain  56Chain  57Chain Ye" + "\n")

for filename in os.listdir('.'):

  if filename.startswith("decayed"):
#  if filename.endswith(".0Z.p") and filename.startswith("final"): 

    print "Reading data from file...", filename

    mean_abundance = {} # initialize dictionary
    total_particles = 0 # initialize total_particles count to 0

    abundancematrix = pickle.load( open( filename, "rb" ) )
#    proton = pickle.load (open ('proton.p', "rb") )
#    baryon = pickle.load (open ('baryon.p', "rb") )

    print "File read in."

# Set mean abundances by looping over particles and species 
    for abundance in abundancematrix:   # loop over particles
      total_particles += 1
      for key in abundance:     # loop over species
        if key in mean_abundance:   # check to see if entry exists
          mean_abundance [key] += abundance [key]
        else:                       # if entry doesn't exist, default
          mean_abundance [key] = abundance [key]

      norm = 0.
#      y_e = 0.

# Normalize abundances by looping over species
    for key in mean_abundance: # loop over species 
      mean_abundance [key] = mean_abundance [key] / total_particles
#      Z = proton [key]
#      A = baryon [key]
#      N = A - Z
#      y_e = y_e + mean_abundance [key] * Z / A
#      if (mean_abundance [key] > 0.01):
#        print key, " ", mean_abundance [key], " ", Z, " ", A
      norm += mean_abundance [key]

    if (abs (norm - 1.) > 0.01):
      print "Warning: Abundances not normalized to within 1%."

    calcium40 = mean_abundance ['ca40']
    calcium44 = mean_abundance ['ca44']
    calcium48 = mean_abundance ['ca48']

    cr50 = mean_abundance ['cr50']
    cr52 = mean_abundance ['cr52']
    cr53 = mean_abundance ['cr53']
    cr54 = mean_abundance ['cr54']

    chromium = cr50 + cr52 + cr53 + cr54
  
    fe54 = mean_abundance ['fe54']
    fe56 = mean_abundance ['fe56']
    fe57 = mean_abundance ['fe57']
    fe58 = mean_abundance ['fe58']

    iron = fe54 + fe56 + fe57 + fe58

    crtofe = chromium / iron

    calcium = calcium40 + calcium44 + calcium48

    sulfur32 = mean_abundance ['s32']
    sulfur34 = mean_abundance ['s34']

    sulfur = sulfur32 + sulfur34

    catos = calcium / sulfur

    chain55 = mean_abundance ['mn55']
    chain56 = mean_abundance ['fe56']
    chain57 = mean_abundance ['fe57']

# Output ca48 abundance, 55 chain, 56 chain, 57 chain, y_e
    f.write (filename + ": \n")

    f.write (str (crtofe) + " " + str (catos) +  \
       " " +  str (chain55) + " " + str (chain56) + " " + \
        str (chain57) + "\n" )

#    print chain55 / chain56
#    print chain55 / chain57

#    print 'fe55/co57 = ', mean_abundance ['fe55'] / mean_abundance ['co57']
#    print 'ti44 =', mean_abundance ['ti44']
#    print 'v49 =', mean_abundance ['v49']
#    print 'ni55 = ', mean_abundance ['ni55']
#    print 'co55 = ', mean_abundance ['co55']
#    print 'fe55 = ', mean_abundance ['fe55']
#    print 'co56 = ', mean_abundance ['co56']
   
#    print '55chain = ', chain55
#    print '56chain = ', chain56
#    print '57chain = ', chain57
#    print '57chain/56chain = ', chain57 / chain56
#    print '55chain/56chain = ', chain55 / chain56
#    print '55chain/57chain = ', chain55 / chain57

  else: # don't process other files 
    continue

#for key in sorted (mean_abundance, key = mean_abundance.get, reverse=True):
#   f.write (key + " " + str (mean_abundance [key]) + "\n")

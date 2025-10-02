suly=float(input("Adja meg a testsúlyt kg-ban:"))
magassag=float(input("Adja meg a magasságot cm-ben:"))

bmi=suly / ((magassag/100)**2)
kerek=round(bmi,2)

print("A testömeg index: ", kerek)
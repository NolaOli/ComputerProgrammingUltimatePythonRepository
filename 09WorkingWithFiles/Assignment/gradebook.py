import csv
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

f = open("09WorkingWithFiles/data/gradebook_data.csv", "r")
reader = csv.reader(f)
Acount = 0
Bcount = 0
Ccount = 0
Dcount= 0
Fcount = 0
for row in reader:
    name, gradelevel, percent = row
    percent = int(percent)
    print(percent)
    if percent>=90:
        Acount = Acount + 1
    elif percent<90 and percent>=80:
        Bcount = Bcount + 1
    elif percent<80 and percent>=70:
        Ccount = Ccount + 1
    elif percent<70 and percent>=60:
        Dcount = Dcount + 1
    else:
        Fcount = Fcount + 1

print("Amount of A's", Acount)
print("Amount of B's", Bcount)
print("Amount of C's", Ccount)
print("Amount of D's", Dcount)
print("Amount of F's", Fcount)
f.close()
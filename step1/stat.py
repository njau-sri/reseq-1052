import sys

MAF_MIN = float(sys.argv[1])
MIS_MAX = float(sys.argv[2])
HET_MAX = float(sys.argv[3])

f1 = open("plink.frq")
f2 = open("plink.lmiss")
f3 = open("plink.hwe")

f1.readline()
f2.readline()
f3.readline()

n = 0

for line1 in f1:
    line2 = f2.next()
    line3 = f3.next()
    v1 = line1.split()
    v2 = line2.split()
    v3 = line3.split()

    maf = 0.0 if v1[4] == "NA" else float(v1[4])
    if maf < MAF_MIN:
        continue

    mis = float(v2[4])
    if mis > MIS_MAX:
        continue

    het = float(v3[6])
    if het > HET_MAX:
        continue

    n += 1

print n

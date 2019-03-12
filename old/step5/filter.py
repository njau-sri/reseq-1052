
MAF_MIN = 0.01
MIS_MAX = 0.2
HET_MAX = 0.1

f1 = open("plink.frq")
f2 = open("plink.lmiss")
f3 = open("plink.hwe")
fout = open("filter.maf.mis.het.txt","w")

f1.readline()
f2.readline()
f3.readline()

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

    fout.write(v1[1])
    fout.write("\n")

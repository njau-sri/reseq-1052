
N = 1052
MAF_MIN = 0.01
MIS_MAX = 0.1
HET_MAX = 0.1

f1 = open("out.frq")
f2 = open("out.hwe")
fout = open("filter.maf.mis.het.txt","w")

f1.readline()
f2.readline()

for line1 in f1:
    line2 = f2.next()
    v1 = line1.split()
    v2 = line2.split()

    maf = min(float(v1[4]),float(v1[5]))
    if maf < MAF_MIN:
        continue

    mis = 1.0 - float(v1[3]) / (N*2)
    if mis > MIS_MAX:
        continue

    w = v2[2].split("/")
    het = float(w[1]) / N
    if het > HET_MAX:
        continue

    fout.write(v1[0])
    fout.write("\t")
    fout.write(v1[1])
    fout.write("\n")

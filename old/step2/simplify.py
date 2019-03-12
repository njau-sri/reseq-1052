import sys

ifs = open(sys.argv[1])
ofs = open(sys.argv[2],"w")

ofs.write(ifs.readline().strip())
ofs.write("\n")

for line in ifs:
    if line.startswith("#CHROM"):
        ofs.write(line.strip())
        ofs.write("\n")
        break

for line in ifs:
    v = line.split()
    if v[0].startswith("scaffold"):
        continue
    if len(v[4]) != 1:
        continue
    v[2] = v[0] + "_" + v[1]
    v[0] = str(int(v[0].replace("Chr","")))
    v[5] = "."
    v[6] = "."
    v[7] = "."
    v[8] = "GT"
    for i in range(9,len(v)):
        v[i] = v[i].split(":",1)[0]
    ofs.write("\t".join(v))
    ofs.write("\n")

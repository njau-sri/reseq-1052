import sys

if len(sys.argv) < 4:
    print "subset.py snp.vcf samples.txt out.vcf"
    raise IOError

f1 = open(sys.argv[1])
f2 = open(sys.argv[2])
fout = open(sys.argv[3],"w")

ind = []
for line in f2:
    ind += line.split()

for line in f1:
    if line.startswith("##fileformat"):
        fout.write(line.strip())
        fout.write("\n")
    elif line.startswith("#CHROM"):
        head = line.split()
        break

idx = range(9) + [head.index(e) for e in ind]
fout.write("\t".join(head[i] for i in idx))
fout.write("\n")

for line in f1:
    v = line.split()
    fout.write("\t".join(v[i] for i in idx))
    fout.write("\n")

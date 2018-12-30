
vcfin1 = "common.433.recode.reheader.vcf"
vcfin2 = "common.619.recode.vcf"
vcfout = "merge.1052.snp.vcf"

f1 = open(vcfin1)
f2 = open(vcfin2)
fout = open(vcfout,"w")

fout.write(f1.readline().strip())
fout.write("\n")
f2.readline()

for line1 in f1:
    line2 = f2.next()
    v1 = line1.split(None,5)
    v2 = line2.split(None,9)
    if v1[:5] != v2[:5]:
        continue
    fout.write(line1.strip())
    fout.write("\t")
    fout.write(v2[9].strip())
    fout.write("\n")

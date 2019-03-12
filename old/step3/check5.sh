#!/bin/bash

## QSUB OPTIONS
#$ -cwd
#$ -j y
#$ -S /bin/bash
#$ -l mem_free=4G

## BSUB OPTIONS
#BSUB -n 4
#BSUB -e %J.err
#BSUB -o %J.out

/gss1/app/python-2.7.9/bin/python subset.py merge.1052.snp.vcf subset.AQ.txt AQ246.snp.vcf

/gss1/app/python-2.7.9/bin/python subset.py merge.1052.snp.vcf subset.CY.txt CY560.snp.vcf

/gss1/app/python-2.7.9/bin/python subset.py merge.1052.snp.vcf subset.GZ.txt GZ246.snp.vcf

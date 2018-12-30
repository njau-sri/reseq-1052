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

plink-1.90b6.7 --vcf ALL.snp.filter.vcf --snps-only --freq --missing --hardy --allow-extra-chr \
--chr Chr01,Chr02,Chr03,Chr04,Chr05,Chr06,Chr07,Chr08,Chr09,Chr10,Chr11,Chr12,Chr13,Chr14,Chr15,Chr16,Chr17,Chr18,Chr19,Chr20

/gss1/app/python-2.7.9/bin/python stat.py 0.01 0.1 0.1
/gss1/app/python-2.7.9/bin/python stat.py 0.01 0.1 0.2
/gss1/app/python-2.7.9/bin/python stat.py 0.01 0.2 0.1
/gss1/app/python-2.7.9/bin/python stat.py 0.01 0.2 0.2

/gss1/app/python-2.7.9/bin/python stat.py 0.05 0.1 0.1
/gss1/app/python-2.7.9/bin/python stat.py 0.05 0.1 0.2
/gss1/app/python-2.7.9/bin/python stat.py 0.05 0.2 0.1
/gss1/app/python-2.7.9/bin/python stat.py 0.05 0.2 0.2

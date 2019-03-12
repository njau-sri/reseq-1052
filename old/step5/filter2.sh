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

/gss1/app/python-2.7.9/bin/python filter.py

vcftools-0.1.17 --vcf CY560.snp.vcf --snps filter.maf.mis.het.txt --recode --out final.CY560.snp

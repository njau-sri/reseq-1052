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

/gss1/app/python-2.7.9/bin/python simplify.py 433/ALL.snp.filter.vcf simplify.433.vcf

/gss1/app/python-2.7.9/bin/python simplify.py 619/ALL.snp.filter.vcf simplify.619.vcf

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

vcftools-0.1.17 --vcf simplify.433.vcf --positions common.sites.txt --recode --out common.433

vcftools-0.1.17 --vcf simplify.619.vcf --positions common.sites.txt --recode --out common.619

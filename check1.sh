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

vcftools-0.1.17 --vcf simplify.433.vcf --diff simplify.619.vcf --diff-site

awk '{if($4=="B"&&$7==$8)print}' out.diff.sites_in_files | cut -f 1,2 > common.sites.txt

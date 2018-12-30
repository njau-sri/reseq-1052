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

bcftools reheader --samples reheader.samples.433.txt --output common.433.recode.reheader.vcf common.433.recode.vcf

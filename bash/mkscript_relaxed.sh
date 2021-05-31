#!/bin/bash

export instdir=$(cat instdir.tmp)/

cp ${instdir}rscripts/firsthalf_testsnps.R tmp/scriptinthemaking.tmp

echo branch samples:
for i in $(cat tmp/branchsamples_1.tmp)
do
    echo $i
    echo -e "\t \t & genotype_numb_df\$___XXXXXX${i}___XXXXXX[y]==1" >> tmp/scriptinthemaking.tmp
done

echo
echo outgroup samples:
for i in $(cat tmp/outgroupsamples_1.tmp)
do
    echo $i
    echo  -e "\t \t & genotype_numb_df\$___XXXXXX${i}___XXXXXX[y]==0 | genotype_numb_df\$___XXXXXX${i}___XXXXXX[y]==___XXXXXXX___XXXXXX" >> tmp/scriptinthemaking.tmp
done

sed -i 's/___XXXXXX/"/g' tmp/scriptinthemaking.tmp

cat \
tmp/scriptinthemaking.tmp \
${instdir}rscripts/secondhalf_testsnps.R \
> ${instdir}rscripts/final_testsnps.R

sed -i \
"s/MULTIVCF/$(cat tmp/vcf.tmp)/g" \
${instdir}rscripts/final_testsnps.R

cp tmp/scriptinthemaking.tmp outscr1
cp ${instdir}rscripts/final_testsnps.R outscr2

Rscript $(cat instdir.tmp)/rscripts/final_testsnps.R
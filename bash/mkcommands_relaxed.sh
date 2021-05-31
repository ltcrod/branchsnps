#!/bin/bash 

x=1
export x=1
export times=$(wc -l $(cat tmp/list.tmp) | awk '{print $1}')

cp $(cat tmp/list.tmp) tmplist.tmp

for i in $(seq 1 ${times})
    do
    echo  branch number: \t ${i} / ${times}

    export bras=$(head -${i} tmplist.tmp | tail -1 | awk '{print $1}' | sed 's/\,/\ /g')
    echo branch samples: $bras
    export ous=$(head -${i} tmplist.tmp | tail -1 | awk '{print $2}' | sed 's/\,/\ /g')
    echo outgroupsamples: $ous

    python $(cat instdir.tmp)/define.py \
        -v $(cat tmp/vcf.tmp) \
        -b ${bras} \
        -o ${ous} \
        -m relaxed

mv mappedsnps.txt mappedsnps_line${i}

done

for i in $(ls mappedsnps_line* | sed 's/mappedsnps_//g')
do
    echo $i >> out_allbranches
    cat mappedsnps_${i} >> out_allbranches
    echo ----------------------------- >> out_allbranches
done

rm mappedsnps_line1
rm mappedsnps_line3
rm mappedsnps_line2
rm *.tmp 
rm tmp/* 
rm -r tmp
rm outscr*
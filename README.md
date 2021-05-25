# branchsnps

A simple script to determine the SNPs defining a phylogenetic branch in a uniparental phylogenetic tree and prints them to stdout.

## Requirements
* [python](https://www.python.org/)
* [R language](https://www.r-project.org/) 


## Usage
```
  -b BRANCHSAMPLES, --branch-samples BRANCHSAMPLES
                        space separated list of the samples of the branch of
                        interest [REQUIRED]
  -o OUTGROUPSAMPLES, --outgroups OUTGROUPSAMPLES
                        space separated list of the samples used as outgroups
                        to identify the SNPs defining the branch of interest
                        (tip: the best choice is a sister clade or star*
                        samples) [REQUIRED]
  -v VCF, --vcf VCF     multiVCF file containing all the samples specified
                        [REQUIRED]
  -m {relaxed,conservative}, --mode {relaxed,conservative}
                        conservative: lists only SNPs that are REF in all the
                        outgroup samples; relaxed: lists all the SNPs that are
                        REF or MISS in the outgroup samples [YET TO BE IMPLEMENTED, default: conservative]
```

## Functioning

![branch](https://github.com/ltcrod/branchsnps/blob/main/pic/treebranch.png)

To determine the SNPs defining branch 1: 
```
python define.py -b A B -o C D E
```
This will print all the positions shared exclusively by the "A" and "B" taxa. 

In an ideal scenario without missing data , reversions or recurrent mutations specifying only "C" or "D" as outgroups taxon would be enough to achieve this goal. 

In this example, specifying only "E" as outgroup taxon instead of "C", "D", and "E" would result in the identification of the mutations of both the branches 1 and 3. 
```
python define.py -b A B -o E
```


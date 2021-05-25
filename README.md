# branchsnps

A simple script to determine the SNPs defining a phylogenetic branch in a uniparental phylogenetic tree

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


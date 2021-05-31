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
  -v VCF, --vcf VCF     input multiVCF file containing all the samples specified
                        [REQUIRED]
  -m {relaxed,conservative}, --mode {relaxed,conservative}
                        conservative: lists only SNPs that are REF in all the
                        outgroup samples; relaxed: lists all the SNPs that are
                        REF or MISS in the outgroup samples [default: conservative]
  -l LISTSAMP, --list LISTSAMP
                        specify a file with a list for both outgroups samples
                        and samples of the branch of interest; the table must
                        contain two tab delimited columns, the first for the
                        samples in the branch of interest and the second for
                        the outgroups; samples should be separated by a comma
                        and no space. If this option is specified, both -o and
                        -b will be ignored. See below for the input format
                        
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

#### Input table example

Outgroups always on the right.

![inputtable](https://github.com/ltcrod/branchsnps/blob/main/pic/table.png)





### Future improvements 

* a clean output for the "-l" option

### Tips

* If samples are not merged, a multiVCF can be produced with [bcftools merge](http://samtools.github.io/bcftools/bcftools.html#merge)
* This script is independent from nwk phylogenies. This allows to find shared mutations in all kind of VCF files, and identify new shared mutations in resequenced already-classified samples. Nonetheless, scripts to map SNPs from VCFs to nwk  trees already exist, like [Richard Durbin](https://github.com/richarddurbin)'s [phynder](https://github.com/richarddurbin/phynder).

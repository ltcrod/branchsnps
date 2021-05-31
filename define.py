import os
import argparse

parser= argparse.ArgumentParser(description='...')
parser.add_argument("-b", "--branch-samples",nargs="+", required= False, dest= 'branchsamples', default="peanut",
                     help= "space separated list of the samples of the branch of interest [REQUIRED]"
                    )
parser.add_argument("-o", "--outgroups", required= False, nargs="+", dest= 'outgroupsamples', default="peanut",
                     help= "space separated list of the samples used as outgroups to identify the SNPs defining the branch of interest (tip: the best choice is a sister clade or star* samples) [REQUIRED]"
                    )
parser.add_argument("-v", "--vcf", required= True, dest= 'vcf',
                     help= "multiVCF file containing all the samples specified [REQUIRED]"
                    )
parser.add_argument("-m", "--mode", required= False, dest= 'mode', default='conservative', choices=['relaxed', 'conservative'],
                     help= "conservative: lists only SNPs that are REF in all the outgroup samples; relaxed: lists all the SNPs that are REF or MISS in the outgroup samples [DEFAULT: conservative]"
                    )
parser.add_argument("-l", "--list", required= False, dest= 'listsamp', default='peanut',
                     help= "specify a file with a list for both outgroups samples and samples of the branch of interest; the table must contain two tab delimited columns, the first for the samples in the branch of interest and the second for the outgroups; samples should be separated by a comma and no space. If this option is specified, both -o and -b will be ignored"
                    )


args = parser.parse_args()

os.system("mkdir tmp")

#scriptdir
realdir=(os.path.dirname(__file__))
rd = open("instdir.tmp", "w")
rd.write(realdir)
rd.close()



#vcf name
vcf = args.vcf
vcfs = open("tmp/vcf.tmp", "w")
vcfs.write(vcf)
vcfs.close()

mode = args.mode
relcon = open("tmp/mode.tmp", "w")
relcon.write(mode)
relcon.close()

#list (if any)
listsamps = args.listsamp
lst = open("tmp/list.tmp", "w")
lst.write(listsamps)
lst.close()

listob = args.listsamp
bs = args.branchsamples
ous = args.outgroupsamples

##############################################################################
# launch chosen command

if bs == "peanut" and ous == "peanut" and listob == "peanut":
    print("no arguments specified, specify [-o and -b] or -l")

elif bs != "peanut" and ous != "peanut" and listob == "peanut":
    #branchsamples list
    for elem in bs:
        bras = open("branchsamples.txt", "a")
        bras.write(elem+"\n")
        bras.close()
    os.system("mv branchsamples.txt tmp/branchsamples_1.tmp")

    #outgroupsamples list
    for elem in ous:
        outs = open("outgroupsamples.txt", "a")
        outs.write(elem+"\n")
        outs.close()
    os.system("mv outgroupsamples.txt tmp/outgroupsamples_1.tmp")
    if mode == "conservative":
        os.system("bash $(cat instdir.tmp)/bash/mkscript.sh")
    elif mode == "relaxed":
        os.system("bash $(cat instdir.tmp)/bash/mkscript_relaxed.sh")
    os.system("sed 's/\"//g' mappedsnps.tmp > mappedsnps.txt")



elif listob != "tytiretupatulae":
    if mode == "conservative":
        os.system("bash $(cat instdir.tmp)/bash/mkcommands.sh")
    elif mode == "relaxed":
        os.system("bash $(cat instdir.tmp)/bash/mkcommands_relaxed.sh")

else: 
    os.system("python $(cat instdir.tmp)/define.py -h")



##############################################################################

if listob == "tytiretupatulae":
    os.system("rm *.tmp tmp/* ; rm -r tmp ; rm outscr* ")
else: 
    print
# os.system("sed -e 's/\n/\,\ /g' mappedsnps.txt > test")
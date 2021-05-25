import os
import argparse
import shutil

parser= argparse.ArgumentParser(description='...')
parser.add_argument("-b", "--branch-samples",nargs="+", required= True, dest= 'branchsamples',
                     help= "space separated list of the samples of the branch of interest [REQUIRED]"
                    )
parser.add_argument("-o", "--outgroups", required= True, nargs="+", dest= 'outgroupsamples',
                     help= "space separated list of the samples used as outgroups to identify the SNPs defining the branch of interest (tip: the best choice is a sister clade or star* samples) [REQUIRED]"
                    )
parser.add_argument("-v", "--vcf", required= True, dest= 'vcf',
                     help= "multiVCF file containing all the samples specified [REQUIRED]"
                    )
parser.add_argument("-m", "--mode", required= False, dest= 'mode', default='conservative', choices=['relaxed', 'conservative'],
                     help= "conservative: lists only SNPs that are REF in all the outgroup samples; relaxed: lists all the SNPs that are REF or MISS in the outgroup samples [DEFAULT: conservative]"
                    )

args = parser.parse_args()

os.system("mkdir tmp")

#scriptdir
realdir=(os.path.dirname(__file__))
rd = open("instdir.tmp", "w")
rd.write(realdir)
rd.close()

#branchsamples list
bs = args.branchsamples
for elem in bs:
    bras = open("branchsamples.txt", "a")
    bras.write(elem+"\n")
    bras.close()
os.system("mv branchsamples.txt tmp/branchsamples_1.tmp")


#outgroupsamples list
ous = args.outgroupsamples
for elem in ous:
    outs = open("outgroupsamples.txt", "a")
    outs.write(elem+"\n")
    outs.close()
os.system("mv outgroupsamples.txt tmp/outgroupsamples_1.tmp")

#vcf name
vcf = args.vcf
vcfs = open("tmp/vcf.tmp", "w")
vcfs.write(vcf)
vcfs.close()



os.system("bash $(cat instdir.tmp)/bash/mkscript.sh")
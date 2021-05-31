# Find shared and not-shared snps by editing the last for-if cycle
#first part == vcf2meg

# Load the library
library(vcfR)
library(dplyr)
library(tidyr)


#setwd and load file with vcfR
# main_dir = "C:/Users/lucat/Desktop/Lab/MEGA_COSE/arias"
# setwd(main_dir)
file_vcf <-  read.vcfR("MULTIVCF")


# Call only the genotype
genotype_file_numb.tmp1 <- extract.gt(file_vcf, return.alleles = F)

genotype_file_allele.tmp1 <- extract.gt(file_vcf, return.alleles = T)


# Create the tables easy to read
table_gt <- vcfR2tidy(file_vcf)


# Remove all the SNPs that in the REF have more than one charachter (MNP)
SNP_ref_list <- unlist(lapply(table_gt$fix$REF, function(x) nchar(x)==1))
SNP_ref_list_2 <- unlist(lapply(table_gt$fix$ALT, function(x) nchar(x)==1))
SNP_ref_list[which(!SNP_ref_list_2)] <- FALSE

genotype_file_numb.tmp2 <- genotype_file_numb.tmp1[SNP_ref_list,]
genotype_file_allele.tmp2 <- genotype_file_allele.tmp1[SNP_ref_list,]



# Grep and keep all the snps that have at least one sample as variant, all the other will be removed
list_snp_cond <- unlist(lapply(apply(genotype_file_numb.tmp2, 1, function(x) grep("1",x)), function(z) length(z)!=0))


genotype_file_allele <- genotype_file_allele.tmp2[list_snp_cond,]
genotype_file_allele[which(is.na(genotype_file_allele))] <- "X"
genotype_file_allele[genotype_file_allele=="."] <- "X"

genotype_file_numb.tmp2[which(is.na(genotype_file_numb.tmp2))] <- "X"
genotype_file_numb.tmp2[genotype_file_numb.tmp2=="."] <- "X"

#import genotypes as dataframes
#numb_df is only useful for checks
genotype_numb_df <- as.data.frame(genotype_file_numb.tmp2)
genotype_allelic_df <- as.data.frame(genotype_file_allele)


#NEWSPLIT check

for (y in (row.names(genotype_numb_df))){
    if (1==1

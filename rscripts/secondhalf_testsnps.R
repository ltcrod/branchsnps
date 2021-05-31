    ){
        print(y)
        write.table(y, file="mappedsnps.tmp", sep=", ", row.names = FALSE, col.names = FALSE, append = TRUE)
    }
}
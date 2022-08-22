# NCEI Data Utilities
Python command utilities to manipulate NCEI data from the National Weather Service

### Global Historical Climatology Network

Data Search  
https://www.ncei.noaa.gov/access/search/data-search/daily-summaries

Direct Downlod  
https://www1.ncdc.noaa.gov/pub/data/ghcn/daily/

FTP Server  
ftp://ftp.ncdc.noaa.gov/pub/data/ghcn/daily

# Load data into MySql

### Convert txt to csv
convert_countries_csv(source_path, target_path, delete_source)

### Load data into table
LOAD DATA INFILE '/path/to/ghcnd-countries.csv' INTO TABLE GHCN.countries;

must disable --secure-file-priv variable in my.cnf to 'Load Data Infile'
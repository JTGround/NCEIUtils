# Description
This repository provides a basic framework to access and
manipulate some of the stores of environmental data hosted by the National Centers for Environmental
Information. The NCEI is part of the National Oceanic and Atmospheric Administration 
and provides an archive of years of environmental data.   

# Data Repositories
### Global Historical Climatology Network

```
from ghcn.io import read_stations

# Read from txt file - into list of stations
stations_list = read_stations('./data/ghcnd-stations.txt')

# Read from txt file - into pandas dataframe
stations_dataframe = read_stations_df('./data/ghcnd-stations.txt')
```

Web Search  
https://www.ncei.noaa.gov/access/search/data-search/daily-summaries  
  
Direct Download  
https://www1.ncdc.noaa.gov/pub/data/ghcn/daily/

FTP Server  
ftp://ftp.ncdc.noaa.gov/pub/data/ghcn/daily

# Load data into MySql

### Convert txt to csv
convert_countries_csv(source_path, target_path, delete_source)

### Load data into table
LOAD DATA INFILE '/path/to/ghcnd-countries.csv' INTO TABLE GHCN.countries;

must disable --secure-file-priv variable in my.cnf to 'Load Data Infile'
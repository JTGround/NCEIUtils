
CREATE TABLE states (
    code CHAR(2) NOT NULL,
    name VARCHAR(47) UNIQUE NOT NULL,
    PRIMARY KEY(code)
) ENGINE=INNODB;

CREATE TABLE countries (
    code CHAR(2) NOT NULL,
    name VARCHAR(61) UNIQUE NOT NULL,
    PRIMARY KEY(code)
) ENGINE=INNODB;

CREATE TABLE stations (
    id CHAR(11) NOT NULL,
    lat DECIMAL(6,4) NOT NULL,
    lon DECIMAL (7,4) NOT NULL,
    elevation DECIMAL(5,1),
    state CHAR(2),
    name VARCHAR(30) NOT NULL,
    gsn_flag BOOLEAN NOT NULL,
    hcn_crn_flag ENUM('HCN','CRN'),
    wmo_id DECIMAL(5,0),
    PRIMARY KEY(id),
    CONSTRAINT cs_stations_lat_gt CHECK (lat >= -90.0),
    CONSTRAINT cs_stations_lat_lt CHECK (lat <= 90.0),
    CONSTRAINT cs_stations_lon_gt CHECK (lat >= -180.0),
    CONSTRAINT cs_stations_lon_lt CHECK (lat <= 180.0)
) ENGINE=INNODB;

CREATE TABLE elements (
    id INTEGER AUTO_INCREMENT NOT NULL,
    name CHAR(4) UNIQUE NOT NULL,
    PRIMARY KEY(id)
) ENGINE=INNODB;

CREATE TABLE inventory (
    id INTEGER AUTO_INCREMENT NOT NULL,
    station_id CHAR(11) NOT NULL,
    lat DECIMAL(6,4) NOT NULL,
    lon DECIMAL (7,4) NOT NULL,
    element_id INTEGER NOT NULL,
    first_year INTEGER NOT NULL,
    last_year INTEGER NOT NULL,
    PRIMARY KEY(id),
    INDEX (station_id),
    INDEX (element_id),
    CONSTRAINT cs_inventory_lat_gt CHECK (lat >= -90.0),
    CONSTRAINT cs_inventory_lat_lt CHECK (lat <= 90.0),
    CONSTRAINT cs_inventory_lon_gt CHECK (lat >= -180.0),
    CONSTRAINT cs_inventory_lon_lt CHECK (lat <= 180.0)
) ENGINE=INNODB;

ALTER TABLE inventory
    ADD CONSTRAINT fk_inventory_stations
    FOREIGN KEY (station_id) REFERENCES stations(id);

ALTER TABLE inventory
    ADD CONSTRAINT fk_inventory_elements
    FOREIGN KEY (element_id) REFERENCES elements(id);

CREATE TABLE daily_records (
    id INTEGER AUTO_INCREMENT NOT NULL,
    station_id CHAR(11) NOT NULL,
    `date` DATE NOT NULL,
    element_id INTEGER NOT NULL,
    `value` INTEGER NOT NULL,
    mflag CHAR(1),
    qflag CHAR(1),
    sflag CHAR(1),
    PRIMARY KEY(id),
    INDEX (station_id),
    INDEX (element_id)
) ENGINE=INNODB;

ALTER TABLE daily_records
    ADD CONSTRAINT fk_daily_records_stations
    FOREIGN KEY (station_id) REFERENCES stations(id);

ALTER TABLE daily_records
    ADD CONSTRAINT fk_daily_records_elements
    FOREIGN KEY (element_id) REFERENCES elements(id);
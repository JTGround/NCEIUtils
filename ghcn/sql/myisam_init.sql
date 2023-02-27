
CREATE TABLE states (
    code CHAR(2) NOT NULL,
    name VARCHAR(47) UNIQUE NOT NULL,
    PRIMARY KEY(code)
) ENGINE=MYISAM;

CREATE TABLE countries (
    code CHAR(2) NOT NULL,
    name VARCHAR(61) UNIQUE NOT NULL,
    PRIMARY KEY(code)
) ENGINE=MYISAM;

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
    PRIMARY KEY(id)
) ENGINE=MYISAM;

CREATE TABLE inventory (
    id INTEGER AUTO_INCREMENT NOT NULL,
    station_id CHAR(11) NOT NULL,
    lat DECIMAL(6,4) NOT NULL,
    lon DECIMAL (7,4) NOT NULL,
    element CHAR(4) NOT NULL,
    first_year INTEGER NOT NULL,
    last_year INTEGER NOT NULL,
    PRIMARY KEY(id),
    INDEX (station_id),
    INDEX (element)
) ENGINE=MYISAM;

CREATE TABLE daily_records (
    id INTEGER AUTO_INCREMENT NOT NULL,
    station_id CHAR(11) NOT NULL,
    record_date DATE NOT NULL,
    element CHAR(4) NOT NULL,
    record_value INTEGER NOT NULL,
    mflag CHAR(1),
    qflag CHAR(1),
    sflag CHAR(1),
    PRIMARY KEY(id),
    INDEX (station_id),
    INDEX (record_date),
    INDEX (element)
) ENGINE=MYISAM;





------------------------------
Variable   Columns   Type
------------------------------
ID            1-11   Character
YEAR         12-15   Integer
MONTH        16-17   Integer
ELEMENT      18-21   Character
VALUE1       22-26   Integer
MFLAG1       27-27   Character
QFLAG1       28-28   Character
SFLAG1       29-29   Character
VALUE2       30-34   Integer
MFLAG2       35-35   Character
QFLAG2       36-36   Character
SFLAG2       37-37   Character
  .           .          .
  .           .          .
  .           .          .
VALUE31    262-266   Integer
MFLAG31    267-267   Character
QFLAG31    268-268   Character
SFLAG31    269-269   Character
------------------------------


DELIMITER //
CREATE PROCEDURE GetStationsByCountry(
	IN inCountryValue VARCHAR(61)
)
BEGIN
	SELECT stations.id, stations.lat, stations.lon, stations.elevation,
        countries.name AS country_name, states.name AS state_name,
        stations.name AS station_name, stations.gsn_flag,
        stations.hcn_crn_flag, stations.wmo_id
    FROM stations
    INNER JOIN countries ON countries.code = LEFT(stations.id, 2)
    LEFT JOIN states ON states.code = stations.state
    WHERE countries.code = inCountryValue OR countries.name = inCountryValue;
END //
DELIMITER ;


DELIMITER //
CREATE PROCEDURE GetStationsByState(
	IN inCountryValue VARCHAR(61),
	IN inStateValue VARCHAR(47)
)
BEGIN
	SELECT stations.id, stations.lat, stations.lon, stations.elevation,
        countries.name AS country_name, states.name AS state_name,
        stations.name AS station_name, stations.gsn_flag,
        stations.hcn_crn_flag, stations.wmo_id
    FROM stations
    INNER JOIN countries ON countries.code = LEFT(stations.id, 2)
    LEFT JOIN states ON states.code = stations.state
    WHERE (countries.code = inCountryValue OR countries.name = inCountryValue)
        AND (states.code = inStateValue OR states.name = inStateValue);
END //
DELIMITER ;


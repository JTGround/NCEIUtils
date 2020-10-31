from ghcn.types import State, Country, Station, ClimateNetwork


def parse_states(filepath):
    states = []

    reader = open(filepath, 'r')
    for line in reader:
        abbrev = line[:2]
        name = line[3:].rstrip()
        state = State(abbrev, name)
        states.append(state)
    return states


def parse_countries(filepath):
    countries = []

    reader = open(filepath, 'r')
    for line in reader:
        abbrev = line[:2]
        name = line[3:].rstrip()
        cty = Country(abbrev, name)
        countries.append(cty)
    return countries


def parse_stations(filepath):
    stations = []

    reader = open(filepath, 'r')
    for line in reader:
        station_id = line[0:11]
        lat = float(line[12:20])
        lon = float(line[21:30])
        elev = float(line[31:37])
        if elev == -999.9:
            elev = None
        state = line[38:40].strip()
        if not state:
            state = None
        name = line[40:70].strip()
        gsn = line[72:75].strip()
        if not gsn:
            gsn = None
        network = line[76:79].strip()
        network_enum = ClimateNetwork.NONE
        if network == "HCN":
            network_enum = ClimateNetwork.HCN
        elif network == "CRN":
            network_enum = ClimateNetwork.CRN
        else:
            network_enum.NONE
        wmo_id = line[81:85].strip()
        if not wmo_id:
            wmo_id = None
        station = Station(station_id, lat, lon, elev, state, name, gsn, network_enum, wmo_id)
        stations.append(station)
    return stations

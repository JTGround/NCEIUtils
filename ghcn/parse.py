from ghcn.types import State, Country, Station, ClimateNetwork, Inventory, StationSource, \
    StationSourceRanking


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
        name = line[41:71].strip()
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
        wmo_id = line[80:85].strip()
        if not wmo_id:
            wmo_id = None
        station = Station(station_id, lat, lon, elev, state, name, gsn, network_enum, wmo_id)
        stations.append(station)
    return stations


def parse_inventory(filepath):
    inventories = []

    reader = open(filepath, 'r')
    for line in reader:
        station_id = line[0:11]
        lat = float(line[12:20])
        lon = float(line[21:30])
        element = line[31:35]
        first_year = int(line[36:40])
        last_year = int(line[41:45])

        inventory = Inventory(station_id, lat, lon, element, first_year, last_year)
        inventories.append(inventory)
    return inventories


def parse_station_sources(filepath):
    stations = []

    reader = open(filepath, 'r')
    for line in reader:
        station_id = line[0:11]
        num_sources = int(line[12:14])

        sources = []
        for src in range(0, num_sources):
            base = 15 + (src * 14)
            rank = src + 1
            source_code = line[base:base + 1]
            source_id = line[base + 2:base + 13]
            sources.append(StationSource(rank, source_code, source_id))

        station = StationSourceRanking(station_id, sources)
        stations.append(station)
    return stations

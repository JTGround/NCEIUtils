from ghcn.types import State, Country, Station, ClimateNetwork, Inventory, StationSource, \
    StationSourceRanking, DailyValue, ElementMonthlyRecord
import os


def parse_states(source_path):
    states = []

    if not os.path.exists(source_path):
        print('File (path=' + source_path + ') does not exist.')
        return states

    file = open(source_path, 'r')
    try:
        for line in file:
            abbrev = line[:2]
            name = line[3:].rstrip()
            state = State(abbrev, name)
            states.append(state)
    finally:
        file.close()

    return states


def parse_countries(source_path):
    countries = []

    if not os.path.exists(source_path):
        print('File (path=' + source_path + ') does not exist.')
        return countries

    file = open(source_path, 'r')
    try:
        for line in file:
            abbrev = line[:2]
            name = line[3:].rstrip()
            cty = Country(abbrev, name)
            countries.append(cty)
    finally:
        file.close()
    return countries


def parse_stations(source_path):
    stations = []

    if not os.path.exists(source_path):
        print('File (path=' + source_path + ') does not exist.')
        return stations

    file = open(source_path, 'r')
    try:
        for line in file:
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
    finally:
        file.close()
    return stations


def parse_inventory(source_path):
    inventories = []

    if not os.path.exists(source_path):
        print('File (path=' + source_path + ') does not exist.')
        return inventories

    file = open(source_path, 'r')
    try:
        for line in file:
            station_id = line[0:11]
            lat = float(line[12:20])
            lon = float(line[21:30])
            element = line[31:35]
            first_year = int(line[36:40])
            last_year = int(line[41:45])

            inventory = Inventory(station_id, lat, lon, element, first_year, last_year)
            inventories.append(inventory)
    finally:
        file.close()
    return inventories


def parse_station_sources(source_path):
    stations = []

    if not os.path.exists(source_path):
        print('File (path=' + source_path + ') does not exist.')
        return stations

    file = open(source_path, 'r')
    try:
        for line in file:
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
    finally:
        file.close()
    return stations


def parse_dly(source_path):
    records = []

    if not os.path.exists(source_path):
        print('File (path=' + source_path + ') does not exist.')
        return records

    file = open(source_path, 'r')
    try:
        for line in file:
            station_id = line[0:11]
            year = int(line[11:15])
            month = int(line[15:17])
            element = line[17:21]

            values = []
            for index in range(0, 31):
                date = index + 1
                base = 21 + (index * 8)
                val = float(line[base: base + 5])
                if val == -9999:
                    val = None
                m_flag = line[base + 5: base + 6].strip()
                q_flag = line[base + 6: base + 7].strip()
                s_flag = line[base + 7: base + 8].strip()
                daily_value = DailyValue(val, date, m_flag, q_flag, s_flag)
                values.append(daily_value)
            monthly_record = ElementMonthlyRecord(station_id, year, month, element, values)
            records.append(monthly_record)
    finally:
        file.close()
    return records


def combine_dly(source_path, target_path, delete_source=False):

    if not os.path.exists(source_path):
        print('File (path=' + source_path + ') does not exist.')
        return

    # read in text lines from source file
    lines = []
    file_read = open(source_path, 'r')
    try:
        for line in file_read:
            lines.append(line)
    finally:
        file_read.close()

    # read in records from target file
    key_set = set()
    station_set = set()
    file_append_initial = open(target_path, 'r')
    try:
        for line in file_append_initial:
            station_id = line[0:11]
            station_set.add(station_id)

            line_key = line[0:21]
            key_set.add(line_key)
    finally:
        file_append_initial.close()

    # write text lines to target file
    file_append = open(target_path, 'a')
    try:
        for line in lines:
            # check if dup station
            station_id = line[0:11]
            key = line[0:21]
            if station_id not in station_set:
                file_append.write(line)
            else:
                if key not in key_set:
                    file_append.write(line)
    finally:
        file_append.close()

    # delete the source file, if required
    if delete_source:
        if os.path.exists(source_path):
            try:
                os.remove(source_path)
            except IOError:
                print("Unable to delete file: path=" + source_path)
        else:
            print("File (path=" + source_path + ") does not exist.")


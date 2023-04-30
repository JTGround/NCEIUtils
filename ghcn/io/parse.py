import pandas

from ghcn.types.stations import Station, Country, Inventory, StationSourceRanking, StationSource, State
from ghcn.types.records import ClimateNetwork, DailyValue, ElementMonthlyRecord
import os

station_cols = [(0, 11), (12, 20), (21, 30), (31, 37), (38, 40), (41, 71), (72, 75), (76, 79), (80, 85)]
station_names = ['station_id', 'lat', 'lon', 'elev', 'state', 'name', 'gsn', 'network', 'wmo_id']

country_cols = [(0, 2), (3, 64)]
country_names = ['code', 'name']

state_cols = [(0, 2), (3, 50)]
state_names = ['code', 'name']

invent_cols = [(0, 11), (12, 20), (21, 30), (31, 35), (36, 40), (41, 45)]
invent_names = ['station_id', 'lat', 'lon', 'element', 'first_year', 'last_year']


def read_stations(source_path):
    station_list = []

    if not os.path.exists(source_path):
        print('File (path=' + source_path + ') does not exist.')
        return station_list

    file = open(source_path, 'r')
    try:
        for line in file:
            station_id = line[station_cols[0][0]:station_cols[0][1]]
            lat = float(line[station_cols[1][0]:station_cols[1][1]])
            lon = float(line[station_cols[2][0]:station_cols[2][1]])
            elev = float(line[station_cols[3][0]:station_cols[3][1]])
            if elev == -999.9:
                elev = None
            state = line[station_cols[4][0]:station_cols[4][1]].strip()
            if not state:
                state = None
            name = line[station_cols[5][0]:station_cols[5][1]].strip()
            gsn = line[station_cols[6][0]:station_cols[6][1]].strip()
            if not gsn:
                gsn = None
            network = line[station_cols[7][0]:station_cols[7][1]].strip()
            network_enum = ClimateNetwork.NONE
            if network == "HCN":
                network_enum = ClimateNetwork.HCN
            elif network == "CRN":
                network_enum = ClimateNetwork.CRN
            wmo_id = line[station_cols[8][0]:station_cols[8][1]].strip()
            if not wmo_id:
                wmo_id = None
            station = Station(station_id, lat, lon, elev, state, name, gsn, network_enum, wmo_id)
            station_list.append(station)
    finally:
        file.close()
    return station_list


def read_stations_df(source_path):
    if not os.path.exists(source_path):
        print("File (path=" + source_path + ") does not exist.")
        return None

    df = pandas.read_fwf(source_path, skiprows=0, skipfooter=0, colspecs=station_cols, index_col=False,
                         names=station_names)
    return df


def read_countries(source_path):
    countries = []

    if not os.path.exists(source_path):
        print('File (path=' + source_path + ') does not exist.')
        return countries

    file = open(source_path, 'r')
    try:
        for line in file:
            code = line[country_cols[0][0]:country_cols[0][1]]
            name = line[country_cols[1][0]:country_cols[1][1]].rstrip()
            cty = Country(code, name)
            countries.append(cty)
    finally:
        file.close()
    return countries


def read_countries_df(source_path):
    if not os.path.exists(source_path):
        print("File (path=" + source_path + ") does not exist.")
        return None

    df = pandas.read_fwf(source_path, skiprows=0, skipfooter=0, colspecs=country_cols, index_col=False,
                         names=country_names)
    return df


def read_states(filepath):
    states = []

    if not os.path.exists(filepath):
        print('File (path=' + filepath + ') does not exist.')
        return states

    file = open(filepath, 'r')
    try:
        for line in file:
            code = line[state_cols[0][0]:state_cols[0][1]]
            name = line[state_cols[1][0]:state_cols[1][1]].rstrip()
            state = State(code, name)
            states.append(state)
    finally:
        file.close()

    return states


def read_states_df(filepath):
    if not os.path.exists(filepath):
        print('File (path=' + filepath + ') does not exist.')
        return None

    df = pandas.read_fwf(filepath, skiprows=0, skipfooter=0, colspecs=state_cols, index_col=False, names=state_names)
    return df


def read_inventory(source_path):
    inventories = []

    if not os.path.exists(source_path):
        print('File (path=' + source_path + ') does not exist.')
        return inventories

    file = open(source_path, 'r')
    try:
        for line in file:
            station_id = line[invent_cols[0][0]:invent_cols[0][1]]
            lat = float(line[invent_cols[1][0]:invent_cols[1][1]])
            lon = float(line[invent_cols[2][0]:invent_cols[2][1]])
            element = line[invent_cols[3][0]:invent_cols[3][1]]
            first_year = int(line[invent_cols[4][0]:invent_cols[4][1]])
            last_year = int(line[invent_cols[5][0]:invent_cols[5][1]])

            inventory = Inventory(station_id, lat, lon, element, first_year, last_year)
            inventories.append(inventory)
    finally:
        file.close()
    return inventories


def read_inventory_df(source_path):
    if not os.path.exists(source_path):
        print('File (path=' + source_path + ') does not exist.')
        return None

    df = pandas.read_fwf(source_path, skiprows=0, skipfooter=0, colspecs=invent_cols, index_col=False, names=invent_names)
    return df


def read_station_sources(source_path):
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

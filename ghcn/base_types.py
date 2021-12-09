from enum import Enum, unique


class State:
    def __init__(self, code, name):
        self.code = code
        self.name = name


class Country:
    def __init__(self, code, name):
        self.code = code
        self.name = name




class Inventory:
    def __init__(self, station_id, lat, lon, element, first_year, last_year):
        self.station_id = station_id
        self.lat = lat
        self.lon = lon
        self.element = element
        self.first_year = first_year
        self.last_year = last_year


class StationSourceRanking:
    def __init__(self, station_id, sources):
        self.station_id = station_id
        self.sources = sources


class StationSource:
    def __init__(self, rank, source_code, source_id):
        self.rank = rank
        self.source_code = source_code
        self.source_id = source_id


class ElementMonthlyRecord:
    def __init__(self, station_id, year, month, element, daily_values):
        self.station_id = station_id
        self.year = year
        self.month = month
        self.element = element
        self.daily_values = daily_values


class ElementDailyRecord:
    def __init__(self, station_id, year, month, date, element, val, m_flag, q_flag, s_flag):
        self.station_id = station_id
        self.year = year
        self.month = month
        self.date = date
        self.element = element
        self.val = val
        self.m_flag = m_flag
        self.q_flag = q_flag
        self.s_flag = s_flag


class DailyValue:
    def __init__(self, val, date, m_flag, q_flag, s_flag):
        self.val = val
        self.date = date
        self.m_flag = m_flag
        self.q_flag = q_flag
        self.s_flag = s_flag


class Station:
    def __init__(self, station_id, lat, lon, elev, state, name, gsn, network, wmo_id):
        self.station_id = station_id
        self.lat = lat
        self.lon = lon
        self.elev = elev
        self.state = state
        self.name = name
        self.gsn = gsn
        self.network = network
        self.wmo_id = wmo_id


@unique
class ClimateNetwork(Enum):
    NONE = "NONE"
    HCN = "HCN"
    CRN = "CRN"

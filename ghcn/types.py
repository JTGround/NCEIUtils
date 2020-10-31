from enum import Enum, unique


class State:
    def __init__(self, code, name):
        self.code = code
        self.name = name


class Country:
    def __init__(self, code, name):
        self.code = code
        self.name = name


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

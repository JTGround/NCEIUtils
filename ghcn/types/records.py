from enum import Enum, unique


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


@unique
class ClimateNetwork(Enum):
    NONE = "NONE"
    HCN = "HCN"
    CRN = "CRN"

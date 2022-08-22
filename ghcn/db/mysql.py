import mysql.connector
from mysql import connector


class MySqlReader:

    @staticmethod
    def insert_states(conn_config, states):

        conn = connector.connect(**conn_config)
        cursor = conn.cursor()

        for state in states:
            insert_sql = ("INSERT INTO states "
                          "(code, name) "
                          "VALUES (%(code)s, %(name)s)")

            insert_values = {
                'code': state.code,
                'name': state.name,
            }
            cursor.execute(insert_sql, insert_values)

        conn.commit()
        cursor.close()
        conn.close()

    @staticmethod
    def insert_countries(conn_config, countries):

        conn = connector.connect(**conn_config)
        cursor = conn.cursor()

        for country in countries:
            insert_sql = ("INSERT INTO countries "
                          "(code, name) "
                          "VALUES (%(code)s, %(name)s)")

            insert_values = {
                'code': country.code,
                'name': country.name,
            }
            cursor.execute(insert_sql, insert_values)

        conn.commit()
        cursor.close()
        conn.close()

    @staticmethod
    def insert_stations(conn_config, stations):

        conn = connector.connect(**conn_config)
        cursor = conn.cursor()

        for station in stations:
            insert_sql = ("INSERT INTO stations "
                          "(id, lat, lon, elevation, state, name, gsn_flag, hcn_crn_flag, wmo_id) "
                          "VALUES (%(id)s, %(lat)s, %(lon)s, %(elevation)s, %(state)s, %(name)s, %(gsn_flag)s, %(hcn_crn_flag)s, %(wmo_id)s)")

            gsn_flag_value = False
            if station.gsn is not None:
                gsn_flag_value = True

            hcn_crn_flag_value = station.network.value
            if hcn_crn_flag_value == 'NONE':
                hcn_crn_flag_value = None

            insert_values = {
                'id': station.station_id,
                'lat': station.lat,
                'lon': station.lon,
                'elevation': station.elev,
                'state': station.state,
                'name': station.name,
                'gsn_flag': gsn_flag_value,
                'hcn_crn_flag': hcn_crn_flag_value,
                'wmo_id': station.wmo_id,
            }
            cursor.execute(insert_sql, insert_values)
            conn.commit()

        cursor.close()
        conn.close()

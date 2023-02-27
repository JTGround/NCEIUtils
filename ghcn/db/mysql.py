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

        batch_size = 20
        for i in range(0, len(stations), batch_size):
            station_range = stations[i:i + batch_size]

            many_values = []
            for station in station_range:

                gsn_flag_value = False
                if station.gsn is not None:
                    gsn_flag_value = True

                hcn_crn_flag_value = station.network.value
                if hcn_crn_flag_value == 'NONE':
                    hcn_crn_flag_value = None

                insert_values = (
                    station.station_id,
                    station.lat,
                    station.lon,
                    station.elev,
                    station.state,
                    station.name,
                    gsn_flag_value,
                    hcn_crn_flag_value,
                    station.wmo_id,
                )
                many_values.append(insert_values)

            insert_sql = """INSERT INTO stations 
                          (id, lat, lon, elevation, state, name, gsn_flag, hcn_crn_flag, wmo_id)
                          VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s) """
            cursor.executemany(insert_sql, many_values)
            conn.commit()

        cursor.close()
        conn.close()

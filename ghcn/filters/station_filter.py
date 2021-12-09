from util.distance import calc_dist


def within_state(state):
    def in_state_name(station):
        return station.state == state
    return in_state_name


def within_elev(min_elev, max_elev):
    def within_elevation_station(station):
        if station.elev is None:
            return False
        return min_elev <= station.elev <= max_elev
    return within_elevation_station


def within_dist_lat_lon(lat, lon, dist):
    def within_dist_lat_lon_station(dist_station):
        return calc_dist(lat, lon, dist_station.lat, dist_station.lon) <= dist
    return within_dist_lat_lon_station


def within_dist_station(station, dist):
    def within_dist_station_station(dist_station):
        return calc_dist(station.lat, station.lon, dist_station.lat, dist_station.lon) <= dist
    return within_dist_station_station

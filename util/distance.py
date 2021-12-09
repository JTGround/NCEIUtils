import math

from ghcn.base_types import Station



def get_closest(stations, lat, lon):
    short_station = Station()
    shortdist = 10000
    for k, v in stations.items():
        dist = calc_dist(lat, lon, v.lat, v.lon)
        if dist < shortdist:
            shortdist = dist
            short_station = v
    return short_station

def get_dist_state(stations, state):
    distances = []
    for s in stations:
        for t in stations:
            # if scnt == tcnt:
            #	continue
            if s.state == state and t.state == state:
                dist = calc_dist(s.lat, s.lon, t.lat, t.lon)
                distances.append(dist)
    return distances


def get_short_dist(stations):
    shortdist = 100000
    scnt = 0
    tcnt = 0
    for s in stations:
        for t in stations:
            if scnt == tcnt:
                continue
            dist = calc_dist(s.lat, s.lon, t.lat, t.lon)
            if dist < shortdist:
                shortdist = dist
            tcnt += 1
        scnt += 1
    return shortdist


# returns distance in km
def calc_dist(lat1, lon1, lat2, lon2):
    R = 6371
    lat1int = float(lat1)
    lon1int = float(lon1)
    lat2int = float(lat2)
    lon2int = float(lon2)

    latdist = math.radians(lat2int - lat1int)
    londist = math.radians(lon2int - lon1int)
    a = math.sin(latdist / 2) * math.sin(latdist / 2) + math.cos(math.radians(lat1int)) * math.cos(
        math.radians(lat2int)) * math.sin(londist / 2) * math.sin(londist / 2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    d = R * c  # dist in km
    return d
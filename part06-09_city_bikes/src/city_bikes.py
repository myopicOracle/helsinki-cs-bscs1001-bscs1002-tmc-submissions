# In this exercise we will write some functions for working on a file containing location data from the stations for city bikes in Helsinki.

# Each file will follow this format:

# Longitude;Latitude;FID;name;total_slot;operative;id
# 24.950292890004903;60.155444793742276;1;Kaivopuisto;30;Yes;001
# 24.956347471358754;60.160959093887129;2;Laivasillankatu;12;Yes;002
# 24.944927399779715;60.158189199971673;3;Kapteeninpuistikko;16;Yes;003

# Each station has a single line in the file. The line contains the coordinates, name, and other identifying information for the station.
# Distance between stations

# First, write a function named get_station_data(filename: str). This function should read the names and locations of all the stations in the file, and return them in a dictionary with the following format:
# Sample output

# {
#   "Kaivopuisto": (24.950292890004903, 60.155444793742276),
#   "Laivasillankatu": (24.956347471358754, 60.160959093887129),
#   "Kapteeninpuistikko": (24.944927399779715, 60.158189199971673)
# }

# Dictionary keys are the names of the stations, and the value attached is a tuple containing the location coordinates of the station. The first element in the tuple is the Longitude field, and the second is the Latitude field.

# Next, write a function named distance(stations: dict, station1: str, station2: str), which returns the distance between the two stations given as arguments.

# The distance is calculated using the Pythagorean theorem. The multiplication factors below are approximate values for converting latitudes and longitudes to distances in kilometres in the Helsinki region.

# # we will need the function sqrt from the math module 
# import math

# x_km = (longitude1 - longitude2) * 55.26
# y_km = (latitude1 - latitude2) * 111.2
# distance_km = math.sqrt(x_km**2 + y_km**2)

# Some examples of the function in action:

# stations = get_station_data('stations1.csv')
# d = distance(stations, "Designmuseo", "Hietalahdentori")
# print(d)
# d = distance(stations, "Viiskulma", "Kaivopuisto")
# print(d)

# Sample output

# 0.9032737292463177
# 0.7753594392019532

# NB: If Visual Studio can't find the file and you have checked that there are no spelling errors, take a look at these instructions.
# The greatest distance

# Please write a function named greatest_distance(stations: dict), which works out the two stations on the list with the greatest distance from each other. The function should return a tuple, where the first two elements are the names of the two stations, and the third element is the distance between the two.

# stations = get_station_data('stations1.csv')
# station1, station2, greatest = greatest_distance(stations)
# print(station1, station2, greatest)

# Sample output

# Laivasillankatu Hietalahdentori 1.478708873076181

# ========================

import math

# file_name = "stations1.csv" # testing

# ========================
# Part 1

def get_station_data(file_name: str) -> dict:
  stations_dict = {}

  with open(file_name) as new_file:
    for line in new_file:
      line = line.strip()
      parts = line.split(";")
      if parts[0] == "Longitude":
        continue
      name, longitude, latitude = parts[3], float(parts[0]), float(parts[1])
      stations_dict[name] = (longitude, latitude)

  print(stations_dict) # debugger
  return stations_dict


def distance(stations: dict, station1: str, station2: str) -> float:
  station1_dict = stations[station1]
  # print(station1_dict) # debugger
  station2_dict = stations[station2]
  # print(station2_dict) # debugger

  longitude1 = station1_dict[0]
  # print(longitude1) # debugger
  longitude2 = station2_dict[0]
  # print(longitude2) # debugger
  latitude1 = station1_dict[1]
  # print(latitude1) # debugger
  latitude2 = station2_dict[1]
  # print(latitude2) # debugger

  x_km = (longitude1 - longitude2) * 55.26
  y_km = (latitude1 - latitude2) * 111.2
  distance_km = math.sqrt(x_km**2 + y_km**2)

  print(distance_km) # debugger
  return distance_km

# print(distance(stations, "Designmuseo", "Hietalahdentori")) # testing
# print(distance(stations, "Viiskulma", "Kaivopuisto")) # testing

# ========================
# Part 2

def greatest_distance(stations: dict) -> tuple:
  furthest_stations = ()

  station_names_list = []
  for name in stations:
    station_names_list.append(name)
  
  current_greatest = 0
  for key in stations:

    for i in range(len(station_names_list)):
      station_a = key
      station_b = station_names_list[i]
      distance_to_compare = distance(stations, key, station_names_list[i])
      if distance_to_compare > current_greatest:
        current_greatest = distance_to_compare
        print("current_greatest: ", current_greatest)
        furthest_stations = ( station_a, station_b, current_greatest )
        print("furthest_stations: ", furthest_stations)
        print(f"Current greatest is: {furthest_stations}")
      
  return furthest_stations

# stations = get_station_data('stations1.csv')
# station1, station2, greatest = greatest_distance(stations)
# print(station1, station2, greatest)


# ========================

if __name__ == "__main__":
  pass

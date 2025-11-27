import csv
import pandas

# with open("weather_data.csv","r") as data:
#     data_list = data.readlines()
# print(data_list)
# for d in data_list:
#     new_value = d.strip()
#     d_index = data_list.index(d)
#     data_list[d_index] = new_value

# print(data_list)

# with open("weather_data.csv","r") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != 'temp':
#             temperatures.append(int(row[1]))
#     print(temperatures)


data = pandas.read_csv("weather_data.csv")
print(data['temp'])
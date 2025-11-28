import pandas

# import csv
# import pandas
#
# # with open("weather_data.csv","r") as data:
# #     data_list = data.readlines()
# # print(data_list)
# # for d in data_list:
# #     new_value = d.strip()
# #     d_index = data_list.index(d)
# #     data_list[d_index] = new_value
#
# # print(data_list)
#
# # with open("weather_data.csv","r") as data_file:
# #     data = csv.reader(data_file)
# #     temperatures = []
# #     for row in data:
# #         if row[1] != 'temp':
# #             temperatures.append(int(row[1]))
# #     print(temperatures)
#
# # def c_to_f(temp):
# #     temp_f = (temp*9/5)+32
# #     return temp_f
# #
# # data = pandas.read_csv("weather_data.csv")
# #
# # data_dict = data.to_dict()
# # temp_list = data["temp"].to_list()
# # # print(data['temp'].max())
# # # print(data.condition)
# # # print(data[data.day == "Monday"])
# # print(data[data.temp  == data.temp.max()])
# # monday = data[data.day == "Monday"]
# # print(f"Monday's temp in Fahrenheit is:  {c_to_f(monday.temp)}")
#
# data_dict = {
#     "students":["Amy","James","Angela"],
#     "scores":[76,56,65]
# }
#
# data = pandas.DataFrame(data_dict)
# print(data)
#
# data.to_csv("new_data.csv")

data_source = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20251128.csv")
color_count = data_source["Primary Fur Color"].value_counts()
color_cont_dict = color_count.to_dict()
color_cont_keys = color_cont_dict.keys()
color_count_values = color_cont_dict.values()

fur_color_dict = {"Fur Color":color_cont_keys,
                  "Count":color_count_values}

color_dataframe = pandas.DataFrame(fur_color_dict)
color_dataframe.to_csv("squirrell_colors.csv")





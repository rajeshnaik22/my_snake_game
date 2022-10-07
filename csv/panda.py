import pandas

data = pandas.read_csv("csv/weather_data.csv")
print(data[data.day == "Monday"]) # To get row for specified column value

print(data[data.temp == data.temp.max()]) #To get row with max column value

hot_day = data[data.temp == data.temp.max()]
print("Hot day temprature was ${hot_day.temp}")
print(hot_day.temp)
data.max
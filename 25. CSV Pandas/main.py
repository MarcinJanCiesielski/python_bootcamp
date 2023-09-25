import csv
import pandas

data = []

with open("./weather_data.csv", encoding="utf8") as csv:
    for line in csv.readlines():
        data.append(line.strip())

print(data)

with open("./weather_data.csv", encoding="utf8") as data_file:
    data = csv.reader(data_file)
    temperatures = []
    for row in data:
        if row[1] != "temp":
            temperatures.append(int(row[1]))

print(temperatures)

data = pandas.read_csv("./weather_data.csv")
print(type(data))

data_dict = data.to_dict()
# print(data_dict)

temp_list = data['temp'].to_list()
print(temp_list)

print(sum(temp_list) / len(temp_list))
print(data['temp'].mean())
print(data['temp'].max())

# Get Data in columns
print(data['condition'])

# Get data in rows
print(data[data.day == "Monday"])
print(data[data.temp == data.temp.max()])

monday = data[data.day == "Monday"]
fahrenheit = (monday.temp * 1.8) + 32
print(fahrenheit)


# Create DataFrame
data_dict = {
    "students": ['Amy', 'James', 'Angela'],
    "scores": [73, 56, 65]
}

data = pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")

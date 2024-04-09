import json


f1 = open("data/NYC_DogLicensing_modified.csv", "r")
lines = f1.readlines()
#print(lines)

dictionary ={}
zipcodes = []
# Create the dictionary here
for line in lines:
    line_list = list(line.split(","))
    if line_list[2][0].isnumeric() == False:
        line_list.remove(line_list[2])
    zipcodes.append(line_list[2].strip())
print(zipcodes)

for key in zipcodes:
    if key not in dictionary:
        dictionary[key] = zipcodes.count(key)
print(dictionary)
f1.close()

#Save the json object to a file
f2 = open("data/NYC_DogLicensing_modified.json", "w")
json.dump(dictionary, f2, indent = 4)

f2.close()
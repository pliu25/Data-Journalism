import json


f1 = open("data/NYC_DogLicensing_modified.csv", "r")
lines = f1.readlines()
#print(lines)

dictionary ={}
zipcodes = []
# Create the dictionary here
for line in lines:
    line_list = line.split(",")
    if line_list[2] != num
    zipcodes.append(line.split(",")[2])
print(zipcodes)
f1.close()

#Save the json object to a file
f2 = open("data/NYC_DogLicensing_modified.json", "w")
json.dump(dictionary, f2, indent = 4)

f2.close()
import json
from collections import defaultdict

f1 = open("data/data.csv", "r")
lines = f1.readlines()
#print(lines)

zipcode_dict ={}
zipcode_dict["macro"] = {}
zipcodes = []
# Create the zipcode_dict here
for line in lines:
    line_list = list(line.split(","))
    if line_list[2][0].isnumeric() == False:
        line_list.remove(line_list[2])
        if line_list[2][0].isnumeric() == False:
            line_list.remove(line_list[2])

    zipcodes.append(line_list[2].strip())
print(len(zipcodes))
#print(zipcode_breed_dict)

#zipcode dictionary: # of breeds in zipcode 
for zip in zipcodes:
    if zip not in zipcode_dict["macro"]:
        zipcode_dict["macro"][zip] = zipcodes.count(zip)

breeds_set = set()
for line in lines: 
    line_list = list(line.split(","))
    breeds_set.add(line_list[1])
#print(breeds_set)

zipcodes_set = set(zipcodes)
#print(zipcodes_set)

zipcodes_breed_draft = defaultdict(list)
#print(zipcodes_breed_draft)

for line in lines:
    line_list = list(line.split(","))
    if line_list[2][0].isnumeric() == False:
        line_list.remove(line_list[2])
    breed_list = list(line_list[1].split('/', 1)[0])
    for char in breed_list:
        if (char.isspace() == False) and (char.isalpha() == False):
            breed_list.remove(char)
    zipcodes_breed_draft[line_list[2].strip()].append("".join(breed_list))
    #zipcodes_breed_draft.append(zipcodes_breed_draft_dict)
    #zipcodes_breed_draft_dict = {}

zipcode_dict["micro"] = {}
for zip in zipcodes_breed_draft.keys():
    zipcode_dict["micro"][zip] = {}
    for breed in zipcodes_breed_draft[zip]:
        if breed not in zipcode_dict["micro"][zip]:
            zipcode_dict["micro"][zip][breed] = zipcodes_breed_draft[zip].count(breed)
        



#print(zipcodes_breed_draft)

print(zipcode_dict["macro"].values())
f1.close(zipcode_dict)

#Save the json object to a file
f2 = open("data/data.json", "w")
json.dump(zipcode_dict, f2, indent = 4)

f2.close()
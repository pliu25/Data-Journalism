import json
from collections import defaultdict

f1 = open("data/NYC_DogLicensing_modified.csv", "r")
lines = f1.readlines()
#print(lines)

zipcode_dict ={}
zipcodes = []
# Create the zipcode_dict here
for line in lines:
    line_list = list(line.split(","))
    if line_list[2][0].isnumeric() == False:
        line_list.remove(line_list[2])
    zipcodes.append(line_list[2].strip())
#print(zipcodes)
#print(zipcode_breed_dict)

#zipcode dictionary: # of breeds in zipcode 
for key in zipcodes:
    if key not in zipcode_dict:
        zipcode_dict[key] = zipcodes.count(key)
#print(zipcode_dict)

breeds_set = set()
for line in lines: 
    line_list = list(line.split(","))
    breeds_set.add(line_list[1])
#print(breeds_set)

zipcodes_set = set(zipcodes)
#print(zipcodes_set)

zipcodes_breed_draft = defaultdict(list)
zipcodes_breed_draft[10].append("yay")
print(zipcodes_breed_draft)

for line in lines:
    zipcodes_breed_draft_dict = {}
    line_list = list(line.split(","))
    if line_list[2][0].isnumeric() == False:
        line_list.remove(line_list[2])
    breed_list = list(line_list[1])
    revised_breed_list = []
    for char in breed_list:
        fix_char = list("".join(char.split('/', 1)[0]))
        revised_breed_list.append(fix_char)
        if (fix_char.isspace() == False) and (fix_char.isalpha() == False):
            revised_breed_list.remove(fix_char)
    zipcodes_breed_draft[line_list[2].strip()].append("".join(revised_breed_list))
    #zipcodes_breed_draft.append(zipcodes_breed_draft_dict)
    #zipcodes_breed_draft_dict = {}

print(zipcodes_breed_draft)



'''
breeds_dictionary = {}
for zipcode in zipcodes_set:
    if zipcode not in breeds_dictionary:
        breeds_dictionary[zipcode] = {}
        for breed in breeds_set:
            if breed not in breeds_dictionary[zipcode]:
                breeds_dictionary[zipcode][breed] = {}
                
print(breeds_dictionary)
'''

f1.close()

#Save the json object to a file
f2 = open("data/NYC_DogLicensing_modified.json", "w")
json.dump(zipcode_dict, f2, indent = 4)
json.dump(zipcodes_breed_draft, f2, indent = 4)

f2.close()
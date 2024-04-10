import json


f1 = open("data/NYC_DogLicensing_modified.csv", "r")
lines = f1.readlines()
#print(lines)

zipcode_dict ={}
zipcodes = []
zipcode_breed_dict = {}
# Create the zipcode_dict here
for line in lines:
    line_list = list(line.split(","))
    if line_list[2][0].isnumeric() == False:
        line_list.remove(line_list[2])
    zipcodes.append(line_list[2].strip())
    zipcode_breed_dict[line_list[2].strip()] = []
#print(zipcodes)
print(zipcode_breed_dict)

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




#print(zipcode_breed_dict)

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

f2.close()
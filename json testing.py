import json

###example JSON data
x = '{"name":"john", "age":"30", "city":"New York"}'

###python object
a = {"name":"john","age":"30","city":"New York"
}

###parse/read json data from x to python dictionary (.loads for string in-memory| .load for files)
y = json.loads(x)

###parse/write python object data from a to json (.dumps for string in-memory| .dump for files)
z = json.dumps(a,indent=4)

#print(y["age"])
#print(z)

###"r" indicates that we are reading from the file "w" is for writing
with open("example data.json","r") as file:
    data = json.load(file)

###loop over each entry/object under "students" (cap sensitive)
#for student in data["students"]:
#    print(student["name"], "=" ,student["age"])

string = "port1: 12345 \nport2: 12345 \nport3: 12345 \nport4: 12345 \nport5: 12345"

to_dict = {}

for value in string.split("\n"):
    to_dict.update({"adw": "wadda"})


print(to_dict)
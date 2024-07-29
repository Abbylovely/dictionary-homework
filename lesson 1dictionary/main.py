# creating dictionary
friut_colours={
    "apple":"red",
    "banana":"yellow",
    "grape":"green",
    "mango":"orange"
}
print(friut_colours)
# accessing a value using its key
print(friut_colours["mango"])
# adding new key-value pair
friut_colours["strawberry"]="white"
print(friut_colours)
# get keys
keys=friut_colours.keys()
print(keys)
# get values
values=friut_colours.values()
print(values)
# list of key-value piar
pairs=friut_colours.items()
print(pairs)
# check if a key exists
if "grape" in friut_colours:
    print("it exists in the key value pair")
else:
    print("it does not exists in the key value print")
# looping through the dictionary
for i in friut_colours:
    print(i)
print("\n")
# looping through the dictionary values
for i in friut_colours.values():
    print(i)
# deleting from dictionary
del friut_colours["grape"]
print(friut_colours)
# change the value
friut_colours["strawberry"]="pink"
print(friut_colours)
#change key value pair
friut_colours["blueberry"]=friut_colours.pop("strawberry")
print(friut_colours)
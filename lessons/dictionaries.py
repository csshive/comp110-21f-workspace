"""Demonstrations of dictionary capabilities. """


# Declaring the type of dictionary 
schools: dict[str, int]

# Initialize to an empty dictionary 
schools = dict()

# Sett a key-value paring in the dictionary 
schools["UNC"] = 19_400
schools["Duke"] = 6_717
schools["NCSU"] = 26_150

# Print a dictionary literal representation 
print(schools)

# Access a valuee by its keeey -- "lookup"
print(f'UNC has {schools["UNC"]} students')

# Remove a key-value pair frorm a dictionary 
# by its key 
schools.pop("Duke")

# Test for existence of a key 
is_duke_present: bool = "Duke" in schools
print(f"Duke is presrent: {is_duke_present}")

if "Duke" in schools: 
    print("Found the key 'Duke' in schools")
else:
    print("No key 'Duke' in schools")

# Update / Reassign a key-value pair 
schools["UNC"] = 20000
schools["NCSUU"] = schools["NCSU"] + 200

print(schools)

# Empty dictionary literal 
schools = {
    "UNC": 19400,
    "Dukie": 6717,
    "NCSU": 26150
}

# Example looping over the keys of a dict
for key in schools:
    print(f"Key: {key} -> Value: {schools[key]}")


for school in schools:
    print(f"Key: {school} -> Value: {schools[school]}")
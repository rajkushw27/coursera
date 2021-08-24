import csv

# reading csv files
file = open("test.csv")
csvfile = csv.reader(file)

for row in csvfile:
    name, age, place = row
    print(f'Name: {name} is {age} year old and lives in {place}')
file.close()
# writing to csv files

hosts = [["windows server:", "192.168.1.7"], ["mac server", "192.168.1.9"]]

with open("createcsv.csv", "w") as host_csv:
    host_csvfile = csv.writer(host_csv)
    host_csvfile.writerows(hosts)

# read and write csv file using dict

with open("test.csv") as dictread:
    file = csv.DictReader(dictread)
    for row in file:
        print(f'name is {row["Name"]} and age is {row["Age"]}')

users = [{"name": "ankit", "username": "ankchandel", "department": "IT"}, {"name": "deepak", "username": "deeprai", "department": "Mechanical"}, {
    "name": "ankit", "username": "ankmota", "department": "Metro"}, {"name": "Rajani", "username": "rajkushw", "department": "ML"}]
keys = ["name", "username", "department"]
with open("createcsv2.csv", "w") as emp:
    file = csv.DictWriter(emp, fieldnames=keys)
    file.writeheader()
    file.writerows(users)

import os
import datetime
# reading a file
file = open("spider.txt")

firstline = file.readline().strip()
all_lines = file.read()

print(firstline)
print(all_lines)
file.seek(0)
file.close()

with open("spider.txt") as second_file:
    for line in second_file:
        print(line.strip().upper())

with open("spider.txt") as third_file:
    file_as_a_list = third_file.readlines()
    print(file_as_a_list)

# writing to a file

with open("write.txt", 'w') as wfile:
    wfile.write("it's written by python")

with open("spider.txt", "a") as wfile:
    wfile.write("it's writtne by python not by spider")

# directory operations
os.remove("write.txt")
#os.rename("spider.txt", "newspider.txt")
if os.path.exists("spider.txt"):
    file_modify_date = os.path.getmtime("spider.txt")
    print(datetime.datetime.fromtimestamp(file_modify_date))
    print(os.path.abspath("spider.txt"))
    print(os.path.getsize("spider.txt"))

print(os.getcwd())
print(os.mkdir("testDir"))
print(os.chdir("testdir"))
print(os.listdir("../"))
os.chdir("../")
dir_check = os.getcwd()

for name in os.listdir(dir_check):
    full_name = os.path.join(dir_check, name)
    if os.path.isdir(full_name):
        print(f'{name} is a directory')
    else:
        print("{} is a file".format(name))

print(os.rmdir("testdir"))

import re

log = "July 31 07:16:32 my computer bad process[43533]: ERROR Performing package upgrade"
regex = r"\[(\d+)\]"
result = re.search(regex, log)
print(result[1])

print(re.search(r'p.ng', 'Penguien', re.IGNORECASE))
# character class
print(re.search(r'[a-z]way', 'the end of highway'))
print(re.search(r'cat|dog', 'i like dogs'))
print(re.findall(r'dog|cat', "i like both cat and dogs"))

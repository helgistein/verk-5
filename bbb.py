import re
line = " I am having a very nice day."
count = len(re.findall(r'\w+', line))
print (count)
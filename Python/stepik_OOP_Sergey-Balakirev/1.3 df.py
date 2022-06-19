import re
import string

pattern = re.compile('[\W_]+')
print(string.printable)
print(pattern.sub('', string.printable))
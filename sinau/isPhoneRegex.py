import re

phoneNumRegex = re.compile(r"(\d\d\d)-(\d\d\d-\d\d\d\d)")
mo = phoneNumRegex.search("My phone number is 415-777-8790.")
print("Phone number found: ", mo.group(2))

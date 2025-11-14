import re

def filter_datum(fields, redaction, message, separator):
    return re.sub(rf'({"|".join(fields)})=[^ {separator}]*', lambda m: f"{m.group(1)}={redaction}", message)

fields = ["name", "email", "phone", "ssn", "password"]
messages = [
    "name=egg;email=egg@sample.com;password=eggcellent;date_of_birth=12/12/1986;",
    "name=bob;email=bob@example.com;password=bob123;date_of_birth=03/04/1993;"
]

for message in messages:
    print(filter_datum(fields, 'xxx', message, ';'))
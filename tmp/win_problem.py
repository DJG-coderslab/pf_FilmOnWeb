import argparse

from pathlib import Path


class WinUser:
    def __init__(self):
        self.attr = {}
        self.name = None

    def add_item(self, key, value):
        # print(f"k:{key}, v: {' '.join(value)}")
        self.attr[key] = ' '.join(value)

app_args = argparse.ArgumentParser()
app_args.add_argument('files', metavar='F', type=str, nargs='+')

args = app_args.parse_args()

attrs = set()
users = []

for file in args.files:
    user = WinUser()
    users.append(user)
    with open(Path(file), 'r') as f:
        for line in f:
            if len(line) < 3:
                continue
            # if 'Name' in line:
            #     continue
            if '----' in line:
                continue
            line = ' '.join(line.split())
            line = line.strip()
            a, *b = line.split()
            attrs.add(a)
            user.add_item(a, b)

# for user in users:
#     print(user.attr['name'])

# print(attrs)
for attr in attrs:
    print(f"           --- {attr} ---       ")
    for user in users:
        name = user.attr['name'].replace('{', '').replace('}', '').split(',')[0]
        print(f"{name:<12s}   {user.attr.get(attr)}")


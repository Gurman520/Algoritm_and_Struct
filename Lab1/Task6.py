import os
import hashlib


def get_hash_md5(file):
    with open(file, 'rb') as f:
        m = hashlib.md5()
        while True:
            data = f.read(8192)
            if not data:
                break
            m.update(data)
        return m.hexdigest()


dct = {}
print("Введите путь до файла")
path = str(input())
if os.path.exists(path):
    files = os.listdir(path)
    for name in files:
        file = f'{path}\{name}'
        if os.path.isfile(file):
            key = get_hash_md5(file)
            dct[key] = dct.get(key, []) + [file]
    key = dct.keys()
    for k in key:
        if len(dct.get(k)) > 1:
            print(dct.get(k))
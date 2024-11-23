import threading
import json

def parse(file_path: str):
    with open(file_path, 'r') as f:
        data = json.load(f)
    file_name = file_path.split('/')[-1]
    print(f'File Name: {file_name}\n'
          f'Contents: {data}\n')

file_paths = ['f1.json', 'f2.json', 'f3.json']
threads = []

for path in file_paths:
    thread = threading.Thread(target=parse, args=(path,))
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()
# TODO: Create a program that does the following
#  1. Reads all .py files from a folder
#  2. Adds them all to a string while checking for duplicity
#  3. Separates code segments to the desired size with POSTFIX
#  4. Creates a file whose name includes datetime and extension is .tfd

import glob
import os
from re import sub
from scrap_n_crawl import POSTFIX, PREFIX, dt


# checks to see if s1 or similar is already in s2 (data)
def is_close(s1: str, s2: str) -> bool:
    return s1[:len(s1) // 3] in s2 or s1[len(s1) // 3:2 * len(s1) // 3] in s2 or s1[2 * len(s1) // 3:] in s2


data = PREFIX
path = r'E:\Desktop\TypeFu\dotpys'
for filename in glob.glob(os.path.join(path, '*.py')):  # code to access and loop through all .py in a path
    with open(os.path.join(os.getcwd(), filename), 'r') as f:  # open in read-only mode
        fr = f.read()
        if not is_close(fr, data):
            data += fr
        else:
            print('file already in data')

for i in range(10, 1, -1):
    data = data.replace('\n' * i, '\n')  # replaces multiple eol with a single one

data = sub('"""(.|\n)*?"""', '', data)  # subs everything inside triple quotes incl. them incl eol with nada
data = sub('"(.|\n)*?"', '', data)  # subs everything inside single quotes incl. them incl eol with nada
data = sub('##.*?\n', '', data)  # subs everything between ## and eol(maybe unnecessary) incl. them with nada

prev_index = 0
new_data = ""
snippet_count = 0
for i, c in enumerate(data):
    data_slice = data[prev_index:i + 1]
    if c == '\n' and len(data_slice) > 300:  # splits snippets by eol as long as we have reached 300 chars
        new_data += data_slice + POSTFIX
        prev_index = i + 1
        snippet_count += 1
new_data = new_data.rstrip(POSTFIX)
print(snippet_count)
with open(file=rf'E:\Desktop\TypeFu\assembled_from_pys\TF{dt.now().strftime("%d%m%y_%H%M")}.tfd', mode='w') as f:
    f.write(new_data)

import os
import sys
import re
import time

if len(sys.argv) < 2:
    print('pick a hand')
    sys.exit(-1)
if sys.argv[1] == 'l':
    h = 'left'
elif sys.argv[1] == 'r':
    h = 'right'
else:
    print(f'{sys.argv[1]} is not a hand')
    exit(-1)

n = f'corne_{h}-nice_nano_v2-zmk.uf2'
dl = '/Users/chris/Downloads'
files = os.listdir(dl)
fws = [(int(f.split('-')[1]), f) for f in files if re.search('^firmware-[0-9]+$', f)]
fws.sort(key=lambda x: x[0], reverse=True)
os.system('rm -i /Volumes/NICENANO/*')
time.sleep(1)
os.system(f'cp {dl}/{fws[0][1]}/{n} /Volumes/NICENANO/')

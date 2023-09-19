import os

files = os.listdir(os.getcwd())

for path, dir, files in os.walk(os.getcwd()):
    for f in files:
        ext = f.split('.')[-1]
        if ext in ['c', 'h', 'cc', 'cpp', 'c++', 'cxx', 'hpp', 'hxx', 'hh', 'h++', 'H']:
            print('open', path, f)
            os.system(f'code {path}\{f}')
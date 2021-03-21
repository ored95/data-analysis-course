#!/usr/bin/env python3

import sys

def file_extensions(filename='src/filenames.txt'):
    try:
        no_ext, exts = [], {}
        with open(filename, 'r') as f:
            for line in f:
                line = line.strip('\n')
                dot = line.rfind('.')
                if dot > 0:
                    ext = line[dot+1:]
                    if ext in exts.keys():
                        exts[ext] += [line]
                    else:
                        exts[ext] = [line]
                else:
                    no_ext.append(line)
        return no_ext, exts
    except EnvironmentError:
        print('FileNotFoundError: No such file or directory: {0}'.format(filename), file=sys.stderr)
        return None    

def main():
    res = file_extensions()
    if res:
        print('{0} files with no extension'.format(len(res[0])))
        for ext, files in sorted(res[1].items()):
            print('{0} {1}'.format(ext, len(files)))

if __name__ == "__main__":
    main()

#!/usr/bin/env python

"""
Generates an HTML table of syscalls from a JSON file.
"""

import json
import argparse

def strip_prefix(s, prefix):
    return s[s.startswith(prefix) and len(prefix):]

def man_page(name):
    return f"http://man7.org/linux/man-pages/man2/{name}.2.html"

def gen_table_row(syscall):
    num = syscall["num"]
    name = strip_prefix(syscall["name"], "sys_")
    params = ', '.join([
        f"<strong>{typ}</strong> {param}" for (typ, param) in syscall["params"]
    ])

    yield "<tr>"
    yield '<td align="right">{}</td>'.format(num)
    yield f'<td><code><a href="{man_page(name)}">{name}</a>({params})</code></td>'
    yield "</tr>"

def gen_table(syscalls):
    yield "<table>"
    yield "<tr>"
    yield "<th>#</th>"
    yield "<th>Syscall</th>"
    yield "</tr>"

    for syscall in syscalls:
        yield from gen_table_row(syscall)

    yield "</table>"

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('json', type=argparse.FileType('r'))

    args = parser.parse_args()

    syscalls = json.load(args.json)

    for line in gen_table(syscalls):
        print(line)

if __name__ == "__main__":
    main()

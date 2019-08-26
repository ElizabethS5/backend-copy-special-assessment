#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Copyspecial Assignment"""

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import re
import os
import shutil
import subprocess
import argparse
import sys

# This is to help coaches and graders identify student assignments
__author__ = "ElizabethS5"


# +++your code here+++
# Write functions and modify main() to call them
def get_special_paths(dir):
    """returns a list of the absolute paths of the special files in the given directory"""
    return [os.path.abspath(file) for file in os.listdir(dir) if re.search(r'__\w+__', file)]


def copy_to(paths, directory):
    """given a list of paths, copies those files into the given directory"""
    for path in paths:
        os.makedirs(directory, exist_ok=True)
        shutil.copy(path, directory)


def zip_to(paths, zippath):
    """given a list of paths, zip those files up into the given zipfile"""
    cmd = ['zip', '-j', 'tmp.zip'] + paths
    print("Command I'm going to do:")
    print(' '.join(cmd))
    p = subprocess.run(cmd, stdout=subprocess.PIPE)
    if p.returncode:
        print()
        print(p.stdout.decode('utf-8'))


def main():
    # This snippet will help you get started with the argparse module.
    parser = argparse.ArgumentParser()
    parser.add_argument('--todir', help='dest dir for special files')
    parser.add_argument('--tozip', help='dest zipfile for special files')
    parser.add_argument('from_dir', help='directory being searched')
    # TODO need an argument to pick up 'from_dir'
    args = parser.parse_args()

    # TODO you must write your own code to get the cmdline args.
    # Read the docs and examples for the argparse module about how to do this.

    # Parsing command line arguments is a must-have skill.
    # This is input data validation.  If something is wrong (or missing) with any
    # required args, the general rule is to print a usage message and exit(1).

    # +++your code here+++
    # Call your functions
    if args.todir:
        copy_to(get_special_paths(args.from_dir), args.todir)
    elif args.tozip:
        zip_to(get_special_paths(args.from_dir), args.tozip)
    else:
        print('\n'.join(get_special_paths(args.from_dir)) + '\n')


if __name__ == "__main__":
    main()

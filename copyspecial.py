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

# This is to help coaches and graders identify student assignments
__author__ = "ElizabethS5"


def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('--todir', help='dest dir for special files')
    parser.add_argument('--tozip', help='dest zipfile for special files')
    parser.add_argument('from_dir', help='directory being searched')
    return parser.parse_args()


def get_special_paths(dir):
    """returns list of absolute paths of special files in given directory"""
    return [
        os.path.abspath(file)
        for file in os.listdir(dir)
        if re.search(r'__\w+__', file)
    ]


def copy_to(paths, directory):
    """given a list of paths, copies those files into the given directory"""
    for path in paths:
        os.makedirs(directory, exist_ok=True)
        shutil.copy(path, directory)


def zip_to(paths, zippath):
    """given a list of paths, zip those files up into the given zipfile"""
    cmd = ['zip', '-j', zippath] + paths
    print("Command I'm going to do:")
    print(' '.join(cmd))
    p = subprocess.run(cmd, stdout=subprocess.PIPE)
    if p.returncode:
        print()
        print(p.stdout.decode('utf-8'))


def main():
    """Use cmd line arguments to copy, zip, or print special files"""
    args = get_arguments()
    to_directory = args.todir
    to_zip = args.tozip
    from_directory = args.from_dir
    file_paths = get_special_paths(from_directory)

    if to_directory:
        copy_to(file_paths, to_directory)
    elif to_zip:
        zip_to(file_paths, to_zip)
    else:
        print('\n'.join(file_paths) + '\n')


if __name__ == "__main__":
    main()

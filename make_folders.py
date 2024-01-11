#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  3 13:19:09 2022

@author: anu
"""

import os

path = os.getcwd()
new_dirs = []

flair = 'flair'
#flair_mask = 'flair_mask'
t1post = 't1post'
#t1post_mask = 't1post_mask'

#### FILL THESE IN FOR THE RANGE OF FOLDERS YOU WANT ####
subject_start = 10
subject_end = 22

for i in range(subject_start, subject_end):
    new_dirs.append('DOSEESC_UM' + str(i))

for dir in new_dirs:
    # if the directory exists, remove it from the list of directories to be created
    if os.path.isdir(os.path.join(path, dir)) == 1: 
        print("skipping directory", dir)
        new_dirs.remove(dir)
    else:
        os.mkdir(os.path.join(path, dir))
        subdir_path = os.path.join(path, dir)
        os.mkdir(os.path.join(subdir_path, flair))
        #os.mkdir(os.path.join(subdir_path, flair_mask))
        os.mkdir(os.path.join(subdir_path, t1post))
        #os.mkdir(os.path.join(subdir_path, t1post_mask))    
#!/usr/bin/env python3

import os
import sys

import mutagen

def strip_null(file=None, verbose=False):
    try:
        audio =  mutagen.File(file)
    except:
        print("Can't open file:", file) 
        sys.exit()

    found = False 
    file_print = False
    for tag in audio:
        if "\x00" in audio[tag][0]:
            found = True
            if verbose is True:
                if file_print == False:
                    print("Found in:", file)
                    file_print = True
                print("Null string in:", tag)
            audio[tag] = audio[tag][0].rstrip("\x00")

    if found is True:
        if verbose is True:
            print("Saving file:", file)
        try:
            audio.save()
        except:
            print("Can't save file:", file)
            sys.exit()

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--verbose", help="increase verbosity", action="store_true")
    parser.add_argument("file", help="path to file")
    args = parser.parse_args()

    strip_null(file=args.file, verbose=args.verbose)

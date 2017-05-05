#!/usr/bin/env python3

from Poster import post
from csvParser import csvParser
from Settings import filename

def main():
    data = csvParser(filename)
    post(data)

if __name__ == "__main__":
        main()

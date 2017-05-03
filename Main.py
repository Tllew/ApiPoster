#!/usr/bin/env python3

from Poster import post
from csvParser import csvParser

def main():
    data = csvParser("basicCsv.csv")
    post(data)

if __name__ == "__main__":
        main()

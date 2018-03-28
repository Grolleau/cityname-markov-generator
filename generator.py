# -*- coding: utf-8 -*-
import markovify
import os
import argparse
from analyzer.city import CityNameText

parser = argparse.ArgumentParser(description='Generate french city names')
parser.add_argument('-n', dest='numberToGenerate', metavar='N', type=int, default=5,
                    help='Number of city to generate (default: 5)')

if __name__ == "__main__":

    args = parser.parse_args()

    fn = os.path.join(os.path.dirname(__file__), 'data/french_towns.csv')
    
    with open(fn, "r", encoding="utf-8") as f:
        text = f.read()

    text_model = CityNameText(text, state_size = 3)
    
    i=0
    while i < args.numberToGenerate:
        city = text_model.make_sentence()
        if(city is not None):
            print(city)
            i+=1
        
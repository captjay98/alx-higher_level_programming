#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary == {} or a_dictionary is None:
        return None

    toreturn = max(a_dictionary.values())

    for key, val in a_dictionary.items():
        if val is toreturn:
            return key

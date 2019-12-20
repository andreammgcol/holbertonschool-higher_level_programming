#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None or a_dictionary == {}:
        return None
    else:
        max_score = (max(a_dictionary, key=a_dictionary.get))
        if max_score == 0:
            return None
        else:
            return max_score

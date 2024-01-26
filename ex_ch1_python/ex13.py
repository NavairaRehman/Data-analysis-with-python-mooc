#!/usr/bin/env python3

def reverse_dictionary(d):
    """Returns a reversed dictionary from the given dictionary."""
    new_dict = {}
    for key, value in d.items():
        for item in value:
            if item in new_dict:
                new_dict[item].append(key)
            else:
                new_dict[item] = [key]
    return new_dict

def main():
    d = {"move": ["liikuttaa"], "hide": ["piilottaa", "salata"], "six": ["kuusi"], "fir": ["kuusi"]}
    print(d)
    print(reverse_dictionary(d))

if __name__ == "__main__":
    main()

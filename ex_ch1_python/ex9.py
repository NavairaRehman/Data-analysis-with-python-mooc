#!/usr/bin/env python3

def merge(L1, L2):
    "Takes two sorted lists and returns a sorted list containing all elements of both lists."
    if len(L1) == 0:
        return L2
    elif len(L2) == 0:
        return L1
    elif L1[0] < L2[0]:
        return [L1[0]] + merge(L1[1:], L2)
    elif L1[0] > L2[0]:
        return [L2[0]] + merge(L1, L2[1:])
    else:
        # If elements are equal, include only one and proceed with both lists
        return [L1[0],L2[0]] + merge(L1[1:], L2[1:])


def main():
    L1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    L2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    print(len(L1))
    print(len(L2))
    print(merge(sorted(L1), sorted(L2)))
    print(len(merge(sorted(L1), sorted(L2))))


if __name__ == "__main__":
    main()

#!/usr/bin/env python3

def detect_ranges(lst):
    lst.sort()
    result = []
    start_range = lst[0]
    end_range = lst[0]
    
    for i in range(1, len(lst)):
        if lst[i] == lst[i - 1] + 1:
            end_range = lst[i]
        else: 
            if start_range == end_range:
                result.append(start_range)
            else:
                result.append((start_range, end_range + 1))
            start_range = end_range = lst[i]
    
    if start_range == end_range:
        result.append(start_range)
    else:
        result.append((start_range,end_range+1))
    
    
    return result



def main():
    L = [2, 5, 4, 8, 12, 6, 7, 10, 13]
    result = detect_ranges(L)
    print(L)
    print(result)

if __name__ == "__main__":
    main()

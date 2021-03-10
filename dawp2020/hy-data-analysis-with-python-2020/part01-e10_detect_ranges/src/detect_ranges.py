#!/usr/bin/env python3

def detect_ranges(L):
    L = sorted(L)
    L1 = []
    i = 0
    while i <= len(L) - 1:
        j = i
        while j < len(L) - 1 and L[j+1] - L[j] == 1:
            j += 1

        if i == j:
            L1.append(L[i])
        else:
            L1.append((L[i], L[j]+1))
        i = j + 1
    return L1

def main():
    L = [2, 5, 4, 8, 12, 6, 7, 10, 13]
    result = detect_ranges(L)
    print(L)
    print(result)

if __name__ == "__main__":
    main()

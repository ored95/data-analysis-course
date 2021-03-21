#!/usr/bin/env python3

def merge(L1, L2):
    L = [] 
    i, j = 0, 0
  
    while i < len(L1) and j < len(L2): 
        if L1[i] < L2[j]: 
            L.append(L1[i]) 
            i += 1
        else: 
            L.append(L2[j]) 
            j += 1

    L = L + L1[i:] + L2[j:]
    return L
    
def main():
    pass

if __name__ == "__main__":
    main()

def maxToEnd(l):
    for i in range (len(l)-1):
        a = i
        b = i+1
        #print(l[a], l[b])
        if l[b] < l[a]:
            c = l[a] 
            l[a] = l[b]
            l[b] = c
    return l

def bubbleSort(l):
    for i in range (len(l)-1):
        l=maxToEnd(l)
    return l

def quickSort(l):
    return l

def heapSort(l):
    return l

# python3



def Siftdown(data,i,size,list1):
    
    
    minindex = i
    
    l = (i*2) + 1
    
    if l < size and data[l] < data[minindex]:
        
        minindex = l
        
    r = (i*2) + 2
    
    
    
    if r < size and data[r] < data[minindex]:
        
        minindex = r
        
        
    if i != minindex:
        
        s = (i,minindex)
        
        list1.append(s)
        
        a = data[i]
        
        b = data[minindex]
        
        data[i] = b
        
        data[minindex] = a
        
        Siftdown(data,minindex,size,list1)
        
    return list1
        

def build_heap(data,n):
    """Build a heap from ``data`` inplace.

    Returns a sequence of swaps performed by the algorithm.
    """
   
    roundel = round(len(data)/2)

    size = n
    
    list1 = []

    for i in reversed(range(roundel)):
    
        Siftdown(data,i,size,list1)
        
    
    print(len(list1))
    
    for i in range(len(list1)):
        
        print(list1[i][0],list1[i][1])


def main():
    n = int(input())
    data = list(map(int, input().split()))
    assert len(data) == n

    swaps = build_heap(data,n)


if __name__ == "__main__":
    main()
    

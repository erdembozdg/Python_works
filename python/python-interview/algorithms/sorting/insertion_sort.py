

def insertion_sort(arr): 
    for i in range(1,len(arr)): 
        currentvalue = arr[i]
        position = i
        while position>0 and arr[position-1]>currentvalue:    
            arr[position]=arr[position-1]
            position = position-1
        arr[position]=currentvalue
    return arr
        
array = [5,9,3,10,45,2,0]
print(insertion_sort(array))
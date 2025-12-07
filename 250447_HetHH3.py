
n = int(input())                    
arr = list(map(int, input().split()))  
x = int(input())                    


for i in range(n):
    for j in range(i+1, n):
        
        if abs(arr[i] - arr[j]) == x:
            print(arr[i], arr[j])   
            exit()                  


# Complete the cutTheSticks function below.
def cut_the_sticks(arr):
    print(len(arr))
    res = []
    while True:                
        res.append(len(arr)) 
        arr = [x for x in arr if x != min(arr)]         
        if len(arr)==0:
            break
    return list(dict.fromkeys(res))
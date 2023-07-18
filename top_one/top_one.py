#created function
def index(arr):
    value = {}
    result = []
    f_val = 0
#Looping through the list we sent
    for i in arr:
        if i in value:
            value[i] += 1
        else:
            value[i] = 1

#Find the highest repetition
    f_val = max(value.values())
#Looping over value keys
    for i in value.keys():
        if value[i] == f_val:
            result.append(i)
        else :
            continue

    return result , f_val


print(index([4,12]))

#Mohammad Sadegh

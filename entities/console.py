def test(list):
    a = []
    for i in list:
        a.append(i)
    return a

def listgenrerator():
    a = "abcdefghijklmnopqrstuvwxyz"
    b = []
    for i in a:
        b.append(i)
    
    return b

print(test(listgenrerator()))

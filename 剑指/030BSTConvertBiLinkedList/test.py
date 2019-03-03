def g():
    # global x
    if x > 10:
        return
    print(x)
    x += 1
    g()

def fun():
    global x
    x=1
    g()
    # print(x)

if __name__ == '__main__':

    fun()
    

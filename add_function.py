def add(a,b):
    c=a+b
    return c

def test_add():
    
    assert add(3,4) == 7
    
def main():
    
    a=3
    b=4
    c=add(a, b)
    print("A= ",a," B= ",b,"C= ",c)

if __name__ == "__main__":
    main()


def multiply(a,b):
    c=a*b
    return c

def test_multiply():
    
    assert multiply(3,4) == 12
    
def main():
    
    a=3
    b=4
    c=multiply(a, b)
    print("A= ",a," B= ",b,"C= ",c)

if __name__ == "__main__":
    main()



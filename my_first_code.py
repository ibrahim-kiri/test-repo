print("Hello, Class")
a=10
b=0
try:
    print ("This is outer try block")
    try:
        print (a/b)
    except ZeroDivisionError:
        print ("Division by 0")
    finally:
        print ("Inside inner finally block")

except Exception:
    print ("General Exception")
    
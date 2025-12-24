try:
    num=int("abc")
    print(num)
except ValueError:
    print("Value Error!")
finally:
    print("Code Executed!")

def multiply (a ,b):
    #LAST IN: FUNCTION C
    return a * b

def calculate_sum(x, y):
    #SECOND IN : FUNCTION B
    result = x + y
    product = multiply(result,2)
    return product

def main():
    final_value = calculate_sum(5,10)
    print(final_value)
    #FIRST IN: FUNCTION A

main()
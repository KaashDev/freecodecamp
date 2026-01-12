** start of main.py **

def number_pattern(n):
    if not isinstance(n,int):
        return("Argument must be an integer value.")
    if n<1:
        return("Argument must be an integer greater than 0.")
    else:
        result = ''
        for num in range(1, n+1):
            result += str(num) + ' '
        return result.strip()

** end of main.py **


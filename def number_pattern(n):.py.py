def number_pattern(n):
    if not isinstance(n,int):
        return 'Argument must be an integer value.'
    if n < 1:
        return 'Argument must be an integer greater than 0.'
    for i in range(n):
        print(i += 1)
        return 
    
number_pattern(4)
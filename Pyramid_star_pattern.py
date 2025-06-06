def generate_pyramid(n):
    """
    Function to return a pyramid pattern of '*' of side n as a list of strings.
    
    Parameters:
    n (int): The number of rows in the pyramid.
    
    Returns:
    list: A list of strings where each string represents a row of the pyramid.
    """
    # Your code here
    lst =[]
    for i in range(1,n+1):
        pattern = '*'* (2*i - 1)
        top_bottom = ' '* (n - i)+ pattern + ' '* (n - i)
        lst.append(top_bottom)
        
    return lst
raw_input = generate_pyramid(5)
print(raw_input)
        

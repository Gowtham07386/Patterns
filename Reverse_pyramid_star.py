def generate_inverted_pyramid(n):
    """
    Function to return an inverted pyramid pattern of '*' of side n as a list of strings.
    
    Parameters:
    n (int): The number of rows in the inverted pyramid.
    
    Returns:
    list: A list of strings where each string represents a row of the inverted pyramid.
    """
    # Your code here
    lst = []
    for i in range(n,0,-1):
        pattern = '*'* (2*i - 1)
        top_bottom = ' '* (n - i)+ pattern + ' '* (n - i)
        lst.append(top_bottom)
    return lst
raw_input = generate_inverted_pyramid(5)
print(raw_input)
        

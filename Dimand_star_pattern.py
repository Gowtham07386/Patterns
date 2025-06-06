def generate_diamond(n):
    """
    Function to return a diamond pattern of '*' of side n as a list of strings.
    
    Parameters:
    n (int): The number of rows for the upper part of the diamond.
    
    Returns:
    list: A list of strings where each string represents a row of the diamond.
    """
    # Your code here
    lst = []
    for i in range(1,n+1):
        pattern ='*'* (2*i - 1)
        top_bottom = ' '*(n -i)+pattern+' '*(n -i)
        lst.append(top_bottom)

    for j in range(n-1,0,-1):
        pattern ='*'* (2*j -1)
        top_bottom = ' '*(n -j)+pattern+' '*(n -j)
        lst.append(top_bottom)
    return lst
raw_input = generate_diamond(3)
print(raw_input)

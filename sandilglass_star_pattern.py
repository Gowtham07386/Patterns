def generate_sandglass(n):
    """
    Function to return a sandglass pattern of '*' of side n as a list of strings.
    
    Parameters:
    n (int): The height of the sandglass.
    
    Returns:
    list: A list of strings where each string represents a row of the sandglass pattern.
    """
    # Your code here
    lst =[]
    for i in range(n,0,-1):
        pattern = '*'*(2*i-1)
        sandglass =' '*(n -i)+pattern+' '*(n -i)
        lst.append(sandglass)
     
    for j in range(2,n+1):
        pattern = '*'*(2*j-1)
        sandglass =' '*(n -j)+pattern+' '*(n -j)
        lst.append(sandglass)
    return lst    


raw_input = generate_sandglass(3)
print(raw_input)

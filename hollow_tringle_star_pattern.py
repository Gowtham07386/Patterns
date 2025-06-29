def generate_hollow_right_angled_triangle(n):
    """
    Function to return a hollow right-angled triangle of '*' of side n as a list of strings.
    
    Parameters:
    n (int): The height of the triangle.
    
    Returns:
    list: A list of strings where each string represents a row of the triangle.
    """
    # Your code here
    lst = []
    for i in range(1,n+1):
        if i == 1:
            i = '*'
            lst.append(i)
        elif i == 2:
            i = '**'
            lst.append(i)
        elif i == n:
            i = '*'*i
            lst.append(i)
        else:
            i = '*'+' '*(i - 2)+'*'
            lst.append(i)
    return lst
raw_input = generate_hollow_right_angled_triangle(5)
print(raw_input)

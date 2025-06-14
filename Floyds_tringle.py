def generate_floyds_triangle(n):
    """
    Function to return the first n rows of Floyd's Triangle as a list of strings.
    
    Parameters:
    n (int): The number of rows in the triangle.
    
    Returns:
    list: A list of strings where each string represents a row of Floyd's Triangle.
    """
    # Your code here
    lst =[]
    curent = 1
    for i in range(1,n+1):
            row = ' '.join(str(curent +j) for j in range(i))
            lst.append(row)
            curent += i
        
    return lst    
        
raw_input = generate_floyds_triangle(5)
print(raw_input)

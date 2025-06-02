def generate_inverted_triangle(n):
    """
    Function to return an inverted right-angled triangle of '*' of side n as a list of strings.
    
    Parameters:
    n (int): The height and base of the triangle.
    
    Returns:
    list: A list of strings where each string represents a row of the triangle.
    """
    # Your code here
    lst = []
    for i in range(n,0,-1):
        i = "*"* i
        lst.append(i)
    return lst
in_put = generate_inverted_triangle(5)
print(in_put)

def generate_number_pyramid(n):
    """
    Function to return a pyramid pattern of numbers of height n as a list of strings.
    
    Parameters:
    n (int): The height of the pyramid.
    
    Returns:
    list: A list of strings where each string represents a row of the pyramid pattern.
    """
    # Your code here
    lst = []
    for i in range(1, n + 1):
        numbers = ' '.join(str(j) for j in range(1, i + 1))
        line = ' ' * (n - i) + numbers +' ' * (n - i)
        lst.append(line)
    return lst


raw_input = generate_number_pyramid(4)
print(raw_input)

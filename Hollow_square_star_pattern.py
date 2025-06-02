def hollow_square(n):
    if n ==1:
        return ['*']
    if n ==2:
        return ['**','**']
    
    top_bottom  =  '*' * n
    middle = '*'+ ' '*(n-2) +'*'
    return [top_bottom] + [middle]*(n-2) + [top_bottom]

n=int(input())
raw_input = hollow_square(n)
print(raw_input)
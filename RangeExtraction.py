def format_integer_list(integers):
    formatted_list = []
    start = integers[0]
    end = integers[0]
    
    for i in range(1, len(integers)):
        if integers[i] - integers[i-1] == 1:
            end = integers[i]
        else:
            if end - start >= 2:
                formatted_list.append(f"{start}-{end}")
            else:
                formatted_list.extend(str(num) for num in range(start, end+1))
            start = integers[i]
            end = integers[i]
    
    # Handle the last sequence of numbers
    if end - start >= 2:
        formatted_list.append(f"{start}-{end}")
    else:
        formatted_list.extend(str(num) for num in range(start, end+1))
    
    return ','.join(formatted_list)

# Example usage:
integers = [12, 13, 15, 16, 17, 20, 21, 22, 25]
formatted = format_integer_list(integers)
print(formatted)

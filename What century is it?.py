def what_century(year):
    year = int(year)
    century_num = (year - 1) // 100 + 1
    
    suffix = 'th'
    if century_num % 100 not in [11, 12, 13]:
        if century_num % 10 == 1:
            suffix = 'st'
        elif century_num % 10 == 2:
            suffix = 'nd'
        elif century_num % 10 == 3:
            suffix = 'rd'
    
    return f"{century_num}{suffix}"
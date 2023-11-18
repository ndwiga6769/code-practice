# Complete the solution so that the function will break up camel casing, using a space between words.

# Example
# "camelCasing"  =>  "camel Casing"
# "identifier"   =>  "identifier"
# ""             =>  ""



def break_camel_case(s):
    result = ''
    for char in s:
        # Check if the character is uppercase
        if char.isupper():
            # Add a space before the uppercase letter
            result += ' ' + char
        else:
            # Keep appending characters to the result
            result += char
    return result

# Test cases
print(break_camel_case("camelCasing"))  # Output: "camel Casing"
print(break_camel_case("identifier"))  # Output: "identifier"
print(break_camel_case(""))           # Output: ""

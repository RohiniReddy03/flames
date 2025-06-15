def remove_common_letters(name1, name2):
    name1_list = list(name1)
    name2_list = list(name2)

    for char in name1[:]:  # copy of name1
        if char in name2_list:
            name1_list.remove(char)
            name2_list.remove(char)

    total_count = len(name1_list) + len(name2_list)
    return total_count

def flames_game(name1, name2):
    name1 = name1.lower().replace(" ", "")
    name2 = name2.lower().replace(" ", "")
    
    count = remove_common_letters(name1, name2)
    
    flames = ["F", "L", "A", "M", "E", "S"]
    
    while len(flames) > 1:
        index = (count % len(flames)) - 1
        
        if index >= 0:
            # Rotate list by removing index element and appending the rest
            right = flames[index+1:]
            left = flames[:index]
            flames = right + left
        else:
            flames = flames[:len(flames)-1]  # if index is -1, remove last letter

    # Final result
    result = {
        "F": "Friends",
        "L": "Love",
        "A": "Affection",
        "M": "Marriage",
        "E": "Enemies",
        "S": "Siblings"
    }

    return result[flames[0]]

# Example usage:
name1 = input("Enter first name: ")
name2 = input("Enter second name: ")

relationship = flames_game(name1, name2)
print("Relationship is:", relationship)

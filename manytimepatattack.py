ef find_letter(s):
    #Returns the position of a given letter in a given string
    position = []
    for index in range(len(s)):
        #There may be more cases where whitespace is odd or zero
        if (s[index] >= 'A' and s[index] <= 'Z') or (s[index] >= 'a' and s[index] <= 'z') or s[index] == chr(0):
            # space_counts[index] += 1
            position.append(index)
    return position

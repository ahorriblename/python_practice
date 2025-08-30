def get_min_deletions(user_string):
    deletion_num = 0
    frequency = {}
    seen_once = []
    seen_twice = []

    for char in user_string:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    
    for value in frequency.values():
        if value not in seen_once and value not in seen_twice:
            seen_once.append(value)
        elif value in seen_once:
            seen_twice.append(value)
            seen_once.remove(value)

    if len(seen_twice) == 0:
        return deletion_num
    
    for value in frequency.values():
        i = 1

        if value in seen_twice:
            while True:
                deletion_num = i
                if value - i not in seen_once:
                    break
                i += 1
    
            seen_once.append(value - i)
            seen_once.append(value)
            seen_twice.remove(value)

    print(seen_once)
    print(seen_twice)

    return deletion_num

print(get_min_deletions("aaabbccedddd"))
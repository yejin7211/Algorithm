def solution(new_id):
    # 1단계
    id = new_id.lower() 
    
    # 2단계
    for c in id: 
        if c.isalpha() or c.isdigit() or c == '-' or c == '_' or c == '.':
            continue
        id = id.replace(c, '')

    # 3단계
    i = 0
    while i < len(id): 
        if i + 1 < len(id) and id[i] == '.' and id[i + 1] == '.':
            id = id[0:i] + id[i+1:]
            i -= 1
        i += 1

    # 4단계
    if id[0] == '.': 
        id = id[1:]
    if id != '' and id[len(id) - 1] == '.':
        id = id[0:len(id) - 1]    
    
    # 5단계
    if id == '':
        id = 'a' 
        
    # 6단계
    if len(id) >= 16: 
        id = id[0:15]
        if id[14] == '.':
            id = id[0:14]

    # 7단계
    while len(id) <= 2: 
        id += id[len(id) - 1]
        
    return id
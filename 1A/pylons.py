def sequence(r, c):
    visited = []
    x = (abs(c-r) % (c + 1))
    if( x == 0 ):
        x = 1
    y = r
    
    for i in range(1, r//2):
        for j in range(1, c//2):
            if( x == j or 
                y == i or 
                y - x == i - j or 
                y + x == i + j 
            ):
                return None
            visited.append([x, y])
            visited.append([i, j])

            x = (x + 1) % (c + 1)
            if( x == 0 ):
                x = 1
            if( x == abs(c-r) ):
                y -= 1



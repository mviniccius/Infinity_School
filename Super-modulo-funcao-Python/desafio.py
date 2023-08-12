def percorrer(num: int) -> int:    
    if num == 0:
        return 1
    print(num)
    
    return percorrer(num-1)
    
    
percorrer(4)
        
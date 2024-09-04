def string_compare(P:str, T:str, i:int, j:int) -> int:
    if i == 0:
        return len(T)
    
    if j == 0:
        return len(P)
    else:
        zamian = string_compare(P, T, i-1, j-1)
        wstawien = string_compare(P,T,i,j-1)
        usuniec = string_compare(P,T,i-1,j) 

    min_cost = min(zamian, wstawien, usuniec)

    return min_cost

def PD(P:str, T:str, i:int, j:int) -> int:
    if i == 0:
        return len(T)
    
    if j == 0:
        return len(P)
    else:
        zamian = string_compare(P, T, i-1, j-1)
        wstawien = string_compare(P,T,i,j-1)
        usuniec = string_compare(P,T,i-1,j) 

    min_cost = min(zamian, wstawien, usuniec)

    return min_cost

def main():
    P = "kot"
    T = "pies"

    result = string_compare(P, T, 2, 3)
    print(result)

main()
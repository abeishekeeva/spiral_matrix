import json 

def parse_str_matrx(str_matrx):
    arr = []
    response = str_matrx.replace('+', '').replace('-', '').replace('|','')
    
    for line in response.splitlines():
        num_arr = [int(i) for i in line.split()]
        if num_arr:
            arr.append(num_arr)
    return arr 

def spiral_matrix_in_counterclock(matrix):
    size = len(matrix) 
    flag = 0
    k, i = 0, size 
    result_arr = []

    while(i > 0): 
  
        for j in range(flag,i): 
            result_arr.append(matrix[j][k])
        i = i - 1 
        k = j 
  
        if (i > 0): 
            for j in range(size - i,i + 1): 
                result_arr.append(matrix[k][j])
            for j in range(k-1,size-i-2,-1): 
                result_arr.append(matrix[j][k])
        else: break
        k = j 
        i = i-1
  
        if (i > 0):  
            for j in range(i,size - i-2,-1): 
                result_arr.append(matrix[k][j])
            k,i = k+1,i+1
            flag = flag + 1
        else: break
    
    return result_arr

def error_handler(err):
    error = json.loads(err)
    
    return {
        "err_code": error.code,
        "err_text": error.message
    }

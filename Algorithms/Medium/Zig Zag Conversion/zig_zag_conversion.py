def convert(s: str, numRows: int):
    if(numRows == 1):
        return s
    matrix = [ [] for x in range(numRows)]
    index_rows = 0
    down = True
    for letter in s:
        matrix[index_rows].append(letter)
        if down:
            index_rows = index_rows + 1
            if index_rows == numRows - 1:
                down = False
                continue
            continue
        index_rows = index_rows - 1
        if index_rows == 0:
            down = True
            continue
    result = ""
    for i in matrix:
        for j in i:
            result = result + j
    return result

def convert2(s: str, numRows: int):
    if(numRows == 1):
        return s
    arr = [ "" for x in range(numRows)]
    index_rows = 0
    down = True
    for letter in s:
        arr[index_rows] = arr[index_rows] + letter
        if down:
            index_rows = index_rows + 1
            if index_rows == numRows - 1:
                down = False
                continue
            continue
        index_rows = index_rows - 1
        if index_rows == 0:
            down = True
            continue
    return "".join(arr)

#wrong
def convert3_(s: str, numRows: int):
    if(numRows == 1):
        return s
    arr = [ "" for x in s]
    round = 0
    current_numRows = numRows - round
    step = 2*current_numRows - 2
    index = 0
    i = 0
    while(True):
        
        if round + (index*step) < len(s) and i < len(s):
            arr[i] = s[round + index*step]
            index = index + 1
            i = i + 1
            continue
        round = round + 1
        if(round == numRows):
            break
        index = 0
        current_numRows = numRows - round
        if(current_numRows == 1):
            current_numRows = numRows

        step = 2*current_numRows - 2
        if(current_numRows == 2):
            step = 1
    return "".join(arr)

def convert3(s: str, numRows: int):
    if(numRows == 1):
            return s
    arr = [ "" for x in s]
    round = 0
    index = 0
    i = 0
    down = True
    last_down_index = 0
    while(True):
        if down:
            
            current_numRows = numRows - round
            if(current_numRows == 1):
                current_numRows = numRows
            step = 2*current_numRows - 2
            last_down_index = round + (index*step)
            if last_down_index < len(s):
                print(current_numRows, step)
                print("down", "round:",round, "["+str(s[last_down_index])+  str(i) + "]", index)
                
                arr[i] = s[last_down_index]
                index = index + 1
                i = i + 1
                if(round == 0 or round == numRows - 1):
                    continue
                down = False
                continue
            round = round + 1
            if(round == numRows):
                break
            index = 0

            down = False
            continue
        #if not down
        #index of the letter in up round = last down index + step
        current_numRows = round
        if(current_numRows == 1):
            current_numRows = numRows
        
        step = 2*round 
        target = round+(index*step)
        if index != 0:
            target = last_down_index + step
            
        if  target < len(s):
            print(current_numRows, step)
            print("up", "round:",round, "["+str(s[target])+  str(i) + "]", index)
            
            arr[i] = s[target]
            index = index + 1
            i = i + 1
            down = True
            continue
        round = round + 1
        if(round == numRows):
            break
        index = 0
        down = False
        continue
    return "".join(arr)

s = "PAYPALISHIRING"
numRows = 3

s = "PAYPALISHIRING"
numRows = 5

print("s:\t\t",s)
print("s zigzag:\t",convert(s,numRows))
print("s zigzag2:\t",convert2(s,numRows))
print("s zigzag3:\t",convert3(s,numRows))



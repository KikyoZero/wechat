n = 0
total = 0
while total < 1000:
    n += 1
    total += n * n
    
n -= 1
print("满足条件的值为:", n)

def sq():
    n = 1
    while (n * (n + 1) * (2 * n + 1)/6) <1000:
        n += 1
    return n - 1 
# 调用函数并打印结果
result = sq()
print('满足条件的值为：', result)


#x = 1*1 + 2 *2 + 3*3 +4*4+5*5+6*6+7*7+8*8+9*9+10*10+11*11+12*12+13*13+14*14
print(x)

#y = 14* (14+1) * (2*14+1)/6
#print(y)
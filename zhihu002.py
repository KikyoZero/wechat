# Python中求1-100之间不能被7整除的数之和
def sum_result():
    total = 0
    for num in range(1, 101):
        if num % 7 != 0:
            total += num
    return total

# 调用函数并打印结果
#result = sum_result()
print("结果为", sum_result())
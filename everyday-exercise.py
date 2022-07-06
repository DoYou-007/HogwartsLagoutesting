"""
4月8号：
回文是指一段数字或者文本，正着读和倒着读都是相同的，例如2002，110011都是回文数字。
请编写一个函数，接收一个数字参数num，返回num中所有数字能够组成回文数字的列表，按升序排列，不允许重复。
个位数字和前后是0的数字（010和00）不被视为回文数字。如果不满足条件则返回空列表。

【示例】
输入：1221
输出：[22, 1221]
解释：数字1221中，1221整体是回文数字，22也是回文数字，因此按升序排列后为[22, 1221]。

题目难度：中等
题目来源：CodeWars-Numerical Palindrome #3.5 6

def solution(num: int)-> list:
    # your code here

assert solution(1221) == [22, 1221]
assert solution(34322122) == [22, 212, 343, 22122]
assert solution(1001331) == [33, 1001, 1331]
assert solution(13598) == []

"""
# num =int(input("输入一个数字"))
from collections import Counter


def solution(num):
    j = 0
    num_list = []
    mub = str(num)
    if num > 10:
        while j < len(mub):
            for k in range(len(mub)-j):
                re = mub[j:len(mub)-k]
                if re == re[::-1] and re[0:1] != 0 and int(re)> 10:
                    num_list.append(int(re))
            j += 1

        return sorted(list(set(num_list)))
    else:
        return []


# print(solution(num))






"""
5月11号
给定两个数字列表，请编写一个函数，从第一个列表nums_a中移除所有在第二个列表nums_b中出现的元素，返回剩下元素组成的列表。

【示例】
输入：[1, 1, 2 ,3 ,1 ,2 ,3 ,4], [1, 3]
输出：[2, 2, 4]
解释：第一个列表剔除所有的数字1和3之后，最终剩下[2, 2, 4]

题目难度：简单
题目来源：CodeWars 10

def solution(nums_a: list, nums_b: list)-> list:
  # your code here

assert solution([1, 1, 2 ,3 ,1 ,2 ,3 ,4], [1, 3]) == [2, 2, 4]
assert solution([8, 2, 7, 2, 3, 4, 6, 5, 4, 4, 1, 2 , 3], [2, 4, 3]) == [8, 7, 6, 5, 1]
assert solution([1, 1, 2 ,3 ,1 ,2 ,3 ,4, 4, 3 ,5, 6, 7, 2, 8], [1, 3, 4, 2]) == [5, 6 ,7 ,8]
"""

def solution(nums_a:list,nums_b:list ):
    del_num ={}
    for i in nums_b:
       del_num[i]=nums_a.count(i)
    print("del_num的值：",del_num)
    for j in del_num:
        for k in range(del_num[j]):
            nums_a.remove(j)
    return nums_a

def solution1(nums_a1:list,nums_b1:list):
    for x in nums_b1:
        while x in nums_a1:
            nums_a1.remove(x)

    return nums_a1

#方法 solution 的简化版本
def solution2(nums_a2:list,nums_b2:list):
    map = Counter(nums_a2)
    for i in nums_b2:
        if i in map.keys():
            map.pop(i)
    return list(map.elements())



# print(solution2([1, 1, 2, 3, 1, 2, 3, 4], [1, 3]))
# print(solution2([8, 2, 7, 2, 3, 4, 6, 5, 4, 4, 1, 2, 3], [2, 4, 3]))
# print(solution2([1, 1, 2, 3, 1, 2, 3, 4, 4, 3, 5, 6, 7, 2, 8], [1, 3, 4, 2]))


"""
5月12号
 给定一个由点号 . 和算术运算符组成的字符串，请编写一个函数，计算它们所对应数字算式的结果。计算规则只需要支持四种即可：加法（"+"）、减法（"-"）、乘法（"*"）、整除（"//"）。

示例：
输入： "..... - ..."
输出： ".."
解释：该算式翻译成数字为 5-3，所以结果是2，再翻译成点号为"…"

题目难度：简单
题目来源：CodeWars：Dot Calculator 11

def solution(operation: str) -> str:
    # your code here

assert solution("..... + ...............") == "...................."
assert solution("..... - ...") == ".."
assert solution("..... * ...") == "..............."
assert solution("..... // ..") == ".."
"""


def solution4(operation:str):
    num = operation.split()
    num_add = eval(str(len(num[0])) + num[1] + str(len(num[2])))
    return '.' * num_add


print(solution4("..... + ..............."))
print(solution4("..... - ..."))
print(solution4("..... * ..."))
print(solution4("..... // .."))
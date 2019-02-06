"""
    regex中的分组，在正则中对部分规则添加小括号
    1- match结果的group无参数的把匹配的**全部**取出来
    2- match.group(1) 取出匹配正则中第一个小括号的内容
    3- 先是判断是否匹配整个正则，然后取出部分内容符合小括号的内容
    4- 正则中的 | 表示or, 但是表示的是|前的”所有“or上竖线后的**所有**
"""

import re

"""
    1- |        匹配 左右任意一个表达式
    2- (a,b)    将括号内的作为一个分组
    3- \num     引用分组num匹配到的字符串,配合小括号使用，引用第几个小括号中的正则
    4- ?P<别名>  分组起别名
    5-      
"""
def testRegex01():

    result1 = re.match(r"(\d{3,4})-?(\d{7,8})", "0531-12345678").group(1)
    result2 = re.match(r"(\d{3,4})-?(\d{7,8})", "0531-12345678").group(2)
    print(result1)  # 0531
    print(result2)  # 12345678

    # 竖线前的所有 or 上竖线后的所有
    result3 = re.match(r"(\d{3,4})-?\d{7}|\d{8}", "0531-12345678").group()
    result4 = re.match(r"(\d{3,4})-?\d{8}|\d{7}", "0531-12345678").group()
    print(result3)
    print(result4)

    # .*表示任意内容, \num     引用分组num匹配到的字符串
    html_str = "<h1>Hello World</h1>"
    result5 = re.match(r"<(.*)>.*</\1>",html_str).group()

    # 注意 \num 引用括号的顺序
    html_str2 = "<h1><a>Hello World</a></h1>"
    result6 = re.match(r"<(.*)><(.*)>.*</\2></\1>",html_str2).group()

    # ?P<别名> --> (?P=group1)
    html_str3 = "<h1><a>Hello World</a></h1>"
    result7 = re.match(r"<(?P<group1>.*)><(.*)>.*</\2></(?P=group1)>",html_str3).group()
    print(result7)


def main():
    testRegex01()


if __name__ == '__main__':
    main()

"""
    枯燥的regex正则表达式，使用的是re模块
    1- re.match(正则表达式，需要处理的str)来匹配 -->  a Match object, or None if no match was found.
    2- match(r"",str) 在第一个参数的**外面**需要写一个小写的r来表示这是一个regex
"""

import re


def test_regex01():

    # <re.Match object; span=(0, 3), match='终结者'>
    result1 = re.match(r"终结者", "终结者1")
    print(result1)

    # <re.Match object; span=(0, 4), match='终结者1'>
    result2 = re.match(r"终结者1", "终结者2")
    print(result2)

    # 有返回值group取出来自己期望的值
    if result2:
        print(result2.group())

    # \d
    result3 = re.match(r"终结者\d", "终结者1").group()
    result4 = re.match(r"终结者\d", "终结者2").group()
    result5 = re.match(r"终结者\d", "终结者3").group()

    print(result3)
    print(result4)
    print(result5)


"""
    匹配单个字符，小写为正，大写为非正
    1- \d 匹配数字，即0-9
    2- \D 匹配非数字，即不是数字
    3- \w 小写，大写，数字，下划线，中文也行 (word)
    4- \W 匹配非(小写，大写，数字，下划线，中文)
    5- [] 匹配中括号中制定的一个字符
    6- \s 匹配空格(tab,space)
    7- \S 匹配非空格(tab,space)
    8- .  匹配任意一个字符，除了\n(换行)
    9- $  匹配结尾[a-zA-Z_][a-zA-Z_0-9]*$
   10- ^  匹配开头^[a-zA-Z_][a-zA-Z_0-9]*，默认就是^，可以略写
    
"""
def testRegex02():

    # \d
    result1 = re.match(r"终结者\d", "终结者1").group()
    # []里面任何的**一个**字符
    result2 = re.match(r"终结者[abcdef]", "终结者a").group()
    # \w
    result3 = re.match(r"终结者\w", "终结者_").group()
    # \s
    result4 = re.match(r"终结者\s\d", "终结者\t3").group()
    # .
    result5 = re.match(r"终结者\s.", "终结者\t3").group()
    # [混合模式] 中间不存在分隔符
    result6 = re.match(r"终结者\s[1-9a-zA-W]", "终结者\tX").group()

    print(result6)

"""
    匹配多个字符
    1- 单个字符后+大括号：\d{3} == \d\d\d
    2- 大括号只表示其前面的**单个字符**，而不是一坨
    3- 大括号中没有分隔符表示其中之一，有逗号的是或的关系
    
    1- {m}   匹配一个字符出现m次
    2- {m,n} 匹配一个字符出现m到n次
    3- ?     匹配一个字符出现1次或者0次都行，一次或者0次 -?
    4- *     匹配一个字符出现0次或者无线次都行，可有可无 -*
    5- +     匹配一个字符出现1次或者无限次都行，至少有一次 -+
"""
def testRegex03():
    # 单匹配中，str从头开始，主要判断\d是不是后面str的子集
    result1 = re.match(r"\d.", "13400003456").group()
    # 多匹配,开通必须是1，后面10个数字
    result2 = re.match(r"1\d{10}", "13400003456").group()
    # 匹配开头是1，第二位数3-9
    result3 = re.match(r"1[3-9]\d{9}", "13400003456").group()
    # 匹配开头是1，第二位数3-9,最后一位不是4
    result4 = re.match(r"1[3-9]\d{8}[0-35-9]", "13400003456").group()
    # 匹配开头是1，第二位数3-9,最后一位不是4,也不是7
    result5 = re.match(r"1[3-9]\d{8}[0-35689]", "13400003456").group()
    # 判断电话号码是不是7位数**或者**8位数
    result6 = re.match(r"\d{7,8}", "12345678").group()
    # 判断区号是不是3位数**或者**4位数
    result7 = re.match(r"\d{3}-\d{7,8}", "010-12345678").group()
    # 判断区号是不是3位数**或者**4位数
    result8 = re.match(r"\d{3,4}-\d{7,8}", "0234-12345678").group()
    # 判断区号是不是3位数**或者**4位数, 出现1次或者0次的-
    result9 = re.match(r"\d{3,4}-?\d{7,8}", "0234-12345678").group()
    # 判断数字的个数，至少一个数字以上
    result10 = re.match(r"\d+", "0234-12345678").group()
    # 判断数字的个数，至少5个数字以上，类似于str的切割
    result11 = re.match(r"\d{5,}", "0234-12345678").group()

"""
    判断变量是不是符合要求
"""
def testRegex04():

    # 定义一个列表，存储多个变量名
    name_list = ["age", "name", "_age", "3_age", "age_3", "age_3#"]
    # 通过正则来遍历判断每一个元素
    for temp in name_list:
        # 开头是[a-zA-Z_]
        # 一直到结尾必须是[a-zA-Z_0-9]，0次或者无限次
        result = re.match(r"^[a-zA-Z_][a-zA-Z_0-9]*$", temp)
        if result:
            print("变量名：%s符合命名要求." % temp)
        else:
            print("变量名：%s不符合命名要求." % temp)


def main():
    # test_regex01()
    # testRegex02()
    # testRegex03()
    testRegex04()


if __name__ == '__main__':
    main()

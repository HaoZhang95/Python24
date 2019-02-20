"""
    python中的数据库操作，也就是java中的jdbc，引入Python DB 模块：pymysql
"""
import pymysql


def test01():

    # 听过pymysql获取connection对象
    conn = pymysql.connect(host='localhost',port=3306,database='jing_dong',user='root',password='haozhang',charset='utf8')

    # 获取connection的cursor游标对象
    cur = conn.cursor()

    # 数据是通过cursor游标来获取的
    count = cur.execute("select * from goods;")
    print("查询到了%d 条数据" % count)

    # fetchmany(5) 返回的是一个嵌套元组， fetch方法返回的是元组
    a_record = cur.fetchone()
    print(a_record)

    # # 更新
    # count = cs1.execute('update goods_cates set name="机械硬盘" where name="硬盘"')
    # # 删除
    # count = cs1.execute('delete from goods_cates where id=6')

    # 提交之前的操作，如果之前已经之执行过多次的execute，那么就都进行提交
    conn.commit()

    # 关闭Cursor对象
    cur.close()
    # 关闭Connection对象
    conn.close()


def test02():

    # 获取用户输入的商品名字
    item_name = input("请输入商品的名字:")

    # 连接数据库
    conn = pymysql.connect(
        host="localhost", port=3306, database="jing_dong",
        user="root", password="haozhang", charset="utf8")

    # 获取游标对象
    cursor = conn.cursor()

    """
       sql注入问题， where name = " or 1=1 or", 就会显示全部的数据
       防止sql注入，使用execute带参数，execute方法有一定的sql注入过滤功能，不要手动拼接sql
       cursor.execute(sql, [item_name])
       execute的参数化查询like语句会查不到，原因未知
   """
    # sql = """select * from goods where name = %s;"""
    sql = """select * from goods where name like "%%s%";"""
    print(sql)
    # sql = """select * from goods where name = %s;"""

    # 执行查询语句,
    count = cursor.execute(sql, [item_name])
    print("查询到了%d 条数据" % count)

    # 显示查询结果
    result = cursor.fetchall()
    print(result)

    # 关闭
    cursor.close()
    conn.close()


def main():

    # test01()
    test02()


if __name__ == "__main__":
    main()
-- 数据库的操作

    -- 链接数据库
    -- mysql -u用户名 -p密码
    mysql -uroot -pmysql
    mysql -uroot -p  -- 回车以后 输入密码

    -- 退出数据库
    exit,quit,ctrl-d

    -- sql语句最后需要有分号;结尾
    -- 显示数据库版本
    SELECT VERSION();

    -- 显示时间
    SELECT now();

    -- 查看所有数据库
    show DATABASES;
    

    -- 创建数据库
    -- create database 数据库名 charset=utf8;
    CREATE DATABASE python_24;
    CREATE DATABASE python_24 charset=utf8;


    -- 查看创建数据库的语句
    -- show crate database ....
    show CREATE DATABASE python_24;

    -- 查看当前使用的数据库
    SELECT DATABASE();

    -- 使用数据库
    -- use 数据库的名字
    USE python_24;

    -- 删除数据库
    -- drop database 数据库名;
    drop database python_24;


-- 数据表的操作

    -- 查看当前数据库中所有表
    show tables;

    -- char 和 varchar的区别， char(5) 不够的使用空格占位， varchar(5)实际几个字符就是几个字符
    -- 创建表的基本用法
    -- auto_increment表示自动增长
    -- not null 表示不能为空
    -- primary key 表示主键
    -- default 默认值
    -- create table 数据表名字 (字段 类型 约束[, 字段 类型 约束]);
    -- create table students(字段的名字 类型 约束, 字段2的名字 类型 约束);
    -- 创建students表(id、name、age、high、gender、cls_id)
    CREATE TABLE students
    (
        id int unsigned not NULL primary key auto_increment,
        name VARCHAR(30) not NULL,
        age TINYINT unsigned DEFAULT 0,
        hight DECIMAL(5, 2),        
        gender enum("男", "女", "保密", "第三性别") DEFAULT "保密",
        cls_id int unsigned
    );

    -- 作业创建一个classes表，里面有2个字段(id name)

    -- 查看表结构
    -- desc 数据表的名字;
    desc students

    -- 查看表的创建语句
    -- show create table 表名字;
    show create table students;

    -- 修改表-添加字段
    -- alter table 表名 add 列名 类型;
    ALTER TABLE students add birth DATETIME;

    -- 修改表-修改字段：不重命名版
    -- alter table 表名 modify 列名 类型及约束;
    ALTER TABLE students MODIFY birth DATE;

    -- 修改表-修改字段：重命名版
    -- alter table 表名 change 原名 新名 类型及约束;
    ALTER TABLE students change birth birthday DATE DEFAULT "2000-01-01";

    -- 修改表-删除字段
    -- alter table 表名 drop 列名;
    ALTER TABLE students DROP cls_id;

    -- 删除表
    -- drop table 表名;
    -- drop database 数据库;
    -- drop table 数据表;
    -- drop table students;

    
-- 增删改查(curd)

    -- 增加
        -- 全列插入
        -- insert [into] 表名 values(...)
        -- 主键字段 可以用 0  null   default 来占位
        -- 向classes表中插入 一个班级

        +----------+-------------------------------------------+------+-----+------------+----------------+
        | Field    | Type                                      | Null | Key | Default    | Extra          |
        +----------+-------------------------------------------+------+-----+------------+----------------+
        | id       | int(10) unsigned                          | NO   | PRI | NULL       | auto_increment |
        | name     | varchar(30)                               | NO   |     | NULL       |                |
        | age      | tinyint(3) unsigned                       | YES  |     | 0          |                |
        | high     | decimal(5,2)                              | YES  |     | NULL       |                |
        | gender   | enum('男','女','保密','第三性别')         | YES  |     | 保密       |                |
        | birthday | date                                      | YES  |     | 2000-01-01 |                |
        +----------+-------------------------------------------+------+-----+------------+----------------+

        -- 向students表插入 一个学生信息
        INSERT INTO students VALUES (0, "曹操", 18, 178.8, "男", "1990-11-21");
        insert into students values (0, "曹真", 19, 170.8, "男", "1991-11-11");
        insert into students values (null, "曹丕", 19, 170.8, "男", "1991-11-11");
        insert into students values (default, "曹植", 19, 170.8, "男", "1991-11-11");

        -- 失败
        -- insert into students values(default, "司马懿", 20, 201.1, "第4性别", "1990-02-01");

        -- 枚举中 的 下标从1 开始 1---“男” 2--->"女"....
        INSERT INTO students VALUES(null, "司马懿", 20, 188.8, 1, "1990-02-01");
        insert into students values(default, "小乔", 20, 201.1, 2, "1990-02-01");

        -- 部分插入
        -- insert into 表名(列1,...) values(值1,...)
        INSERT into students (name, gender) VALUES("吕布", "男");

        -- 多行插入
        INSERT INTO students (name, gender) VALUES ("张飞", "男"), ("赵云", "男");
        INSERT INTO students VALUES (default, "貂蝉", 19, 170.8, "女", "1991-11-11"), (default, "孙尚香", 20, 170.8, "女", "1991-11-11");


    -- 修改
    -- update 表名 set 列1=值1,列2=值2... where 条件;
    UPDATE students SET age=22 where id=8;
    

    -- 查询基本使用
        -- 查询所有列
        -- select * from 表名;
        select * from students;

        -- 定条件查询
        select * from students where gender="女";
        select * from students where age<20;

        -- 查询指定列
        -- select 列1,列2,... from 表名;
        SELECT name, gender FROM students;

        -- 字段的顺序
        SELECT gender, name from students;

        -- 可以使用as为列或表指定别名
        -- select 字段[as 别名] , 字段[as 别名] from 数据表 where ....;
        SELECT name as 姓名, gender as 性别 FROM students;


    -- 删除
        -- 物理删除
        -- delete from 表名 where 条件
        -- delete from students; -- 这意味着清空数据表的所有数据
        DELETE FROM students where id=9 or id=10;

        -- **逻辑删除**,欺骗用户的删除
        -- 用一个字段来表示 这条信息是否已经不能再使用了
        -- 给students表添加一个is_delete字段 bit 类型， 1 byte = 8 bits, 一个bit要么0 or 1， 但是不够一个字节，显示不出来
        ALTER table students add is_delete BIT(1) default 0;

        UPDATE students set is_delete=1 where id=6;

        SELECT * FROM students WHERE is_delete=0;










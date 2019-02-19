-- 数据的准备
    -- 创建一个数据库
    CREATE DATABASE python_24_1 charset=utf8;

    -- 使用一个数据库
    USE python_24_1;

    -- 显示使用的当前数据库是哪个?
    SELECT DATABASE();

    -- 查询当前mysql系统中所有的数据库
    show DATABASES;

    -- 创建students表
    -- 字段有id,name,age,height,gender,cls_id,is_delete
    create table students(
        id int unsigned primary key auto_increment not null,
        name varchar(20) default '',
        age tinyint unsigned default 0,
        height decimal(5,2),
        gender enum('男','女','中性','保密') default '保密',
        cls_id int unsigned default 0,
        is_delete bit default 0
    );


    -- 创建classes表
    -- 字段有id,name
    -- classes表
    create table classes (
        id int unsigned auto_increment primary key not null,
        name varchar(30) not null
    );

    -- 插入数据
    -- 向students表中插入数据
    insert into students values
    (0,'小明',18,180.00,2,1,0),
    (0,'小月月',18,180.00,2,2,1),
    (0,'彭于晏',29,185.00,1,1,0),
    (0,'刘德华',59,175.00,1,2,1),
    (0,'黄蓉',38,160.00,2,1,0),
    (0,'凤姐',28,150.00,4,2,1),
    (0,'王祖贤',18,172.00,2,1,1),
    (0,'周杰伦',36,NULL,1,1,0),
    (0,'程坤',27,181.00,1,2,0),
    (0,'刘亦菲',25,166.00,2,2,0),
    (0,'金星',33,162.00,3,3,1),
    (0,'静香',12,180.00,2,4,0),
    (0,'郭靖',12,170.00,1,4,0),
    (0,'周杰',34,176.00,2,5,0);

    -- 向classes表中插入数据
    insert into classes values (0, "python_01期"), (0, "python_02期");

-- 查询
    -- 查询所有字段
    -- select * from 表名;
    -- 查询students、classes表中的所有数据
    SELECT * FROM students;
    SELECT * FROM classes;

    -- 查询指定字段
    -- select 列1,列2,... from 表名;
    -- 从students表中查询name,age字段
    SELECT name, age FROM students;
    
    -- 使用 as 给字段起别名
    -- select 字段 as 名字.... from 表名;
    -- 从students表中查询name,age字段，并且将name命名为姓名，将age命名为年龄
    SELECT name as 姓名, age as 年龄 FROM students;

    -- select 表名.字段 .... from 表名;
    -- 从students表中查询name,age字段，字段使用 数据表名.字段名的方式
    SELECT students.name as 姓名, students.age as 年龄 FROM students;
    
    -- 可以通过 as 给表起别名
    -- select 别名.字段 .... from 表名 as 别名;
    -- 从students表中查询name,age字段，并且给students表命名为s，字段使用 数据表别名.字段名的方式
    -- 失败的select students.name, students.age from students as s;  -- 已经给数据表起别名后，不能再使用原数据表的名字
    SELECT s.name as 学生姓名, s.age as 学生年龄 from students as s;

    -- 消除重复行
    -- distinct 字段
    -- 查询students表中所有的不重复的性别
    SELECT DISTINCT gender from students;

-- 条件查询
    -- 比较运算符
        -- select .... from 表名 where .....
        -- >
        -- 查询students表中，年龄大于18岁的所有信息
        select * from students where age>18;

        -- 查询students表中，年龄大于18岁的id,name,gender
        select id, name, gender from students where age>18;

        -- <
        -- 查询students表中，年龄小于18岁的所有信息
        select * from students where age<18;

        -- >=
        -- <=
        -- 查询小于或者等于18岁的信息
        select * from students where age<=18;

        -- =
        -- 查询students表中，年龄为18岁的所有学生的信息
        select * from students where age=18;

        -- != 或者 <>
        SELECT * from students where age != 18;


    -- 逻辑运算符
        -- and
        -- 查询students表中，年龄在18到28之间的所有学生信息
        -- 失败select * from students where age>18 and <28;
        -- 失败select * from students where 18<age<28; 查出的是全部数据
        SELECT * FROM students where age >= 18 and age < 28;

        -- 查询students表中，年龄在18岁以上的所有女性的信息
        select * from students where age>18 and gender="女";
        SELECT * FROM students where age > 18 and gender = 2;

        -- or
        -- 查询students表中，年龄在18以上或者身高查过180(包含)以上的所有信息
        SELECT * FROM students WHERE age>18 or height>=180;

        -- not
        -- 查询students表中，年龄 不在 18岁以上的女性 这个范围内的信息
        SELECT * FROM students WHERE not (age>18 and gender=2);

        -- 查询students表中，年龄 不 小于或者等于18 并且 是女性
        SELECT * FROM students WHERE not age<=18 and gender=2;


    -- 模糊查询
        -- like 
        -- % 替换0个或1或多个， 可有任一个的占位符
        -- _ 替换1个，一个占位符
        -- 查询students表中，姓名中 以 "小" 开始的名字
        -- %小% 姓名中包含**小**的记录
        -- 小% 姓名中以**小**开头的记录
        select name from students where name="小";
        select name from students where name like "小%";
        SELECT name from students WHERE name like "_小%";


        -- 查询students表中，姓名中 有 "小" 所有的名字
        select name from students where name like "%小%";

        -- 查询students表中，有2个字的名字
        SELECT name from students where name like "__";

        -- 查询students表中，有3个字的名字
        select name from students where name like "___";

        -- 查询students表中，至少有2个字的名字
        SELECT name from students WHERE name like "__%";

        -- rlike 正则
        -- 查询students表中，以 周开始的姓名
        SELECT name from students WHERE name rlike "^周.*";     -- 查询的是周XX

        -- 查询students表中，以 周开始、伦结尾的姓名
        SELECT name from students WHERE name rlike "^周.*伦$";


    -- 范围查询
        -- in (1, 3, 8)表示在一个非连续的范围内
        -- 查询students表中，年龄为18或者34的姓名
        SELECT name FROM students WHERE age=18 or age=34;
        SELECT name from students WHERE age in (18, 34);

        -- not in 不非连续的范围之内
        -- 查询students表中，年龄不是 18、34岁之间的信息
        SELECT * FROM students WHERE age not in (18, 34);


        -- between ... and ...表示在一个连续的范围内
        -- 查询students表中，年龄在18到34之间的的信息
        SELECT * FROM students WHERE age BETWEEN 18 and 34;
        
        -- not between ... and ...表示不在一个连续的范围内
        -- 查询students表中，年龄不在在18到34之间的的信息
        SELECT * FROM students WHERE age NOT BETWEEN 18 and 34;
        -- 失败的select * from students where age not (between 18 and 34);


    -- 空判断
        -- 判空is null
        -- 查询students表中，没有填写身高的学生的所有信息
        SELECT * FROM students WHERE height is NULL;
        SELECT * FROM students WHERE height = NULL;         -- 查询的是height的值是null的，结果为空

        -- 判非空is not null
        -- 查询students表中，填了了身高的学生的所有信息
        SELECT * FROM students WHERE height is NOT NULL;

-- 排序
    -- order by 字段
    -- asc从小到大排列，即升序
    -- desc从大到小排序，即降序

    -- 查询students表中，年龄在18到34岁之间的男性，按照年龄从小到到排序
    SELECT * FROM students WHERE age>18 and age<34 ORDER BY age ASC;

    -- 查询students表中，年龄在18到34岁之间的男性，身高从高到矮排序
    SELECT * FROM students WHERE age BETWEEN 18 and 34 ORDER BY age DESC;

    -- order by 多个字段
    -- order by 字段1 排序方式, 字段2 排序方式.....
    -- 查询students表中，年龄(包括)在18到34岁之间的女性，身高从高到矮排序, 如果身高相同的情况下按照年龄从小到大排序
    SELECT * FROM students WHERE (age BETWEEN 18 and 34) and (gender=2) ORDER BY height DESC, age ASC;

    -- 查询students表中，年龄在18到34岁之间的女性，身高从高到矮排序, 
    -- 如果身高相同的情况下按照年龄从小到大排序,
    -- 如果年龄也相同那么按照id从大到小排序
    select * from students where age>=18 and age<=34 and gender=2 order by height desc,age asc, id desc;
    
    -- 查询students表中，所有的学生 按照年龄从小到大、身高从高到矮的排序
    select * from students order by age asc, height desc;

-- 聚合函数
    -- 总数
    -- count
    -- 查询students表中，男性有多少人，女性有多少人
    select count(*) from students where gender=1;
    select count(*) from students where gender=2;

    -- 查询students表中，男性有多少人，女性有多少人，并且将查询出来的人数字段起名为 男/女性人数
    select count(*) as "男性的人数" from students where gender=1;
    SELECT count(*) as "女性的人数" FROM students WHERE gender=2;

    -- 最大值
    -- max
    -- 查询students表中，最大的年龄
    SELECT max(height) FROM students;

    -- 查询students表中，女性的最高 身高
    select max(height) from students where gender=2;

    -- 最小值
    -- min
    select min(height) from students where gender=2;

    -- 求和
    -- sum
    -- 在students表中，计算所有人的年龄总和
    select sum(age) from students;
    
    -- 平均值
    -- avg
    -- 在students表中，计算所有的人的平均年龄
    -- 在students表中，计算平均年龄 sum(age)/count(*)
    SELECT avg(age) FROM students;
    SELECT sum(age)/count(*) FROM students;

    -- 四舍五入 round(123.23 , 1) 保留1位小数
    -- 在students表中，计算所有人的平均年龄，保留2位小数
    SELECT round(avg(age), 0) FROM students;
    select round(avg(age),2) from students;

    -- 在students表中，计算男性的平均身高 保留2位小数
    SELECT round(avg(height), 2) FROM students WHERE gender=1;


-- 分组
    -- group by
    -- distinct是直接从表中找不同， group by是先分组，在从**各个组中**select查找
    -- 在students表中，按照性别分组,查询所有的性别
    -- 失败select * from students group by gender;
    select gender from students group by gender;

    -- 在students表中，计算每种性别中的人数
    SELECT gender,count(*) FROM students GROUP BY gender;

    -- 在students表中，计算男性的人数
    -- 先按照gender=1的数据，然后按照gender分组， 最后对分组进行count(*)
    select count(*) from students where gender=1;
    select gender,count(*) from students where gender=1 group by gender;
    SELECT gender, count(*) FROM students WHERE gender=1 GROUP BY gender;

    -- group_concat(...)
    -- 在students表中，查询男性中的姓名
    SELECT gender, group_concat(name) FROM students WHERE gender=1 GROUP BY gender;

    -- having
    -- 在students表中，按照性别分组，查询平均年龄超过30岁的性别，以及姓名 having avg(age) > 30
    SELECT gender, group_concat(name), avg(age) FROM students GROUP BY gender having avg(age)>30;
    
    -- 在students表中，查询每种性别中的人数多于2个的信息
    SELECT gender, group_concat(name),  count(*) FROM students GROUP BY gender HAVING count(*)>2;


-- 分页
    -- limit start, count

    -- 在students表中，限制查询出来的男性信息个数为2
    select * from students limit 2;

    -- 在students表中，查询前5个数据
    SELECT * FROM students limit 5;

    -- 在students表中，查询id6-10（包含）的信息

    -- 在students表中，每页显示2个，第1个页面
    -- limit 0,2 从下标index为0的记录往下开始找2个
    select * from students limit 0, 2;

    -- 在students表中，每页显示2个，第2个页面
    select * from students limit 2, 2;

    -- 在students表中，每页显示2个，第3个页面
    select * from students limit 4, 2;
    
    -- 在students表中，每页显示2个，第4个页面
    select * from students limit 6, 2; -- -----> limit (第N页-1)*每页的个数, 每页的个数;

    -- 在students表中，每页显示2个，显示第6页的信息, 按照年龄从小到大排序
    -- 失败select * from students limit (6-1)*2,2;
    -- 失败select * from students limit 10,2 order by age asc;
    select * from students order by age asc limit 10,2;

    -- 在students表中，查询女性信息 并且按照身高从高到矮排序 只显示前2个
    SELECT * FROM students WHERE gender="女" ORDER BY height DESC limit 0, 2;


-- 连接查询(多张表查询)
    -- inner join ... on

    -- select ... from 表A inner join 表B;

    -- 查询 有能够对应班级的学生以及班级信息
    SELECT * FROM students INNER JOIN classes ON students.cls_id=classes.id;

    -- 按照要求显示姓名、班级
    select students.name, classes.name from students inner join classes on students.cls_id=classes.id;
    select students.name as 姓名, classes.name as 班级 from students inner join classes on students.cls_id=classes.id;
    SELECT s.name as "学生姓名", c.id as "班级" FROM students as s INNER JOIN classes as c on s.cls_id=c.id;

    -- 给数据表起名字
    select s.name, c.name from students as s inner join classes as c on s.cls_id=c.id;

    -- 查询 有能够对应班级的学生以及班级信息，显示学生的所有信息，只显示班级名称
    select s.*, c.name from students as s inner join classes as c on s.cls_id=c.id;
    
    -- 在以上的查询中，将班级姓名显示在第1列
    select c.name , s.* from students as s inner join classes as c on s.cls_id=c.id;

    -- 查询 有能够对应班级的学生以及班级信息, 按照班级进行排序
    -- select c.xxx s.xxx from student as s inner join clssses as c on .... order by ....;
    select c.name , s.* from students as s inner join classes as c on s.cls_id=c.id order by c.name;

    -- 当是同一个班级的时候，按照学生的id进行从小到大排序
     select c.name , s.* from students as s inner join classes as c on s.cls_id=c.id order by c.name, s.id;

    -- left join, 以左边的表为主，一定会把左边的表显示完
    -- 查询每位学生对应的班级信息
    select * from students as s left join classes as c on s.cls_id=c.id;

    -- 查询没有对应班级信息的学生
    -- select ... from xxx as s left join xxx as c on..... where .....
    -- select ... from xxx as s left join xxx as c on..... having .....
    select * from students as s left join classes as c on s.cls_id=c.id having c.id is null;
    select * from students as s left join classes as c on s.cls_id=c.id where c.id is null;

    -- right join   on， 以右边的表为主
    -- 将数据表名字互换位置，用left join完成

-- 自关联
    -- 省级联动 url:http://demo.lanrenzhijia.com/2014/city0605/
    -- 省级联动就是1张表替代7张表，自己表跟自己关联，一张表中的字段引用到了自张表中的字段

    -- 查询所有省份
    select * from areas where pid is null;

    -- 查询出山东省有哪些市
    SELECT * FROM areas as province INNER JOIN areas as city ON province.aid=city.pid HAVING province.atitle="山东省";
    select province.atitle, city.atitle from areas as province inner join areas as city on city.pid=province.aid having province.atitle="山东省";
    SELECT * FROM areas WHERE pid=(SELECT aid FROM areas WHERE title="山东省")

    -- 查询出青岛市有哪些县城
    select province.atitle, city.atitle from areas as province inner join areas as city on city.pid=province.aid having province.atitle="青岛市";
    select * from areas where pid=(select aid from areas where atitle="青岛市")


-- 子查询
    -- 标量子查询
    -- 查询出高于平均身高的信息

    -- 查询最高的男生信息
    select * from students where height = 188;
    SELECT * FROM students WHERE height = (SELECT max(height) FROM students);

    -- 列级子查询
    -- 查询学生的班级号能够对应的学生信息
    -- select * from students where cls_id in (select id from classes);













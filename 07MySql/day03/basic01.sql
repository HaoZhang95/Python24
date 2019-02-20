-- 数据库设计
    -- 冗余，同一张表中出现多次重复的数据，修改起来麻烦。创建多个表，引用表中的id进行显示

    -- 创建商品分类表
    create table if not exists goods_cates(
        id int unsigned not null auto_increment primary key,
        name varchar(40) not null
    );

    -- 查询goods表中商品的种类
    select cate_name from goods group by cate_name;

    -- 将分组结果写入到goods_cates数据表
    insert INTO goods_cates (name) SELECT cate_name FROM goods GROUP BY cate_name;

    -- 通过goods_cates数据表来更新goods表
    -- 失败：UPDATE goods SET cate_name = (SELECT id FROM goods_cates WHERE );
    SELECT * FROM goods as g INNER JOIN goods_cates as gc ON  g.cate_name=gc.name;
    UPDATE goods as g INNER JOIN goods_cates as gc ON g.cate_name=gc.name SET g.cate_name = gc.id;


    -- select brand_name from goods group by brand_name;
    -- 在创建数据表的时候一起插入数据
    -- 注意: 需要对brand_name 用as起别名，否则name字段就没有值
    create table goods_brands (
        id int unsigned primary key auto_increment,
        name varchar(40) not null) select brand_name as name from goods group by brand_name;

    CREATE TABLE goods_brands (
        id INT unsigned PRIMARY KEY auto_increment,
        name VARCHAR(40) NOT NULL
    );

    INSERT INTO goods_brands (name) SELECT brand_name FROM goods GROUP BY brand_name;

    -- 更新goods表中的brand_name使用id替换
    UPDATE goods as g INNER JOIN goods_brands AS gb ON g.brand_name=gb.name SET g.brand_name=gb.id;

    -- 更改goods中的cate_name为cate_id
    ALTER TABLE goods 
    change cate_name cate_id int unsigned NOT NULL,
    change brand_name brand_id int unsigned NOT NULL;


-- 外键约束:对数据的有效性进行验证

    -- 表中的外键约束越多，性能越低。开发中不推荐使用外键, 最好不用外键
    -- 给brand_id 添加外键约束成功
    ALTER TABLE goods add FOREIGN KEY (brand_id) REFERENCES goods_brands(id);
    -- 给cate_id 添加外键失败
    -- 会出现1452错误
    -- 错误原因:已经添加了一个不存在的cate_id值12,因此需要先删除
    ALTER TABLE goods add FOREIGN KEY (cate_id) REFERENCES goods_cates(id);


    -- 需要先获取外键约束名称,该名称系统会自动生成,可以通过查看表创建语句来获取名称
    show create table goods;
    -- 获取名称之后就可以根据名称来删除外键约束
    alter table goods drop foreign key 外键名称;
    ALTER TABLE goods DROP FOREIGN KEY brand_id;


    -- 如何在创建数据表的时候就设置外键约束呢?
    -- 注意: goods 中的 cate_id 的类型一定要和 goods_cates 表中的 id 类型一致
    create TABLE goods(
        id int primary key auto_increment not null,
        name varchar(40) default '',
        price decimal(5,2),
        cate_id int unsigned,
        brand_id int unsigned,
        is_show bit default 1,
        is_saleoff bit default 0,
        foreign key(cate_id) references goods_cates(id),
        foreign key(brand_id) references goods_brands(id)
    );
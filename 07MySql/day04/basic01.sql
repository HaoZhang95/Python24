
-- View试图，一张虚拟的表，临时过渡作用

    -- 在数据库或者表大版本更新的时候，如果新表中修改了大量的旧表中的字段，那么已经存在的sql语句就该大规模修改
    -- 为了防止这种大规模的修改，引入一张虚拟的表View，这个视图中不存有任何的数据，保留view和新表中字段的对应关系
    -- 1- 这样就不需要在sql语句中更改大量的新字段名，而是只更改一个old sheet --> view
    -- 2- 安全作用：新表中如果不想让开发者使用全部的数据字段，只在view视图中对应部分字段供开发者使用
    -- 总结：在不大量更改sql语句的情况下，进行数据库的版本更新

    -- 建议以v_开头
    -- create view 视图名称 as select语句;

    create view v_goods_info as (
        select g.id, g.name, b.name as brand_name, c.name as cate_name, g.price from
            goods as g inner join goods_cates as c on g.cate_id=c.id
                        inner join goods_brands as b on g.brand_id=b.id
    );

    -- 虚拟的表并不存在任何数据，所以不能更改试图数据，只能更改原表中的数据，那么视图中的数据也会被更改
    select * from v_goods_info;


-- 事务：是一个操作序列
    -- 默认的sql语句就是一个事务，默认一句sql就自动commit，手动开启就会让其不自动commit
    -- A扣钱和B加钱，要么同时成功，要么同时失败。

    -- 1- 检查支票账户的余额高于或者等于200美元。
    -- 2- 从支票账户余额中减去200美元。
    -- 3- 在储蓄帐户余额中增加200美元。
    -- 有一个sql执行失败就会rollback回滚

    start transaction;
    select balance from checking where customer_id = 10233276;
    update checking set balance = balance - 200.00 where customer_id = 10233276;
    update savings set balance = balance + 200.00 where customer_id = 10233276;
    --    rollback; commit之前可以手动回滚
    commit;

    -- 事务的死锁
    -- 如果一个client的sql开启了事务，但是没有commit，同时另一个客户端也想操作同一张表，也想commit
    -- 这样第二个客户端的commit就会**超时报错**，被阻塞


-- 索引，一套特殊的数据结构
    -- 是一种特殊的算法，包含数据表中的所有记录的**引用指针**
    -- 数据库索引好比是一本书前面的目录，能加快数据库的查询速度

    -- 查看索引
    show index from 表名;


    -- 创建索引
    -- 如果指定字段是字符串，需要指定长度，建议长度与定义字段时的长度一致
    -- 字段类型如果不是字符串，可以不填写长度部分
    create index 索引名称 on 表名(字段名称(长度))

    -- 建立所里索引虽然会加快某一字段的查询速度，但是会影响插入和更新的速度
    -- 一般索引是添加在经常查询，但是不经常修改的字段上
    -- 索引的原理：二叉树，根据索引的index进行二叉树查找，字段中的一个数据修改，那么整体的二叉树会耗时更新
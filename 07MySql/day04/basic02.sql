-- 数据库的用户权限

    -- 在默认的mysql数据库中的user表
    desc user;

    -- 查看所有用户, % 表示可以远程登陆和本机登陆,任意ip
    select host,user,authentication_string from user;

    +-----------+------+-----------------------+
    | host      | user | authentication_string |
    +-----------+------+-----------------------+
    | localhost | root |                       |
    | 127.0.0.1 | root |                       |
    | ::1       | root |                       |
    | localhost |      | NULL                  |
    +-----------+------+-----------------------+


-- 创建账户、授权

    -- 需要使用实例级账户登录后操作，以root为例
    -- 常用权限主要包括：create、alter、drop、insert、update、delete、select
    -- 如果分配所有权限，可以使用all privileges

    -- grant 权限列表 on 数据库 to '用户名'@'访问主机' identified by '密码';
    -- jing_dong.* 表示jing_dong数据库中的所有表，只授权select和update权限
    grant select, update on jing_dong.* to 'laowang'@'localhost' identified by '123456';

    -- 查看用户有哪些权限
    show grants for laowang@localhost;

    -- 修改用户权限
    grant 权限名称 on 数据库 to 账户@主机 with grant option;

    -- 修改密码, 使用password()函数进行密码加密
    update user set authentication_string=password('新密码') where user='用户名';
    update user set authentication_string=password('123') where user='laowang';
    注意修改完成后需要刷新权限

    -- 更新用户和密码需要刷新权限
    flush privileges;

    -- 删除用户， drop user '用户名'@'主机'; 或者 delete from user where user='用户名';
    drop user 'laowang'@'%';
    delete from user where user='laowang';

    -- 操作结束之后需要刷新权限
    flush privileges


-- mysql的主从同步机制

    -- 导出为sql文件的备份，不能实现实时的备份
    -- 防止数据库挂掉，需要一个备份的数据库，服务器更新一个数据库的同时，这个数据库会自动添加这个数据到备份的数据库
    -- 保障两个数据库数据的实时性，一个数据库挂掉，服务器就会请求备份的数据库，需要设置主从关系，从的数据库只能查

    -- 多个数据库都有同步的数据，所以服务器不需要只从一个数据库取数据，要分配服务器请求给多个数据库，达到负载平衡
    -- 提升服务器对数据库的操作速度

    -- 具体的主从配置步骤省略，不重要
# 查看MySQL日志

作用： 通过查看MySQL日志文件，可以了解用户对数据库作了哪些操作

1. **修改配置，启动`MySQL`日志文件**

	打开 MySQL 的配置文件 `mysqld.cnf`，**删除 68、69 行前面的 # 号注释**

 		sudo vi /etc/mysql/mysql.conf.d/mysqld.cnf

	![image](../imgs/django-031.png)

2. 重启`MySQL`服务

 		sudo service mysql restart

3. **通过 `tail` 命令**，查看`MySQL`日志文件内容

 		sudo tail -f /var/log/mysql/mysql.log
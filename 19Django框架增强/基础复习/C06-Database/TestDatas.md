	
	insert into department(name, create_date, is_delete) values("研发部", "2009-01-01", 0);
	insert into department(name, create_date, is_delete) values("人事部", "2009-03-01", 0);
	insert into department(name, create_date, is_delete) values("财务部", "2008-01-01", 0);
	insert into department(name, create_date, is_delete) values("行政部", "2008-01-02", 1);
	insert into department(name, create_date, is_delete) values("销售部", "2008-01-03", 1);
	
	insert into employee(name, age, gender, salary, hire_date, comment, department_id) values("赵小一", 28, 0, 12000, "2011-01-01", null, 1);
	insert into employee(name, age, gender, salary, hire_date, comment, department_id) values("赵小二", 27, 0, 13000, "2011-01-01", null, 1);
	insert into employee(name, age, gender, salary, hire_date, comment, department_id) values("赵小三", 23, 0, 11000, "2015-01-01", null, 1);
	insert into employee(name, age, gender, salary, hire_date, comment, department_id) values("赵小四", 24, 0, 10000, "2016-01-01", null, 1);
	
	insert into employee(name, age, gender, salary, hire_date, comment, department_id) values("赵小五", 22, 1, 7000, "2017-01-01", null, 2);
	insert into employee(name, age, gender, salary, hire_date, comment, department_id) values("赵小六", 20, 1, 6000, "2013-01-01", null, 2);
	insert into employee(name, age, gender, salary, hire_date, comment, department_id) values("赵小七", 25, 0, 7000, "2014-01-01", null, 2);
	insert into employee(name, age, gender, salary, hire_date, comment, department_id) values("赵小八", 25, 0, 8000, "2014-01-01", null, 2);
	
	insert into employee(name, age, gender, salary, hire_date, comment, department_id) values("马云", 53, 0, 10000, "2011-01-01", "阿里", 3);
	insert into employee(name, age, gender, salary, hire_date, comment, department_id) values("马化腾", 46, 0, 10000, "2010-01-01", "腾讯", 3);
	insert into employee(name, age, gender, salary, hire_date, comment, department_id) values("李彦宏", 49, 0, 10000, "2010-01-01", "百度", 3);
	insert into employee(name, age, gender, salary, hire_date, comment, department_id) values("雷军", 48, 0, 10000, "2012-01-01", "小米", 3);

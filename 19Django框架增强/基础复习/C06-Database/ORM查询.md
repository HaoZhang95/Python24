
### 条件查询

用法：
模型类.objects.filter(模型类属性名__条件名 = 值)

- 判等： exact

		# 例：查询id为1的员工
		select * from employee where id=1;
		Employee.objects.filter(id__exact=1)
		Employee.objects.filter(id=1)

- 模糊查询： contains / endswith / startswith

		# 例：查询名字包含'马'的员工
		select * from employee where name like '%马%';
		Employee.objects.filter(name__contains='马')

		# 例：查询名字以'军'结尾的员工
		select * from employee where name like '%军';
		Employee.objects.filter(name__endswith='军')

- 空查询： isnull 

		# 例：查询备注信息不为空的员工
		select * from employee where comment is not null ;
		Employee.objects.filter(comment__isnull=False)
		
- 范围查询: in

		# 例：查询id编号为1或3或5的员工
		select * from employee where id in (1, 3, 5); 
		Employee.objects.filter(id__in=[1,3,5])

- 比较查询: gt(greater than) lt(less than) gte  lte

		# 例：查询age大于等于30的员工
		select * from employee where age >= 30; 
		Employee.objects.filter(age__gte=30)

- 日期查询： year

		# 例：查询2015年入职的员工
		select * from employee where year(hire_date) = 2015; 
		Employee.objects.filter(hire_date__year=2015)
		
		# 例：查询2014年1月1日后入职的员工
		select * from employee where hire_date >= '2014-1-1';
		Employee.objects.filter(hire_date__gte='2014-1-1')

- 返回不满足条件的数据： exclude

用法： 模型类.objects.exclude(条件)

		# 例：查询id不为3的员工
		select * from employee where id != 3; 
		Employee.objects.exclude(id=3)

### F对象 

用法： F('字段')
`from django.db.models import F`    

	# 例：查询年龄大于id的员工信息（无实际意义）
	select * from employee where age > id; 
	Employee.objects.filter(age__gt=F(‘id’))
	
	# 例：查询年龄大于4倍id编号的员工信息（无实际意义）
	select * from employee where age > id * 4; 
	Employee.objects.filter(age__gt=F(‘id’) * 4 )

### Q对象

用法： Q(条件1) 逻辑操作符 Q(条件2)
    
`from django.db.models import Q`

	例：查询id大于3且年龄大于30的员工信息。
	select * from employee where id > 3 and age > 30; 
	Employee.objects.filter(id__gt=3, age__gt=30)
	Employee.objects.filter(Q(id__gt=3) & Q(age__gt=30))

	例：查询id大于3或者年龄大于30的员工信息。
	select * from employee where id > 3 or age > 30; 
	Employee.objects.filter(Q(id__gt=3) | Q(age__gt=30))
	
	例：查询id不等于3员工信息。
	select * from employee where id != 3; 
	Employee.objects.filter(~Q(id=3))

### order_by方法

用法：
升序： 模型类.objects.order_by('字段名') 
降序： 模型类.objects.order_by('-字段名')


	例：查询所有员工信息，按照id从小到大进行排序。
	select * from employee order by id asc; 
	Employee.objects.order_by('id')

	例：查询所有员工信息，按照id从大到小进行排序。
	select * from employee order by id desc; 
	Employee.objects.order_by('-id')

	例：把id大于3的员工信息, 按年龄从大到小排序显示；
	select * from employee where id > 8 order by age desc; 
	Employee.objects.filter(id__gt=8).order_by('-age')

### aggregate方法

用法： 模型类.objects.aggregate（聚合类（'模型属性'））

	from django.db.models import Sum, Count, Max, Min, Avg

	例：查询所有员工的平均工资
	select avg(salary) from employee; 
	Employee.objects.aggregate(Avg('salary'))

### count方法
用法： 模型类.objects.count()

	例：统计所有员工的人数。
	select count(*) from employee; 
	Employee.objects.count()

	例：统计id大于3的所有员工的人数。
	select count(*) from employee where id > 3; 
	Employee.objects.filter(id__gt=3).count()

### 关联查询 

	例：查询 “研发部” 的所有员工
	# 方式一：
	d = Department.objects.get(name=‘研发部’)
	d.employee_set.all()		# 一查多
	# 方式二：
	Employee.objects.filter(department__name='研发部')

	例：查询 “赵小二” 所属的部门信息
	# 方式一：	
	e = Employee.objects.get(name='赵小二')
	e.department			# 多查一
	# 方式二：
	Department.objects.filter(employee__name='赵小二')


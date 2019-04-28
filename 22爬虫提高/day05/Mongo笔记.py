# # 查看所有的数据库
# show dbs
#
# # 切换数据库,如果数据库不存在，也不会，但是不会创建数据库，只有你往数据库中插入数据时，会默认创建数据库
# use 数据库名称
#
# # 查看当前数据库
# db
#
# # 查看用户,首先必须要切换到admin数据库
# use admin
# show users
#
# # 删除数据库,首先必须要切换到想要删除的数据库
# use python
# db.dropDatabase()
#
# # 创建集合,可以不手动创建集合
# db.createCollection('stu')
#
# # 直接往不存在的集合中插入数据，会默认创建集合
# # 数据的存储的格式都是键值对，如果未指定_id，默认创建，_id是索引
# db.t1.insert({name:"python",age:18})
#
# # 查看集合是否创建成功
# db.collections
#
# # 查看集合中的数据，相当于查看集合中的所有数据
# # 如果数据比较多，默认展示20条,如果要加载更多数据，使用it
# db.t1.find()
#
# # 删除集合
# db.t1.drop()
#
# # 插入多条数据，必须使用列表
# db.t1.insert([{name:'C++'},{name:'C#'}])
#
# # 指定查询条件
# db.t1.find({name:'C#'})
#
# # 更新数据,默认情况下，只更新一条,默认情况下，
# # update执行的是覆盖操作，原始数据无论有多少字段，会把之前的数据进行覆盖；
# db.t1.update({name:'C++'},{name:'go'})
#
# # 更新指定键值的数据，$set如果该键值不存在，新创建
# db.t1.update({name:'PHP'},{$set:{name:'Javascript'}})
#
# # 更新数据multi如果未设置，只更新1条，如果为true，更新多条
# db.t1.update({name:'qiang'},{$set:{name:'jun',age:30}},{multi:true})
#
# # 不指定条件更新
# db.t1.update({},{$set:{name:'jun',age:30}},{multi:true})
#
# # 删除数据，必须要有{}
# db.t1.remove({})
# db.t1.remove() # 不能删除
#
# # 保存数据
# # save = insert + update
# # 如果主键重复，insert会报错，save不会
# db.t1.save({_id:1,name:'c++'})
#
#
# # 查询的操作：
# # 格式化输出,类似于字典的格式输出
# db.stu.find().pretty()
#
# # 查询一条数据，默认格式化输出
# db.stu.findOne()
#
# # 比较运算符:lt、lte、gt、gte、ne
# # 查询年龄小于20的数据
# db.stu.find({age:{$lt:20}})
# db.stu.find({age:{$lte:20}})
# db.stu.find({age:{$gt:20}})
# db.stu.find({age:{$gte:20}})
# # 查询年龄不等于20的数据
# db.stu.find({age:{$ne:20}})
#
# # 逻辑运算符：
# # $and,满足两个条件的数据,参数存储在列表中
# db.stu.find({$and:[{hometown:'蒙古'},{gender:true}]})
#
# # 查询年龄小于40，并且性别为男的数据
# db.stu.find({$and:[{age:{$lt:40}},{gender:true}]})
#
# # 查询年龄小于30，或者性别为女的数据
# db.stu.find({$or:[{age:{$lt:30}},{gender:false}]})
#
#
# # 范围运算符
# # $in查找指定范围内的数据
# db.stu.find({age:{$in:[16,18]}})
#
# # $nin查找不在指定范围内的数据
# db.stu.find({age:{$nin:[16,18]}})
#
# # 正则表达式 : 正则表达式只能匹配字符串，不能匹配数值；
#
# # 查找所有姓黄的数据
# db.stu.find({name:/^黄/})
#
# # 查找姓名中有王的数据
# db.stu.find({name:/王/})
#
# # 正则表达式$regex,正则表达式必须用引号
# db.stu.find({hometown:{$regex:'大'}})
#
# # 自定义查询条件，本质上相当于自定义函数
# # 返回的是年龄大于等于20的数据
# db.stu.find({
#     $where:function(){
#         return this.age >= 20
#     }
# })
# # 返回的是家乡为桃花岛的数据
# db.stu.find({ $where:function(){ return this.hometown == '桃花岛' } })
#
# # 跳转指定条目的数据，相当于从第四条开始查询数据
# db.stu.find().skip(3)
#
# # 查询指定条目的数据，相当于只拿三条数据
# db.stu.find().limit(3)
#
# # 先执行间隔3条数据，然后分页,使用skip和limit前后不影响结果
# db.stu.find().skip(3).limit(2)
#
# # 投影
# # 对查询结果的指定字符不显示
# db.stu.find({age:18},{_id:0})
#
# # 对查询结果进行指定字段显示，hometown：0不显示
# db.stu.find({},{_id:0,name:1,age:1,hometown:1})
#
# # 对查询结果进行排序
# # 需要使用sort方法，key:value为1升序-1为降序
# db.stu.find({age:{$gt:18}}).sort({age:-1})
# db.stu.find({age:{$gt:18}}).sort({age:1})
#
# # 对查询结果进行统计
# # count返回的是数据的条目数
# db.stu.find({age:18}).count()
# db.stu.count({age:18})
#
# # 对数据进行去重操作
# # 把年龄小于40的数据进行去重，返回的是列表
# db.stu.distinct('age',{age:{$lt:40}})
#
# # 聚合运算
# # 分组,按照年龄分组，
# db.stu.aggregate([{$group:{_id:'$age',_result:{$sum:1}}}])
#
# # 未使用$符号，不能根据年龄进行分组
# db.stu.aggregate([{$group:{_id:'age',_result:{$sum:1}}}])
#
# # 分组，按照年龄进行分组，并提取数据
# db.stu.aggregate([{$group:{_id:'$age',_result:{$avg:'$age'}}}])
#
# # 对性别进行分组，并计算每组年龄的平均值
# db.stu.aggregate([{$group:{_id:'$gender',_result:{$avg:'$age'}}}])
#
# # 计算每组人员的年龄的总和
# db.stu.aggregate([{$group:{_id:'$gender',_result:{$sum:'$age'}}}])
#
# # 计算每组人员年龄最小的人
# db.stu.aggregate([{$group:{_id:'$gender',_result:{$min:'$age'}}}])
#
#
# # $match类似于find方法，但是区别在于可以对查询结果进行再次操作
# db.stu.aggregate([{$match:{age:{$gt:18}}}])
#
# # $match和$project,实现类似于投影的功能
# db.stu.aggregate([{$match:{age:{$gt:18}}},{$project:{_id:0}}])
#
# # $skip和$limit，间隔指定条目的数据
# db.stu.aggregate([{$match:{age:{$gt:18}}},{$limit:1}])
# # 拿取指定条目的数据
# db.stu.aggregate([{$match:{age:{$gt:18}}},{$skip:1}])
# # $sort排序-1按照降序进行排序
# db.stu.aggregate([{$match:{age:{$gt:18}}},{$sort:{age:-1}}])
#
# # $unwind 拆分列表中的数据，默认情况下是按照_id进行判断
# db.t2.aggregate([{$unwind:'$size'}])
#
#
# # 索引：
# # 查看索引
# db.t3.getIndexes()
# # 查看执行效率,单位是毫秒
# db.t3.find({name:'name_99999'}).explain('executionStats')
# # 创建索引
# db.t3.ensureIndex({name:1},{background:true})
#
# # 删除索引
# db.t3.getIndexes()
#
# # 数据库的备份
# # 把数据库中的数据，备份到指定位置
# mongodump -d dbname -o 文件夹
# # 从磁盘中把数据库还原到mongo中，注意：终端中显示的数据库的大小会有出入
# mongorestore -d 备份到mongo中的的数据库的名称，--dir 文件夹名称/数据库的名称
#
# # 备份指定数据库中的集合
# mongoexport -d python -c stu --type csv -f name,hometown,age,gender -o stu.csv
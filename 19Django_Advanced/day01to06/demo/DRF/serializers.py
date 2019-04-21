from rest_framework import serializers

from user.models import BookInfo

"""
    DRF框架中的序列化器
"""


# class BookInfoSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = BookInfo
#         fields = '__all__'


"""
    定义好序列化器之后，在视图中创建一个继承自ModelViewSet的ViewSet,用来指定序列化器
"""


class BookInfoSerializer(serializers.ModelSerializer):

    # 序列化的时候有可能和反序列化的字段不同，比如id字段并不需要接收自前段，而是数据库自动生成，所以前段不要传id，设置为read_only
    # read_only 表示只在序列化输出的时候使用，指的是返回给前端的时候，前段只能read
    # write_only 表示只在反序列化输入的时候使用，指的是接收前段请求，会带上的字段
    id = serializers.IntegerField(label='ID', read_only=True)
    name = serializers.CharField(label='名称', max_length=20)
    pub_date = serializers.DateField(label='发布日期', required=False)
    read_count = serializers.IntegerField(label='阅读量', required=False)
    comment_count = serializers.IntegerField(label='评论量', required=False)
    is_delete = serializers.BooleanField(label='图片', required=False)

    class Meta:
        model = BookInfo

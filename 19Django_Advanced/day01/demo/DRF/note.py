"""
    前后端不分离：前段页面的渲染是由后端进行的，比如render_template来直接返回一个html界面或者重定向
        如果当后端对接的不再是浏览器，而是一个app移动端，那么整体的后端再返回html的话，则需要再开发一套接口

    前后端分离：后端只是负责返回数据本身，不再进行页面的渲染，前段无所谓是html浏览器还是app，无论是哪种，只需要一套后端接口即可
        浏览器使用nginx来请求html,css,js页面，然后浏览器拿到后解析里面的js，让js去请求后端获取数据，浏览器在进行界面的数据添加和渲染
        同样的道理，app请求数据，自己本身进行页面的渲染和数据的填充
"""

"""
    restful设计
    1- api.github.com 尽量部署在专用的域名下
    2- http://www.example.com/api/1.1/foo 又需要的话把api的版本添加到url中，用来请求不同版本中的不同新旧数据
    3- 路径中根据不同的请求方式来指定动作，不要有动词。只能有名词。名词需要复数
       GET /products ：将返回所有产品清单
       POST /products ：将产品新建到集合
       GET /products/4 ：将获取产品 4
       PATCH（或）PUT /products/4 ：将更新产品 4
       http://127.0.0.1:8080/AppName/rest/products/1
    4- 使用规定的状态来响应，比如201，新建或者更新数据成功
    5- 错误处理40X,使用json中的key=error
    6- 不同的请求，需要返回状态码之外，还需要返回指定的结果：PUT之后返回201，还有被更新对象的json信息
    7- restful尽量使用json数据格式，xml的话标签太多，解析效率不高<xml><name>hao zhang</name></xml>    
"""
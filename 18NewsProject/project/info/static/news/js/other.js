// 解析url中的查询字符串
function decodeQuery(){
    var search = decodeURI(document.location.search);
    return search.replace(/(^\?)/, '').split('&').reduce(function(result, item){
        values = item.split('=');
        result[values[0]] = values[1];
        return result;
    }, {});
}

$(function(){
    // 页面加载完毕，获取新闻列表
    getNewsList(1)

    // TODO 关注当前作者
    $(".focus").click(function () {

    })

    // TODO 取消关注当前作者
    $(".focused").click(function () {

    })
})

// TODO 获取新闻列表
function getNewsList(page) {

}

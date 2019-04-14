function getCookie(name) {
    var r = document.cookie.match("\\b" + name + "=([^;]*)\\b");
    return r ? r[1] : undefined;
}

$(function(){
    $(".news_review").submit(function (e) {
        e.preventDefault()

        // 新闻审核提交
        var params = {};
        // 获取到所有的参数
        $(this).serializeArray().map(function (x) {
            params[x.name] = x.value;
        });
        // 取到参数以便判断
        var action = params["action"];
        var news_id = params["news_id"];
        var reason = params["reason"];
        if (action == "reject" && !reason) {
            alert('请输入拒绝原因');
            return;
        }
        params = {
            "action": action,
            "news_id": news_id,
            "reason": reason
        }
        $.ajax({
            url: "/admin/news_review_action",
            type: "post",
            contentType: "application/json",
            headers: {
                "X-CSRFToken": getCookie("csrf_token")
            },
            data: JSON.stringify(params),
            success: function (resp) {
                if (resp.errno == "0") {
                    // 返回上一页，刷新数据,document.referrer代表是从哪一个链接跳转过来的，类似于浏览器返回箭头
                    location.href = document.referrer;
                }else {
                    alert(resp.errmsg);
                }
            }
        })

    })
})

// 点击取消，返回上一页
function cancel() {
    history.go(-1)
}
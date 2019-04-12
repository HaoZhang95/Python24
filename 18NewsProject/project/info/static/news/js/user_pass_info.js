function getCookie(name) {
    var r = document.cookie.match("\\b" + name + "=([^;]*)\\b");
    return r ? r[1] : undefined;
}


$(function () {
    $(".pass_info").submit(function (e) {
        e.preventDefault();

        // 修改密码
        var params = {};
        // 将当前pass_info的表单获取name有值得input标签参数
        // x表示的就是标签，取出的值就是 x:{name: "old_password", value:"123456"}
        // 所以表单中需要获取的标签的name不能设置为name=""，这样获取不到数值
        $(this).serializeArray().map(function (x) {
            params[x.name] = x.value;
        });
        // 取到两次密码进行判断
        var new_password = params["new_password"];
        var new_password2 = params["new_password2"];

        if (new_password != new_password2) {
            alert('两次密码输入不一致')
            return
        }

        $.ajax({
            url: "/user/pass_info",
            type: "post",
            contentType: "application/json",
            headers: {
                "X-CSRFToken": getCookie("csrf_token")
            },
            data: JSON.stringify(params),
            success: function (resp) {
                if (resp.errno == "0") {
                    // 修改成功
                    alert("修改成功")
                    window.location.reload()
                }else {
                    alert(resp.errmsg)
                }
            }
        })

    })
})
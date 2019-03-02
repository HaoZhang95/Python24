$(function () {

    var check_user_flag = false;

    // 复选框默认是勾选的,所以flag是true,防止用户直接点击注册
    var check_allow_flag = true;

    // 当各个输入框失去焦点的时候就开始判断， $user_name命名方便，表示jquery选择出来的标签
    var $user_name = $("#user_name")
    $user_name.blur(function () {
        console.log(122112);
        check_user_name()
        
    })

    // 验证用户名---输入框
    function check_user_name() {
        var vals = $($user_name).val()
        var re = /^\w{6,20}$/;

        console.log(1212);
        

        if (vals == '') {
            $($user_name).next().show()
            $($user_name).next().html("用户名不能为空...")
            check_user_flag = false
            return;
        }

        if (re.test(vals)) {
            $($user_name).next().hide()
            check_user_flag = true
        } else {
            // 错误显示的是当前输入框的错误提示
            $($user_name).next().show()
            $($user_name).next().html("用户名不符合规则...")
            check_user_flag = false
        }
    }
    

    var $allow = $("#allow")
    $allow.blur(function () {
        check_allow()
    })

    // 验证复选框--checkbox,判断prop(属性)
    function check_allow() {
        if ($allow.prop("checked")) {
            console.log($allow.prop("checked"));
            $allow.siblings('span').hide()
            check_allow_flag = true
        } else {
            $($allow).next().next().show()
            $($allow).next().next().html("请首先同意协议...")
            check_allow_flag = false
        }
    }

    var $forms = $("#forms")
    $forms.submit(function () {
        submit()
    })

    // 判断是否所有的规则都满足, 为每一个输入框设置一个flag,而不是一个flag判断所有的输入框
    function submit() {
        if (check_user_flag && check_allow_flag) {
            console.log("允许提交...");
        } else {
            console.log("验证失败...");
            return false;
        }
    }

})
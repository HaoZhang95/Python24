$(function(){

    // {#  ajax必须配置，否则ajax的post请求一直404  #}
    // var csrftoken = $('meta[name=csrf-token]').attr('content')
    // console.log("meta中的:" + csrftoken);
    //
    // $.ajaxSetup({
    //     beforeSend: function(xhr, settings) {
    //         if (!/^(GET|HEAD|OPTIONS|TRACE)$/i.test(settings.type) && !this.crossDomain) {
    //             xhr.setRequestHeader("X-CSRFToken", csrftoken)
    //         }
    //     }
    // })

	// 打开登录框
	$('.login_btn').click(function(){
        $('.login_form_con').show();
	});
	
	// 点击关闭按钮关闭登录框或者注册框
	$('.shutoff').click(function(){
		$(this).closest('form').hide();
	});

    // 隐藏错误
    $(".login_form #mobile").focus(function(){
        $("#login-mobile-err").hide();
    });
    $(".login_form #password").focus(function(){
        $("#login-password-err").hide();
    });

    $(".register_form #mobile").focus(function(){
        $("#register-mobile-err").hide();
    });
    $(".register_form #imagecode").focus(function(){
        $("#register-image-code-err").hide();
    });
    $(".register_form #smscode").focus(function(){
        $("#register-sms-code-err").hide();
    });
    $(".register_form #password").focus(function(){
        $("#register-password-err").hide();
    });


	// 点击输入框，提示文字上移
	// $('.form_group').on('click focusin',function(){
	// 	$(this).children('.input_tip').animate({'top':-5,'font-size':12},'fast').siblings('input').focus().parent().addClass('hotline');
	// })
    //
	// // 输入框失去焦点，如果输入框为空，则提示文字下移
	// $('.form_group input').on('blur focusout',function(){
	// 	$(this).parent().removeClass('hotline');
	// 	var val = $(this).val();
	// 	if(val=='')
	// 	{
	// 		$(this).siblings('.input_tip').animate({'top':22,'font-size':14},'fast');
	// 	}
	// })

    $('.form_group').on('click',function(){
    $(this).children('input').focus()
    });

    $('.form_group input').on('focusin',function(){
        $(this).siblings('.input_tip').animate({'top':-5,'font-size':12},'fast');
        $(this).parent().addClass('hotline');
    });


	// 打开注册框
	$('.register_btn').click(function(){
		$('.register_form_con').show();
		generateImageCode()
	});


	// 登录框和注册框切换
	$('.to_register').click(function(){
		$('.login_form_con').hide();
		$('.register_form_con').show();
        generateImageCode()
	});

	// 登录框和注册框切换
	$('.to_login').click(function(){
		$('.login_form_con').show();
		$('.register_form_con').hide();
	});

	// 根据地址栏的hash值来显示用户中心对应的菜单
	var sHash = window.location.hash;
	if(sHash!=''){
		var sId = sHash.substring(1);
		var oNow = $('.'+sId);		
		var iNowIndex = oNow.index();
		$('.option_list li').eq(iNowIndex).addClass('active').siblings().removeClass('active');
		oNow.show().siblings().hide();
	}

	// 用户中心菜单切换
	var $li = $('.option_list li');
	var $frame = $('#main_frame');

	$li.click(function(){
		if($(this).index()==5){
			$('#main_frame').css({'height':900});
		}
		else{
			$('#main_frame').css({'height':660});
		}
		$(this).addClass('active').siblings().removeClass('active');
		$(this).find('a')[0].click()
	});

    // TODO 登录表单提交
    $(".login_form_con").submit(function (e) {

        // 阻止默认的表单提交，不然的话后端返回的错误无法处理， 自定义提交实现局部的错误提示
        e.preventDefault();
        var mobile = $(".login_form #mobile").val();
        var password = $(".login_form #password").val();

        if (!mobile) {
            $("#login-mobile-err").show();
            return;
        }

        if (!password) {
            $("#login-password-err").show();
            return;
        }

        // 发起登录请求
        // 拼接参数
        var params = {
            "mobile":mobile,
            "password":password
        };

        $.ajax({
            url:'/passport/login',
            type:'post',
            data:JSON.stringify(params),
            contentType:'application/json',
            // 不带上cookie中的token的话，那么就会被CSRFProtect(app)拦截，返回400错误
            headers:{'X-CSRFToken':getCookie('csrf_token')},
            success: function (resp) {
                //判断是否登陆成功
                if(resp.errno == '0'){
                    window.location.reload()
                }else{
                    alert(resp.errmsg);
                }

            }
        })

    });


    // TODO 注册按钮点击
    $(".register_form_con").submit(function (e) {
        // 阻止默认提交操作,不让其往默认的action提交
        e.preventDefault();

		// 取到用户输入的内容
        var mobile = $("#register_mobile").val();
        var smscode = $("#smscode").val();
        var password = $("#register_password").val();

		if (!mobile) {
            $("#register-mobile-err").show();
            return;
        }
        if (!smscode) {
            $("#register-sms-code-err").show();
            return;
        }
        if (!password) {
            $("#register-password-err").html("请填写密码!");
            $("#register-password-err").show();
            return;
        }

		if (password.length < 6) {
            $("#register-password-err").html("密码长度不能少于6位");
            $("#register-password-err").show();
            return;
        }

        // 发起注册请求
        //拼接请求参数
        var params = {
            "mobile":mobile,
            "sms_code":smscode,
            "password":password
        };

        $.ajax({
            url:'/passport/register',
            type:'post',
            data:JSON.stringify(params),
            contentType:'application/json',
            headers:{'X-CSRFToken':getCookie('csrf_token')},
            success: function (resp) {
                //判断是否注册成功
                if(resp.errno == '0'){
                    //重新加载当前页面
                    window.location.reload();
                }else{
                    alert(resp.errmsg);
                }
            }
        })
    })
});

//退出登陆
function logout() {
    $.ajax({
        url:'/passport/logout',
        type:'post',
        headers:{'X-CSRFToken':getCookie('csrf_token')},
        success:function (resp) {
            window.location.reload()
        }
    })
}


var imageCodeId = "";
var preimageCodeId = "";

// TODO 生成一个图片验证码的编号，并设置页面中图片验证码img标签的src属性
// 图片验证码的流程：每个验证码生成之前会使用uuid获取一个唯一的编号对应这个验证码，请求页面的验证码图片的url中就包含这个编号
//然后后端把编号取出，当作一个key，随机生成一个验证码当作value存在redis，返回给客户端
//如果客户输入的验证码和编码和redis中的对应，那么就允许给客户端发送短信验证码
function generateImageCode() {

    //1.生成一个随机字符串
    imageCodeId = generateUUID();

    //2.拼接图片url地址
    // image_url = '/passport/image_code?cur_id='+imageCodeId;
    image_url = '/passport/image_code?cur_id='+imageCodeId + "&pre_id="+preimageCodeId;

    //3.将地址设置到image标签的src属性中,为image_url
    $('.get_pic_code').attr('src',image_url);

    //4.记录上一次的编号，用于用户点击验证码进行刷新
    preimageCodeId = imageCodeId

}


// 发送短信验证码
function sendSMSCode() {
    // 校验参数，保证输入框有数据填写
    //移除按钮点击事件
    $(".get_code").removeAttr("onclick");
    var mobile = $("#register_mobile").val();
    if (!mobile) {
        $("#register-mobile-err").html("请填写正确的手机号！");
        $("#register-mobile-err").show();
        $(".get_code").attr("onclick", "sendSMSCode();");
        return;
    }
    var imageCode = $("#imagecode").val();
    if (!imageCode) {
        $("#image-code-err").html("请填写验证码！");
        $("#image-code-err").show();
        $(".get_code").attr("onclick", "sendSMSCode();");
        return;
    }

    // TODO 发送短信验证码
    //拼接参数
    var params = {
        "mobile":mobile,
        "image_code":imageCode,
        "image_code_id":imageCodeId
    }

    // 得到的是undefined，要想ajax的post成功，必须在headers中带上csrf_tokem
    console.log("ajax中的:" + getCookie('csrf_token'));
    //发送获取短信请求
    $.ajax({
        url:'/passport/sms_code',//请求地址
        type:'POST',
        data:JSON.stringify(params),
        contentType:'application/json',
        headers:{'X-CSRFToken':getCookie('csrf_token')},
        success: function (resp) {
            //判断是否请求成功
            console.log(resp)
            if(resp.errno == '0'){

                //定义倒计时时间
                var num = 60;

                //创建定时器
                var t = setInterval(function () {

                    //判断是否倒计时结束
                    if(num == 1){
                        //清除定时器
                        clearInterval(t);
                        //设置标签点击事件,并设置内容
                        $(".get_code").attr("onclick",'sendSMSCode()');
                        $(".get_code").html('点击获取验证码');


                    }else{
                        //设置秒数
                        num -= 1;
                        $('.get_code').html(num + '秒');
                    }
                },1000);//一秒走一次

            }else{//发送失败
                alert(resp.errmsg);
                // 重新设置点击事件,更新图片验证码
                $(".get_code").attr("onclick",'sendSMSCode()');
                generateImageCode();
            }
        }, error: function (error) {
            console.log(error);
            console.log(error.toString());
        }

    })

}

// 调用该函数模拟点击左侧按钮
function fnChangeMenu(n) {
    var $li = $('.option_list li');
    if (n >= 0) {
        $li.eq(n).addClass('active').siblings().removeClass('active');
        // 执行 a 标签的点击事件
        $li.eq(n).find('a')[0].click()
    }
}

// 一般页面的iframe的高度是660
// 新闻发布页面iframe的高度是900
function fnSetIframeHeight(num){
	var $frame = $('#main_frame');
	$frame.css({'height':num});
}

function getCookie(name) {
    var r = document.cookie.match("\\b" + name + "=([^;]*)\\b");
    return r ? r[1] : undefined;
}

function generateUUID() {
    var d = new Date().getTime();
    if(window.performance && typeof window.performance.now === "function"){
        d += performance.now(); //use high-precision timer if available
    }
    var uuid = 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, function(c) {
        var r = (d + Math.random()*16)%16 | 0;
        d = Math.floor(d/16);
        return (c=='x' ? r : (r&0x3|0x8)).toString(16);
    });
    return uuid;
}

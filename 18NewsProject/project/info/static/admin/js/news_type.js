function getCookie(name) {
    var r = document.cookie.match("\\b" + name + "=([^;]*)\\b");
    return r ? r[1] : undefined;
}

$(function(){
    var $a = $('.edit');
    var $add = $('.addtype');
    var $pop = $('.pop_con');
    var $cancel = $('.cancel');
    var $confirm = $('.confirm');
    var $error = $('.error_tip');
    var $input = $('.input_txt3');
    var sHandler = 'edit';
    var sId = 0;

    $a.click(function(){
        sHandler = 'edit';
        sId = $(this).parent().siblings().eq(0).html();
        $pop.find('h3').html('修改分类');
        $pop.find('.input_txt3').val($(this).parent().prev().html());
        $pop.show();
    });

    $add.click(function(){
        sHandler = 'add';
        $pop.find('h3').html('新增分类');
        $input.val('');
        $pop.show();
    });

    $cancel.click(function(){
        $pop.hide();
        $error.hide();
    });

    $input.click(function(){
        $error.hide();
    });

    $confirm.click(function(){

        var params = {}
        if(sHandler=='edit')
        {
            var sVal = $input.val();
            if(sVal=='')
            {
                $error.html('输入框不能为空').show();
                return;
            }
            params = {
                "id": sId,
                "name": sVal,
            };
        }
        else
        {
            var sVal = $input.val();
            if(sVal=='')
            {
                $error.html('输入框不能为空').show();
                return;
            }
            params = {
                "name": sVal,
            }
        }

        // TODO 发起修改分类请求

    })
})
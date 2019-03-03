$(function () {

    var index_of_current_li = 0
    var index_of_target_li = 0
    var arrow_flag = true

    var $img_li = $(".slide ul li")

    for (let index = 0; index < $img_li.length; index++) {
        var $point_li =  $("<li></li>")
        if (index == 0) {
            $point_li.addClass("active")
        }
        $point_li.appendTo($(".slide ol"))
    }

    // 因为上面设置第一个原点为active,所以设置显示第一张图片
    $img_li.not(":first").css({"left": "760px"})

    // 圆点点击，从小到大点击，图片是从右向左移动，反之，从左向右
    var $point_li = $(".slide ol li")
    $point_li.click(function () {
        index_of_target_li = $(this).index()
        
        pic_move()
    })

    // 左右箭头点击
    var $left = $(".slide .left")
    var $right = $(".slide .right")

    $right.click(function () {
        if (arrow_flag) {
            arrow_flag = false
            index_of_target_li++;
            pic_move()
        }
    })

    $left.click(function () {
        if (arrow_flag) {
            arrow_flag = false
            index_of_target_li--;
            pic_move()
        }
    })

    // 自动播放
    var oTimer = setInterval(auto_move, 3000)

    function auto_move() {
        index_of_target_li++;
        pic_move()
    }

    // 鼠标移入离开事件
    var $slide = $(".slide")
    $slide.hover(function () {
        clearInterval(oTimer)
        oTimer = null
    }, function () {
        oTimer = setInterval(auto_move, 3000)
    })

   
    // 图片移动
    function pic_move() {
        if (index_of_current_li < index_of_target_li) {
            // 从右向左移动图片---需要保证目标图在右侧, 防止跳着点原点,目标图位置错乱
            // 为了防止用户连续点击，动画需要先停止再重新执行，否则会出乱,遇到animate就自动在前加上stop()
            $img_li.eq(index_of_current_li).stop().animate({"left": "-760px"}, function () {
                arrow_flag = true
            })
            $img_li.eq(index_of_target_li).css({"left": "760px"})
        } else {
            // 从左向右移动图片---需要保证目标图在左侧
            $img_li.eq(index_of_current_li).stop().animate({"left": "760px"}, function () {
                arrow_flag = true
            })
            $img_li.eq(index_of_target_li).css({"left": "-760px"})
        }

        // 如果到结尾，显示第一张图,仍然摆位置从右侧到左侧
        if (index_of_target_li > $img_li.length - 1) {
            index_of_target_li = 0
            index_of_current_li = $img_li.length - 1

            // 摆位置
            $img_li.eq(index_of_target_li).css({"left": "760px"})
            $img_li.eq(index_of_current_li).stop().animate({"left": "-760px"}, function () {
                arrow_flag = true
            })
        }

        // 如果到开头，显示最后一张图,仍然摆位置从左侧到右侧
        if (index_of_target_li < 0) {
            index_of_target_li =  $img_li.length - 1
            index_of_current_li = 0

            // 摆位置
            $img_li.eq(index_of_target_li).css({"left": "-760px"})
            $img_li.eq(index_of_current_li).stop().animate({"left": "760px"}, function () {
                arrow_flag = true
            })
        }

        // 更新index和圆点
        $img_li.eq(index_of_target_li).stop().animate({"left": "0px"}, function () {
            arrow_flag = true
        })
        index_of_current_li = index_of_target_li
        $point_li.eq(index_of_target_li).addClass("active").siblings().removeClass("active")
    }
})
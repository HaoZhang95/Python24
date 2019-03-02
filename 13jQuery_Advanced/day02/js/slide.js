$(function () {

    var index_of_current_li = 0
    var index_of_target_li = 0

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
        index_of_target_li++;
        console.log(121);
        
        pic_move()
    })

    $left.click(function () {
        index_of_target_li--;
        pic_move()
    })

    // 自动播放

    // 鼠标移入离开事件
   
    // 图片移动
    function pic_move() {
        if (index_of_current_li < index_of_target_li) {
            // 从右向左移动图片---需要保证目标图在右侧, 防止跳着点原点,目标图位置错乱
            $img_li.eq(index_of_current_li).animate({"left": "-760px"})

            $img_li.eq(index_of_target_li).css({"left": "760px"})
            $img_li.eq(index_of_target_li).animate({"left": "0px"})
        } else {
            // 从左向右移动图片---需要保证目标图在左侧
            $img_li.eq(index_of_current_li).animate({"left": "760px"})

            $img_li.eq(index_of_target_li).css({"left": "-760px"})
            $img_li.eq(index_of_target_li).animate({"left": "0px"})
        }

        // 如果到结尾，显示第一张图,仍然摆位置从右侧到左侧
        if (index_of_target_li > $img_li.length - 1) {
            index_of_target_li = 0
            index_of_current_li = $img_li.length - 1

            // 摆位置
            $img_li.eq(index_of_target_li).css({"left": "760px"})
            $img_li.eq(index_of_target_li).animate({"left": "0px"})

            $img_li.eq(index_of_current_li).animate({"left": "-760px"})
        }

        // 如果到开头，显示最后一张图,仍然摆位置从左侧到右侧
        if (index_of_target_li < 0) {
            index_of_target_li =  $img_li.length - 1
            index_of_current_li = 0

            // 摆位置
            $img_li.eq(index_of_target_li).css({"left": "-760px"})
            $img_li.eq(index_of_target_li).animate({"left": "0px"})

            $img_li.eq(index_of_current_li).animate({"left": "760px"})
        }

        // 更新index和圆点
        index_of_current_li = index_of_target_li
        $point_li.eq(index_of_target_li).addClass("active").siblings().removeClass("active")
    }
})
/**
 * Created by wlw on 15-1-12.
 */

$(document).ready(function () {
    $(".order").click(function () {
        oldid = $(this).closest('tr').find('input[name="oldid"]').val();
        $button = $(this);
        if ($button.val() == "已预约") {
            alert("这已经预约,请不要试第二次");
            return;
        }
        $.ajax({
            url: "/order_open_lab/order/",
            type: 'post',
            data: {
                oldid: oldid,
                csrfmiddlewaretoken: $('input[name="csrfmiddlewaretoken"]').val()
            },
            dataType: 'json',
            success: function (data) {
                var r = data['result'];
                if (r == 'success') {
                    confirm("你已经预约请等待老师审核");
                    $button.val("已预约");
                } else {
                    alert(data['msg']);
                }
            },
            error: function () {

            }
        });
    });

    $('.order_circle').click(function () {
        var coldid = $(this).closest('tr').find('input[name="coldid"]').val();
        $button = $(this);
        if ($button.val() == "已预约") {
            alert("这已经预约,请不要试第二次");
            return;
        }

        $.ajax({
            url: "/order_open_lab/order_circle/",
            type: 'post',
            data: {
                coldid: coldid,
                csrfmiddlewaretoken: $('input[name="csrfmiddlewaretoken"]').val()
            },
            dataType: 'json',
            success: function (data) {
                var r = data['result'];
                if (r == 'success') {
                    confirm("你已经预约请等待老师审核");
                    $button.val("已预约");
                } else {
                    alert(data['msg']);
                }
            },
            error: function () {

            }
        });
    });
});
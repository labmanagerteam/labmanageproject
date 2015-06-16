/**
 * Created by wlw on 15-1-27.
 */


var reflect = function ($this, action) {

    var get_option = function () {
        var type = $this.closest('tr').find('input[name="type"]').val();
        if (type == "one_time") {
            return {
                csrfmiddlewaretoken: $('input[name="csrfmiddlewaretoken"]').val(),
                order_id: $this.closest('tr').find('input[name="order_id"]').val(),
                action: action
            };
        } else {
            return {
                csrfmiddlewaretoken: $('input[name="csrfmiddlewaretoken"]').val(),
                corder_id: $this.closest('tr').find('input[name="corder_id"]').val(),
                action: action
            }
        }
    };

    var get_action = function () {
        var type = $this.closest('tr').find('input[name="type"]').val();
        if (type == "one_time") {
            return '/check_order/reflect/';
        } else {
            return '/check_order/circle_reflect/';
        }
    };

    $.ajax({
        url: get_action(),
        data: get_option(),
        type: 'post',
        dataType: 'json',
        success: function (data) {
            if (data['result'] == 'error') {
                confirm(data['msg']);
                $this.closest('tr').remove();
            } else if (data['result'] == 'success') {
                $this.closest('tr').remove();
            }
        },
        error: function () {
            alert("网络有问题，请稍后再试");
        }
    });
};


$(document).ready(function () {
    $('.accept').click(function () {
        reflect($(this), 'accept');
    });

    $('.refuse').click(function () {
        reflect($(this), 'refuse');
    });
});
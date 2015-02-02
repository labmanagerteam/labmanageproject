/**
 * Created by wlw on 15-1-27.
 */


var reflect = function ($this, action) {
    $.ajax({
        url: '/check_order/reflect/',
        data: {
            csrfmiddlewaretoken: $('input[name="csrfmiddlewaretoken"]').val(),
            order_id: $this.closest('tr').find('input[name="order_id"]').val(),
            action: action
        },
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
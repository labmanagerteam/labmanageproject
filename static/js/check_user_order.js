/**
 * Created by wlw on 15-1-27.
 */


var reflect = function ($this, action) {
    $.ajax({
        url: '/check_order/reflect/',
        data: {
            csrfmiddlewaretoken: $('input[name="csrfmiddlewaretoken"]').val(),
            order_id: $this.closest('tr').find('input[name="order_id"]').val(),
            uid: $this.closest('tr').find('input[name="uid"]').val(),
            action: action
        },
        type: 'post',
        dataType: 'json',
        success: function (data) {

        },
        error: function () {

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
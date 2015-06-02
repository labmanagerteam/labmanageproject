/**
 * Created by wlw on 15-2-19.
 */
var do_delete = function ($this, url, action) {
    var delid = $this.closest('tr').find('.del_id').val();
    $.ajax({
        url: url,
        data: {
            delid: delid,
            csrfmiddlewaretoken: $('input[name="csrfmiddlewaretoken"]').val()
        },
        type: 'post',
        dataType: 'json',
        success: function (data) {
            success_handler_g(data, "删除成功", action);
        },
        error: function () {
            error_handler_g();
        }
    });
};
/**
 * Created by wlw on 15-2-25.
 */

$(document).ready(function () {

    var $form = $('#semster_submit_form');

    $form.submit(function () {
        $(this).ajaxSubmit({
            beforeSubmit: function (arr, $form, options) {
                var begin_date = new Date(get_input('begin_date', arr)[0]);
                var end_date = new Date(get_input('end_date', arr)[0]);
                var now = new Date();
                console.log(begin_date);
                console.log(end_date);
                console.log(now);

                if (begin_date > end_date) {
                    alert("开始时间应该在结束时间之后");
                    return false;
                }

                if (now > end_date) {
                    alert("你设置的时间已过");
                    return false;
                }

                if (now > begin_date) {
                    if (confirm("此时已处于您设置的学期之内,您确定要提交么?")) {
                        return true;
                    } else {
                        return false;
                    }
                }

                //if(confirm("注意：如果当前学期尚未结束"))
                //{
                //    return true;
                //}else{
                //    return false;
                //}
            },
            dataType: 'json',
            success: function (data) {
                success_handler_g(data, "你已成功设置了学期的起止时间", false);
            },
            error: function () {
                error_handler_g();
            }
        });
        return false;
    });
});

/**
 * Created by wlw on 15-2-19.
 */


var success_handler_g = function (data, success_msg, success_action) {
    if (data['result'] == 'success') {
        confirm(success_msg);
        if (success_action) {
            success_action();
        }
    } else {
        alert(data['msg']);
    }
};


var error_handler_g = function () {
    alert("网络有问题,请稍后再试");
};

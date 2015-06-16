/**
 * Created by wlw on 15-1-11.
 */


var get_now_open_lab_olid = function () {
    return $("#now_open_lab").find('input[name="olid"]').val();
};

var get_conflict_lab_olid_list = function () {
    var c_list = [];
    $('#conflict_list').find('input[name="olid"]').each(function () {
        c_list.push($(this).val());
    });

    if (c_list.length == 0) {
        console.log("no conflict");
        return [];
    } else {
        console.log("yes conflict");
        return c_list;
    }

};

var check_open_str = "/check_open_lab";

var success_handler = function (data) {
    if (data['result'] == "ok") {
        confirm("已通过");
        location.href = check_open_str + "/";
    } else {
        alert(data['result']);
    }
};

var error_handler = function () {
    alert("网络有问题,请稍后再试");
};

$(document).ready(function () {
    $("#accept").click(function () {
        $.ajax({
            url: check_open_str + "/accept/",
            data: {
                now_open_lab: get_now_open_lab_olid(),
                conflict_list: get_conflict_lab_olid_list(),
                csrfmiddlewaretoken: $('input[name="csrfmiddlewaretoken"]').val()
            },
            type: 'post',
            dataType: 'json',
            success: function (data) {
                success_handler(data);
            },
            error: function () {
                error_handler();
            }
        });
    });

    $("#refuse").click(function () {
        $.ajax({
            url: check_open_str + "/refuse/",
            data: {
                now_open_lab: get_now_open_lab_olid(),
                csrfmiddlewaretoken: $('input[name="csrfmiddlewaretoken"]').val()
            },
            type: 'post',
            dataType: 'json',
            success: function (data) {
                success_handler(date);
            },
            error: function () {
                error_handler();
            }
        });
    });
});
/**
 * Created by wlw on 15-2-26.
 */

var lab_select = "";

var get_week_day_select = function () {
    var day = ['星期一', '星期二', '星期三', '星期四', '星期五', '星期六', '星期日'];
    var val = [0, 1, 2, 3, 4, 5, 6];

    var line = '<select name="weekday" class="number_menu">';
    for (var i in day) {
        line += "<option value=" + val[i] + ">" + day[i] + "</option>";
    }

    line += "</select>";

    return line;
};

//var get_lab_c = function (lcid) {
//    console.log(lcid);
//    $.ajax({
//        url: '/get_lab_by_lcid/',
//        data: {
//            lcid: lcid
//        },
//        type: 'get',
//        async: false,
//        dataType: 'json',
//        success: function (data) {
//            console.log('data:' + data);
//            lab_select = '<select class="selectmenu number_menu" name="lid">';
//            for (var i in data) {
//                console.log(data[i]['lid'] + ': ' + data[i]['lname']);
//                lab_select += '<option value="' + data[i]['lid'] + '">' +
//                data[i]['lname'] +
//                '</option>';
//            }
//            lab_select += '</select>';
//            console.log("c");
//            console.log("complete");
//        },
//        error: function () {
//            console.log("get_lab_c error");
//        }
//    });
//
//    console.log("lab_select:" + lab_select);
//    return lab_select;
//};
var get_lab = function (i, lcid) {
    $.ajax({
        type: 'get',
        url: '/get_lab_by_lcid',
        data: {
            lcid: lcid
        },
        dataType: 'json',
        success: function (data) {
            if (i === 1) {
                $('#single_labname').empty();
                $('#single_labname').append("<option value=\"\" selected=\"\">请选择实验室</option>");
                for (var j = 0; j < data.length; j++) {
                    $('#single_labname').append("<option value=\"" + data[j].lid + "\">" + data[j].lname + "</option>");
                }
            } else {
                $('#loop_labname').empty();
                $('#loop_labname').append("<option value=\"\" selected=\"\">请选择实验室</option>");
                for (var j = 0; j < data.length; j++) {
                    $('#loop_labname').append("<option value=\"" + data[j].lid + "\">" + data[j].lname + "</option>");
                }
            }
        },
        error: function () {
            console.log('error');
        }
    });
};

$(document).ready(function () {

    //var $clcid = $("#c_lcid");
    get_lab(1, $('#single_labcenter').val());
    get_lab(2, $('#loop_labcenter').val());
    $('#single_labcenter').change(function () {
        get_lab(1, $(this).val());
        var table = document.getElementById("single_t");
        while (table.rows.length != 2) {
            table.deleteRow(2);
        }
    });

    $('#loop_labcenter').change(function () {
        get_lab(2, $(this).val());
        var table = document.getElementById("loop_t");
        while (table.rows.length != 2) {
            table.deleteRow(2);
        }
    });

    add_no_empty();

//$clcid.selectmenu({
//    change: function (event, ui) {
//        get_lab_c($(this).val());
//        console.log("lab_select:" + lab_select);
//        $(".detail_circle_line").remove();
//    }
//});

    $('#add_circle').click(function () {
        var one_line =
            '<tr class="detail_circle_line">' +
            "<td>" + lab_select + "</td>" +
            "<td>" + get_week_day_select() + "</td>" +
            "<td>" + create_time('begin_time') + "</td>" +
            "<td>" + create_time('end_time') + "</td>" +
            '<td><input type="button" class="button delete_one_detail" value="删除"/></td>' +
            '<td></td>' +
            '</tr>';

        $('#circle table').append(one_line);
        add_number_menu();
        add_no_empty();
        $('.button').button();
    });

    $('#circle_form').submit(function () {
        $(this).ajaxSubmit({
            beforeSubmit: function (arr, $form, options) {
                for (var i in arr) {
                    console.log(arr[i]);
                }
                var begin_week_number = get_input('begin_week_number', arr)[0];
                var end_week_number = get_input('end_week_number', arr)[0];

                if (Number(begin_week_number) >= Number(end_week_number)) {
                    alert("结束的周应在开始的周之后");
                    return false;
                }

                var lid_list = get_input('lid', arr);
                var weekday_list = get_input('weekday', arr);
                var begin_time_list = get_input('begin_time', arr);
                var end_time_list = get_input('end_time', arr);

                for (var i = 0; i < lid_list.length; ++i) {
                    if (Number(begin_time_list[i]) >= Number(end_time_list[i])) {
                        alert("开始时间应在结束时间之后");
                    }
                    for (var j = 0; j < i; ++j) {
                        if (lid_list[i] == lid_list[j] && weekday_list[i] == weekday_list[j]) {
                            if (Number(begin_time_list[i]) < Number(end_time_list[j]) &&
                                Number(end_time_list[i]) > Number(begin_time_list[j])) {
                                alert("第" + i + "行与第" + j + "行存在时间上的冲突");
                                return false;
                            }
                        }
                    }
                }

                return true;
            },
            dataType: 'json',
            success: function (data) {
                if (data['result'] == 'success') {
                    confirm("你的开放计划已提交，请等待管理员审核");
                } else {
                    if (data["join_list"]) {
                        var join_list = data["join_list"];
                        var s = "第" + join_list[0];
                        for (var i = 1; i < join_list.length; ++i) {
                            s += "," + join_list[i]
                        }
                        s += "行与现有开放计划冲突";
                        alert(s);
                    } else {
                        alert(data['msg']);
                    }
                }
            },
            error: function () {
                error_handler_g();
            }
        });
        return false;
    });
})
;

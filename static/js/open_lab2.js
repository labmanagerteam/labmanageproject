/**
 * Created by wlw on 15-1-8.
 */
/**
 * Created by wlw on 15-1-5.
 */

var create_time = function (name) {
    var time = '<select name="' + name + '">';
    var i = 8;
    while (i <= 22) {
        time += '<option value="' + i + '">' + i + '</option>';
        ++i;
    }
    time += '</select>';
    return time;
};

var one_line = '';

var get_lab = function (lcid) {
    var get_func = $.ajax({
        url: '/get_lab_by_lcid/',
        data: {
            lcid: lcid
        },
        type: 'get',
        dataType: 'json',
        success: function (data) {
            var inner_line = '<tr class="detail_one_line">' +
                '<td>' +
                '<select name="lid">';
            for (var i in data) {
                console.log(data[i]['lid'] + ': ' + data[i]['lname']);
                inner_line += '<option value="' + data[i]['lid'] + '">' +
                data[i]['lname'] +
                '</option>';
            }

            inner_line += '</select>' +
            '</td>' +
            '<td>' +
            '<input type="date" name="date" />' +
            '</td>' +
            '<td>' +
            create_time('begin_time') +
            '</td>' +
            '<td>' +
            create_time('end_time') +
            '</td>' +
            '<td>' +
            '<input class="delete_one_detail" type="button" value="删除" />' +
            '</td>' +
            '</tr>';

            console.log("c");

            one_line = inner_line;
            console.log("complete");
        },
        error: function () {
            console.log("error");
        }
    });
};

var submit = function (out_data) {
    var send = $.ajax({
        url: '/send_open_lab/',
        data: out_data,
        type: 'post',
        dataType: 'json',
        success: function (data) {

        },
        error: function () {
            console.log("error");
        }
    });
};

$(document).ready(function () {

    var $lcid = $('#id_lcid');
    get_lab($lcid.val());

    $('#add_button').click(function () {
        console.log("begin add");
        $(this).closest('tr').before(one_line);
        console.log("end add");
    });

    $(document).on('click', '.delete_one_detail', function () {
        console.log("begin delete this detail");
        $(this).closest('tr').remove();
        console.log("end delete this detail");
    });

    $lcid.change(function () {
        get_lab($(this).val());
        $('.detail_one_line').remove();
        console.log('remove all');
    });

    $('#submit').click(function () {
        var date_list = Array();
        $('input[name="date"]').each(function () {
            date_list.push($(this).val());
        });

        var lid_list = Array();
        $('input[name="lid"]').each(function () {
            lid_list.push($(this).val());
        });

        var begin_list = Array();
        $('input[name="begin_time"').each(function () {
            begin_list.push($(this).val());
        });

        var end_list = Array();

    });

});
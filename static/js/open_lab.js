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
            '<td class = "error">' +
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

var succcess_handle = function (data) {
    var $detail_list = $('.detail_one_line');

    if (data[0]['result'] == 'e') {
        alert("Their is some error");
    } else if (data[0]['result'] == 's') {
        confirm('你的开放计划已经提交，请等待管理员审核');
        location.reload();
    } else {
        for (var i = 0; i < data.length; ++i) {
            $detail_list.eq(data[i]).find('.error').
                append('<p style="color:red">改行与已有开放计划的时间冲突</p>');
        }
    }
};

var one_time_handle = function () {

    var detail_list = new Array();
    var lid_list = new Array();
    var begin_list = new Array();
    var end_list = new Array();
    $('.detail_one_line').each(function () {
        var lid = $(this).find('select[name="lid"]').val();
        var date = $(this).find('input[name="date"]').val();
        var begin_time = new Date(date);
        console.log('lid:' + lid);
        lid_list.push(lid);
        begin_time.setHours($(this).find('select[name="begin_time"]').val());
        begin_list.push(date + ' ' + $(this).find('select[name="begin_time"]').val());
        var end_time = new Date(date);
        end_time.setHours($(this).find('select[name="end_time"]').val());
        end_list.push(date + ' ' + $(this).find('select[name="end_time"]').val());
        for (var i = 0; i < detail_list.length; ++i) {
            if (detail_list[i][0] != lid)continue;
            var begin = detail_list[i][1];
            var end = detail_list[i][2];
            if (begin_time < end && end_time > begin) {
                $(this).find('.error').append('<p style="color:red">与第' + i + '行时间冲突</p>');
            }
        }
        detail_list.push(new Array(lid, begin_time, end_time));
    });

    var olname = $('input[name="olname"]').val();
    var lcid = $('select[name="lcid"]').val();

    console.log('lid_list:' + lid_list);

    $.ajax({
        url: '/send_open_lab/',
        data: {
            lcid: lcid,
            olname: olname,
            csrfmiddlewaretoken: $('input[name="csrfmiddlewaretoken"]').val(),
            lid: lid_list,
            begin_time: begin_list,
            end_time: end_list
        },
        type: 'post',
        dataType: 'json',
        success: function (data) {
            succcess_handle(data);
        },
        error: function () {
            console.log("error");
        }
    });
};

var circle_handle = function () {

};

$(document).ready(function () {

    var $lcid = $('#lcid');
    get_lab($lcid.val());

    $('#add_button').click(function () {
        console.log("begin add");
        $(this).closest('tr').before(one_line);
        $('select').selectmenu();
        $('input[type="button"]').button();
        console.log("end add");
    });

    $(document).on('click', '.delete_one_detail', function () {
        console.log("begin delete this detail");
        $(this).closest('tr').remove();
        console.log("end delete this detail");
    });

    $lcid.selectmenu({
        change: function (event, ui) {
            get_lab($(this).val());
            $('.detail_one_line').remove();
            console.log('remove all');
        }
    });

    $(document).on('blur', 'input', function () {
        var $this = $(this);
        if (!$this.val()) {
            console.log('input empty');
            $this.addClass('empty');
        } else {
            console.log('input filed');
            if ($this.hasClass('empty')) {
                $this.removeClass('empty');
            }
        }
    });

    $('#submit').click(function () {
        $('.error').empty();
        var empty = false;
        $('input').each(function () {
            if (!$(this).val()) {
                empty = true;
                $(this).addClass('empty');
            }
        });

        if (empty) {
            return;
        }

        var type = $('select[name="type"]').val();
        if (type == 1) {
            one_time_handle();
        } else if (type == 2) {
            circle_handle();
        }
    });

});
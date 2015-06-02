/**
 * Created by wlw on 15-1-9.
 */
var page_number = 0;
var page_size = 10;

var wrap_one_line = function (one_item) {
    var one_line = '<tr>' +
        '<td>' + one_item['olname'] + '</td>' +
        '<td>' + one_item['uname'] + '</td>' +
        '<td>' + one_item['lcname'] + '</td>' +
        '<td>' + one_item['type'] + '</td>' +
        '<td>' + one_item['begin_date_time'] + '</td>' +
        '<td>' + one_item['end_date_time'] + '</td>' +
        '<td>' +
        '<a class="button" href="detail/' + one_item['olid'] + '/">详情</a>' +
        '</td>' +
        '</tr>';
    console.log('one_line:' + one_line)
    return one_line;
};

var error_handle = function () {
    alert("网络有问题，请稍后再试");
};

//var wrap_one_time_one_line=function(one_item){
//    return '<tr>' +
//        '<td>' +
//        ''
//};

//var display_one_time_detail=function(data){
//    var detail_table = '<table>' +
//        '<tr>' +
//        '<th>实验室</th>' +
//        '<th>日期</日期>' +
//        '<th>开始时间</th>' +
//        '<th>结束时间</th>' +
//        '</tr>'
//
//    for(var i=0;i<data.length;++i)
//    {
//        detail_table  +=
//    }
//};

var display_circle_detaail = function (data) {
};

var add_more_open_lab = function () {

    $.ajax({
        url: '/check_open_lab/get_uncheck_open_lab/',
        data: {
            begin_line_number: page_number * page_size,
            page_size: page_size,
            csrfmiddlewaretoken: $('input[name="csrfmiddlewaretoken"]').val()
        },
        type: 'post',
        dataType: 'json',
        success: function (data) {
            console.log("succsee send");
            page_number += 1;
            console.log('page_number:' + page_number);
            console.log('data:' + data);
            console.log('result:' + data['result']);
            if (data['result'] == 'e') {
                alert("something error");
            } else if (data['result'] == 'no_more') {
                $('#more').remove();
                $('#content').append(no_more);
            } else if (data['result'] == 'success') {
                console.log('append');
                var inner_line = '';
                var more_opne_lab = data['uc_ol'];
                for (var i = 0; i < more_opne_lab.length; ++i) {
                    inner_line += wrap_one_line(more_opne_lab[i]);
                }
                $('table').append(inner_line);
            } else {
                console.log("no use part");
            }
            $('.button').button();
        },
        error: function () {
            error_handle();
        }
    });
};

var no_more = '<div id="no_more">没有未审核的申请了</div>';

//var get_detail = function(olid, success_handler){
//    $.ajax({
//        url:'',
//        data:{
//            csrfmiddlewaretoken: $('input[name="csrfmiddlewaretoken"]').val(),
//            olid: olid
//        },
//        type:'post',
//        dataType: 'json',
//        success:function(data){
//
//        },
//        error:function(){
//            error_handle();
//        }
//    });
//};

$(document).ready(function () {
    add_more_open_lab();
    $('#more').click(function () {
        add_more_open_lab();
    });
});
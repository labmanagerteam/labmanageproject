/**
 * Created by wlw on 15-2-1.
 */

var list = [
    '<table>' +
    '<tr>' +
    '<th>学号</th>' +
    '<td><input type ="text" name="uid" /></td>' +
    '</tr>' +
    '<tr>' +
    '<th>姓名</th>' +
    '<td><input name="uname"/></td>' +
    '</tr>' +
    '<tr>' +
    '<th>密码</th>' +
    '<td><input name="password"/></td>' +
    '</tr>' +
    '<tr>' +
    '<th>卡号</th>' +
    '<td><input name="card_number"/></td>' +
    '</tr>' +
    '<tr>' +
    '<th>院系编号</th>' +
    '<td><input name="did"/></td>' +
    '</tr>' +
    '<tr>' +
    '<th>年级（以“入学年份 （本/研）”的形式）<th>' +
    '</td><input name="grade"/></td>' +
    '</tr>' +
    '</table>',

    '<table>' +
    '<tr>' +
    '<th>工号</th>' +
    '<td><input name="uid" /></td>' +
    '</tr>' +
    '<tr>' +
    '<th>姓名</th>' +
    '<td><input name="uname" /></td>' +
    '</tr>' +
    '<th>密码</th>' +
    '<td><input name="password"/></td>' +
    '</tr>' +
    '<th>卡号</th>' +
    '<td><input name="card_number"/></td>' +
    '</tr>' +
    '<tr>' +
    '<th>实验中心代码</th>' +
    '<td><input name="lcid"/></td>' +
    '</tr>' +
    '</table>'
];

var one_url_list = [
    '/add_user/one_student/',
    '/add_user/one_teacher/'
];

var generate_one_line = function (val) {
    console.log("generate one line");
    var one_line = list[val];
    var $one_item = $('#one_item form .change_field');
    $one_item.empty();
    $one_item.append(one_line);
    console.log("action changed");
    $('#one_item form').attr("action", one_url_list[val]);
};

var generate_list_url = function (val) {
    var list_url = ['/add_user/student_list/', '/add_user/teacher_list'];
    var url = list_url[val];
    $('#list_item form').attr("action", url);
};

var generate = function (val) {
    generate_one_line(val);
    generate_list_url(val);
};

$(document).ready(function () {

    var $cato = $('#catagory');
    generate($cato.val());

    $cato.change(function () {
        var val = $(this).val();
        generate(val);
    });

    $(document).on('submit', '#one_form', function () {
        $(this).ajaxSubmit({
            dataType: 'json',
            success: function (data) {
                if (data['result'] == 'success') {
                    confirm("添加成功");
                } else {
                    confirm(data['msg']);
                }
            },
            error: function () {
                alert("网络异常，请稍后再试");
            }
        });
        return false;
    });

    $(document).on('submit', '#list_form', function () {
        $(this).ajaxSubmit({
            dataType: 'json',
            success: function (data) {

            }
        });
        return false;
    });
});
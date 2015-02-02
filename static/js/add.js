/**
 * Created by wlw on 15-2-1.
 */

var list = [
    '<table>' +
    '<tr>' +
    '<th>学号</th>' +
    '<td><input name="uid" /></td>' +
    '</tr>' +
    '<tr>' +
    '<th>姓名</th>' +
    '<td><input name="uname"/></td>' +
    '</tr>' +
    '<tr>' +
    '<th>院系</th>' +
    '<td><input name="department"/></td>' +
    '</tr>' +
    '<tr>' +
    '<th>年级<th>' +
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
    '<tr>' +
    '<th>实验中心代码</th>' +
    '<td><input name="lcid"/></td>' +
    '</tr>'
];

var generate_one_line = function (val) {
    var one_line = list[val];
    var $one_item = $('#one_item');
    $one_item.empty();
    $one_item.append(one_line);
};

var generate_list_url = function (val) {
    var list_url = [];
    return list_url[val];
};

$(document).ready(function () {
    $('#catagory').change(function () {
        var val = $(this).val();
        generate_one_line(val);
    });
});
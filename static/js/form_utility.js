/**
 * Created by wlw on 15-2-25.
 */

var get_input = function (name, arr) {
    var l = [];
    console.log(name + ':');
    for (var i in arr) {
        if (arr[i]['name'] == name) {
            console.log(arr[i]['value']);
            l.push(arr[i]['value']);
        }
    }
    return l;
};

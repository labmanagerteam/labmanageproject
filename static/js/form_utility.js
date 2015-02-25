/**
 * Created by wlw on 15-2-25.
 */

var get_input = function (name, arr) {
    for (var i in arr) {
        if (arr[i]['name'] == name) {
            return arr[i]['value'];
        }
    }
}

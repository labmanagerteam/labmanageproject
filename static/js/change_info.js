/**
 * Created by wlw on 15-2-21.
 */

$(document).ready(function () {
    $('#change_dialog').dialog({
        buttons: [{
            text: '修改', click: function () {
                console.log("submit");
                $('#submit_change').closest('form').submit();
            }
        },
            {
                text: '取消', click: function () {
                $(this).dialog('close')
            }
            }],
        modal: true,
        autoOpen: false
    });

    $('.change_info_button').click(function () {
        fill_info($(this));
        $('#change_dialog').dialog('open');
    });
});

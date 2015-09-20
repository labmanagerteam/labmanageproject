options = {
    dataType: 'json',
    success: function (data) {
        if (data['result'] == 'success') {
            confirm("添加成功");
            $('input[type="text"]').each(function () {
                $(this).val("");
            });
            $('select').val("");
            //location.reload();
        } else {
            confirm(data['msg']);
        }
    },
    error: function () {
        alert("网络异常，请稍后再试");
    }
};


$(document).ready(function () {

    //generate_all();

    $(document).on('submit', '.one_form', function () {
        $(this).ajaxSubmit(options);
        return false;
    });

    $(document).on('submit', '.list_form', function () {
        $(this).ajaxSubmit(options);
        return false;
    });
});
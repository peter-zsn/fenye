/**
 * Created by peter on 2017/7/19.
 */
function showpwd(id) {
    $.ajax({
        url: '',
        type: 'post',
        data: {"id": id},
        success: function (data) {
            data = $.parseJSON(data);
            alert('密码是: ' + data.data.pwd);
        }
    })
}

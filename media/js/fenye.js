/**
 * Created by peter on 2017/7/19.
 */
function showpwd(id) {
    $.ajax({
        url: '',
        type: 'post',
        data: {"id": id},
        dataType: 'json',
        success: function (data) {
            // data = $.parseJSON(data);
            console.log(data);
            alert('密码是: ' + data.data.pwd);
        }
    })
}

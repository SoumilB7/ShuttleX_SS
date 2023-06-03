$(document).ready(function() {
    $('#submit-btn').click(function() {
        var input = $('#input-field').val();
        $.ajax({
            type: 'POST',
            url: 'http://192.168.43.170:5000/process_data',
            contentType: 'application/json',
            data: JSON.stringify({input: input}),
            success: function(data) {
                $('#output-field').val(data.output);
            },
            error: function(xhr, status, error) {
                console.error(status + ': ' + error);
            }
        });
    });
    $('#camera-btn').click(function() {
        input = "cam$$";//$('#input-field').val();
        $.ajax({
            type: 'POST',
            url: 'http://192.168.43.170:5000/process_data',
            contentType: 'application/json',
            data: JSON.stringify({input: input}),
            success: function(data) {
                $('#output-field').val(data.output);
            },
            error: function(xhr, status, error) {
                console.error(status + ': ' + error);
            }
        });



    });
});

var uid

var finalUID = document.getElementById("userMainpage")
function loginFunc()
{

    var user =document.getElementById("username")
    uid=user.value
    console.log(user.value)
    localStorage.username=uid


}

function loadFunc()
{

    console.log(uid)
    finalUID.innerHTML=localStorage.username

}


function testfunc()
{
    console.log("This works")

}
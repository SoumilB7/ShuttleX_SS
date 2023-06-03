$(document).ready(function() {
    $('#submit-btn1').click(function() {
        var input = "counter1"
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
    $('#submit-btn2').click(function() {
        var input = "counter2"
        $.ajax({
            type: 'POST',
            url: 'http://192.168.43.170:5000/process_data',
            contentType: 'application/json',
            data: JSON.stringify({input: input}),
            success: function(data) {
                $('#output-field2').val(data.output);
            },
            error: function(xhr, status, error) {
                console.error(status + ': ' + error);
            }
        });
    });
    $('#submit-btn3').click(function() {
        var input = "counter3"
        $.ajax({
            type: 'POST',
            url: 'http://192.168.43.170:5000/process_data',
            contentType: 'application/json',
            data: JSON.stringify({input: input}),
            success: function(data) {
                $('#output-field3').val(data.output);
            },
            error: function(xhr, status, error) {
                console.error(status + ': ' + error);
            }
        });
    });
    $('#submit-btn4').click(function() {
        var input = "counter4"
        $.ajax({
            type: 'POST',
            url: 'http://192.168.43.170:5000/process_data',
            contentType: 'application/json',
            data: JSON.stringify({input: input}),
            success: function(data) {
                $('#output-field4').val(data.output);
            },
            error: function(xhr, status, error) {
                console.error(status + ': ' + error);
            }
        });
    });
    $('#submit-btn5').click(function() {
        var input = "counter5"
        $.ajax({
            type: 'POST',
            url: 'http://192.168.43.170:5000/process_data',
            contentType: 'application/json',
            data: JSON.stringify({input: input}),
            success: function(data) {
                $('#output-field5').val(data.output);
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
                //$('#output-field').val(data.output);
            },
            error: function(xhr, status, error) {
                console.error(status + ': ' + error);
            }
        });
    });
    $('#btn1').click(function()
    {

        input = "personLocation";//$('#input-field').val();
        $.ajax({
            type: 'POST',
            url: 'http://192.168.43.170:5000/process_data',
            contentType: 'application/json',
            data: JSON.stringify({input: input}),
            success: function(data) {
                //$('#output-field').val(data.output);
                localStorage.shuttleLoc=data.output;
                console.log(data.output)
            },
            error: function(xhr, status, error) {
                console.error(status + ': ' + error);
            }
        });
        setTimeout(relocate,2000)
    });
});

var uid
function relocate()
{
    window.location.href = 'map.html'
}
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

function mapFunction()
{

}
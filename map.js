$(document).ready(function() {
    $('#Relod_button').click(function () {
        var input = "personLocation";//$('#input-field').val();
        $.ajax({
            type: 'Bus1',
            url: 'http://192.168.43.54:5000/process_data',
            contentType: 'application/json',
            data: JSON.stringify({input: input}),
            success: function (data) {
                $('#mapotpt').val(data.output);
                localStorage.bus1Data = data.output
                console.log(data.output)
            },
            error: function (xhr, status, error) {
                console.error(status + ': ' + error);
            }
        });
    });
});
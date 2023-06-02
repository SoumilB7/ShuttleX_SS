$(document).ready(function()
{
    $('#submit-btn').click(function()
    {
        var input = $('#input-field').val();
        $.ajax({
            type: 'POST',
            url: 'http://127.0.0.1:5000/process_data',
            contentType: 'application/json',
            data: JSON.stringify({input: input}),
            success: function(data)
            {
                $('#output-field').val(data.output);
            },
            error: function(xhr, status, error)
            {
                console.error(status + ': ' + error);
            }
        });
    });
});


function testfunc()
{
    console.log("This works")
}
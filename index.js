$(document).ready(function() {
    $('#submit-btn').click(function() {
      var input = $('#input-field').val();
      $.ajax({
        type: 'POST',
        url: 'http://192.168.43.54:5000/process_data',
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
        url: 'http://192.168.43.54:5000/process_data',
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
/*
// Handle form submission
document.getElementById('myForm').addEventListener('submit', function(event) {
  event.preventDefault();  // Prevent the default form submission

  var form = event.target;
  var formData = new FormData(form);

  // Make an HTTP POST request to the Flask backend
  fetch('/api/endpoint', {
      method: 'POST',
      body: formData
  })
  .then(function(response) {
      if (response.ok) {
          console.log('Request sent successfully');
          // Handle success response
      } else {
          console.error('Request failed');
          // Handle error response
      }
  })
  .catch(function(error) {
      console.error('Request failed:', error);
      // Handle network error
  });
});
inp = document.getElementById("") 
/*  
inp.addEventListener("click", () => {
  window.open("C:\Users\SOUMIL\JS_Start\Kiddu_GPT\templates\login.html")
})
*/
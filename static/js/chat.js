$(document).ready(function() {
    // Fetch and populate models
    $.ajax({
        url: '/models',
        method: 'GET',
        success: function(models) {
            models.forEach(function(model) {
                $('#model-select').append('<option value="' + model + '">' + model + '</option>');
            });
        },
        error: function() {
            console.log('Failed to fetch models from Ollama server');
        }
    });

    $('#chat-form').on('submit', function(event) {
        event.preventDefault();

        var message = $('#message-input').val();
        var model = $('#model-select').val();

        if (message.trim() === '' || !model) {
            return;
        }

        $('#chat-box').append('<div><strong>You:</strong> ' + message + '</div>');
        $('#message-input').val('');
        $('#chat-box').scrollTop($('#chat-box')[0].scrollHeight);

        $.ajax({
            url: '/chat',
            method: 'POST',
            contentType: 'application/json',
            data: JSON.stringify({ message: message, model: model }),
            success: function(response) {
                if (response && response.response) {
                    $('#chat-box').append('<div><strong>Ollama:</strong> ' + response.response + '</div>');
                } else {
                    $('#chat-box').append('<div><strong>Ollama:</strong> No response received</div>');
                }
                $('#chat-box').scrollTop($('#chat-box')[0].scrollHeight);
            },
            error: function(xhr, status, error) {
                console.log("Error: ", error);
                console.log("Status: ", status);
                console.log("Response: ", xhr.responseText);
                $('#chat-box').append('<div><strong>Error:</strong> Failed to communicate with Ollama server</div>');
                $('#chat-box').scrollTop($('#chat-box')[0].scrollHeight);
            }
        });
    });
});

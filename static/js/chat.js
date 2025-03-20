$(document).ready(function() {
    $('#chat-form').on('submit', function(event) {
        event.preventDefault();

        var message = $('#message-input').val();
        if (message.trim() === '') {
            return;
        }

        $('#chat-box').append('<div><strong>You:</strong> ' + message + '</div>');
        $('#message-input').val('');

        $.ajax({
            url: '/chat',
            method: 'POST',
            contentType: 'application/json',
            data: JSON.stringify({ message: message }),
            success: function(response) {
                $('#chat-box').append('<div><strong>Ollama:</strong> ' + response.response + '</div>');
                $('#chat-box').scrollTop($('#chat-box')[0].scrollHeight);
            },
            error: function() {
                $('#chat-box').append('<div><strong>Error:</strong> Failed to communicate with Ollama server</div>');
                $('#chat-box').scrollTop($('#chat-box')[0].scrollHeight);
            }
        });
    });
});

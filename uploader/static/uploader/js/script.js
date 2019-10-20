var users = [];
var requiredFields = ['email', 'first_name', 'last_name', 'birthday'];

$('#file').bind('change', function () {
    users = [];
    $('#users').text('');
    $('#logs').text('');
    var regex = /^([a-zA-Z0-9\s_\\.\-:])+(.csv|.txt)$/;
    if (regex.test($('#file').val().toLowerCase())) {
        if (typeof (FileReader) != 'undefined') {
            var reader = new FileReader();
            reader.onload = function (e) {
                var parsed = Papa.parse(e.target.result);
                if (parsed.errors.length) {
                    $('#logs').text(JSON.stringify(parsed.errors, null, 2));
                    return;
                }
                for (var i = 0; i < requiredFields.length; i++) {
                    if (parsed.data[0].indexOf(requiredFields[i]) < 0) {
                        $('#logs').text('Row ' + requiredFields[i] + ' is missing.');
                        return;
                    }
                }
                for (var i = 1; i < parsed.data.length; i++) {
                    if (parsed.data[i].length == 4) {
                        var user = {};
                        for (var j = 0; j < 4; j++) {
                            user[parsed.data[0][j]] = parsed.data[i][j]
                        }
                        users.push(user);
                    } else if (parsed.data[i].length > 1) {
                        $('#logs').text('Line ' + (i+1) + ' is invalid.');
                        return;
                    }
                }
                $('#users').text(JSON.stringify(users, null, 2));
            }
            reader.readAsText($('#file')[0].files[0]);
        } else {
            $('#logs').text('This browser does not support HTML5.');
        }
    } else {
        $('#logs').text('Please upload a valid CSV file.');
    }
});

$('#upload').bind('click', function () {
    if (users.length == 0) {
        return;
    }
    $.ajax({
        type: 'POST',
        url: window.API_URL,
        data: JSON.stringify(users),
        contentType: "application/json; charset=utf-8",
        dataType: "text"
    })
        .done(function (response) {
            $('#logs').html('<div style="color:green">Your data has been created.</div>');
        })
        .fail(function (xhr) {
            var errors = JSON.parse(xhr.responseText);
            $('#logs').text(JSON.stringify(errors, null, 2));
        });
});
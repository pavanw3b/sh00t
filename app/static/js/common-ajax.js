function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function getCSRFToken() {
    return getCookie('csrftoken');
}

function csrfSafeMethod(method) {
    /* these HTTP methods do not require CSRF protection */
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", getCSRFToken());
        }
    },
    contentType: 'application/json'
});

function sync(target) {
    $("#response").html("(Saving..)");
    setTimeout( function() {
        send(target);
    }, 1000);
}

function send(target) {
    switch(target) {
        case "flag":
            var title = JSON.stringify($("#title").val());
            var note = JSON.stringify($("#note").val());
            var done = JSON.stringify(false);
            if($("#done").is(":checked"))
                done = JSON.stringify(true);
            var assessment = JSON.stringify($("#assessment").val());
            $.ajax({
                url: "/api/flag/" + $("#id").val() + "/",
                data: '{"title": '+title+', "note": '+note+', "done": '+done+', "assessment": '+assessment+'}',
                type: 'PUT',
                success: function() {
                    $("#response").html("(Saved)");
                }
            });
            break;

        case "sh0t":
            var title = JSON.stringify($("#title").val());
            var body = JSON.stringify($("#body").val());
            var assessment = JSON.stringify($("#assessment").val());
            $.ajax({
                url: "/api/sh0t/" + $("#id").val() + "/",
                data: '{"title": ' + title + ', "body": '+ body +', "assessment": ' + assessment + '}',
                type: 'PUT',
                success: function() {
                    $("#response").html("(Saved)");
                }
            });
            break;

        case "assessment":
            var name = JSON.stringify($("#name").val());
            var project = JSON.stringify($("#project").val());
            $.ajax({
                url: "/api/assessment/" + $("#id").val() + "/",
                data: '{"name": ' + name + ', "project": ' + project + '}',
                type: 'PUT',
                success: function() {
                    $("#response").html("(Saved)");
                }
            });
            break;

        case "project":
            var name = JSON.stringify($("#name").val());
            $.ajax({
                url: "/api/project/" + $("#id").val() + "/",
                data: '{"name": ' + name + ' }',
                type: 'PUT',
                success: function() {
                    $("#response").html("(Saved)");
                }
            });
            break;

        default:
            alert("Invalid target");
    }
}

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
    timeout = setTimeout( function() {
        send(target);
    }, 2000);
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
            var severity = JSON.stringify($("#severity").val());
            var title = JSON.stringify($("#title").val());
            var body = JSON.stringify($("#body").val());
            var assessment = JSON.stringify($("#assessment").val());
            $.ajax({
                url: "/api/sh0t/" + $("#id").val() + "/",
                data: '{"title": ' + title +  ', "severity": ' + severity + ', "body": '+ body +', "assessment": ' + assessment + '}',
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

        case "template":
            var name = JSON.stringify($("#name").val());
            var body = JSON.stringify($("#body").val());
            $.ajax({
                url: "/api/template/" + $("#id").val() + "/",
                data: '{"name": ' + name + ', "body": '+ body +' }',
                type: 'PUT',
                success: function() {
                    $("#response").html("(Saved)");
                }
            });
            break;

        case "case_master":
            var name = JSON.stringify($("#name").val());
            var description = JSON.stringify($("#description").val());
            var order = JSON.stringify($("#order").val());
            var module = JSON.stringify($("#module_master").val())
            $.ajax({
                url: "/api/case-master/" + $("#id").val() + "/",
                data: '{"name": ' + name + ', "description": '+ description + ' , "order": ' + order + ', "module":' + module +' }',
                type: 'PUT',
                success: function() {
                    $("#response").html("(Saved)");
                }
            });
            break;

        case "module_master":
            var name = JSON.stringify($("#name").val());
            var description = JSON.stringify($("#description").val());
            var order = JSON.stringify($("#order").val());
            var methodology = JSON.stringify($("#methodology_master").val())
            $.ajax({
                url: "/api/module-master/" + $("#id").val() + "/",
                data: '{"name": ' + name + ', "description": '+ description + ' , "order": ' + order + ', "methodology":' + methodology +' }',
                type: 'PUT',
                success: function() {
                    $("#response").html("(Saved)");
                }
            });
            break;

        case "methodology_master":
            var name = JSON.stringify($("#name").val());
            var description = JSON.stringify($("#description").val());
            var order = JSON.stringify($("#order").val());
            $.ajax({
                url: "/api/methodology-master/" + $("#id").val() + "/",
                data: '{"name": ' + name + ', "description": '+ description + ' , "order": ' + order +' }',
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

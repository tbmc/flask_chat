
var socket;

$(document).ready(function() {
    socket = io.connect();

    socket.on("connect", function() {
        socket.emit("new_user", "")
    });
    socket.on("new_user", function(data) {
        // Nouvel utilisateur data.pseudo
        add_indication("Un nouvel utilisateur vient d'entrer dans le salon : <b>" + data.pseudo + "</b>");
    });
    socket.on("message", function(data) {
        console.log("Nouveau message", data.message);
        add_message(data.pseudo, data.message)
    });

    var text = $("#text_message");
    $("#send_button").on("click", send_message);


    function send_message() {
        var v = text.val();
        text.val("");
        console.log(v)
        if(v.length > 0) {
            socket.emit("message", {
                message: v
            });
        }
    }


    function add_indication(indic) {
        var t = "<p class='indication'>" + indic + "</p>";
        add_html_message(t);
    }

    function add_message(pseudo, msg, is_from_me) {
        var t = "";
        if(is_from_me) {
            t = "from_me";
        }
        var p = "<span class='pseudo'>" + pseudo + "</span>";
        var m = "<span class='message'>" + msg + "</span>"
        var html = "<p class='message " + t + "'>" + p + m + "</p>";
        add_html_message(html)
    }

    var scroll_to_bottom = false;
    function add_html_message(html) {
        var e = $("#messages-list");
        e.append(html);
        if(scroll_to_bottom)
            clearTimeout(scroll_to_bottom);
        scroll_to_bottom = setTimeout(function() {
            e.animate({
                scrollTop: e.prop("scrollHeight")
            }, 100);
            scroll_to_bottom = false;
        }, 100)
    }



    $(".btn-theme .theme-click").click(change_theme);

    function change_theme(event) {
        var css, txt;
        var themes = window.themes;
        var t = themes.list;
        if(event) {
            var e = event.currentTarget;
            css = e.getAttribute("theme-filename");
            txt = e.innerText;
        }else if(localStorage['theme']) {
            var ls = JSON.parse(localStorage['theme']);
            css = ls.filename;
            txt = ls.text;
        }else {
            txt = t[0];
            css = t[1];
        }
        $("link[link-type='theme']").attr("href", themes.path + css);
        $(".btn-theme span.theme-text").text(txt);
        localStorage['theme'] = JSON.stringify({
            text: txt,
            filename: css,
        });
    }

    change_theme(null);

});


/*
Source de la fonction :
http://werxltd.com/wp/2010/05/13/javascript-implementation-of-javas-string-hashcode-method/
 */
String.prototype.hashCode = function() {
    var hash = 0;
    if(this.length === 0)
        return hash;
    for(var i = 0, len = this.length, c; i < len; i++) {
        c = this.charCodeAt(i);
        hash = ((hash << 5) - hash) + c;
        hash |= 0; // Converti le hash en entier de 32 bits
    }
    return hash;
};




$(function() {

    $('#search').focus();
    document.forms[0].onsubmit = function(e) {
        e.preventDefault();
        if (!$('#search').val()) {
            $('#search').focus();
            return false;
        }
        var url = '/s/' + encodeURIComponent($('#search').val()) + '.html';
        window.location = url;
        return false;
    };
});

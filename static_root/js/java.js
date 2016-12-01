$(function() {

    $('[id^="like-"]').click(function (e) {
        var self = this;
        e.preventDefault();
        $.ajax({
            type: "POST",
            url: "/addlike/",
            data: {'id': $(this).attr('name')
                // , 'csrfmiddlewaretoken': '{{ csrf_token }}'
            },
            dataType: "json",
            success: function (response) {

                $(self).val("Like " + response.likes_count);
            },
            error: function (rs, e) {
                alert("Aвторизируйтесь");
            }
        });
        return false
    })

});

$(function() {

    $('body').on('click', '[data-author-id^="follows-"]', function (e) {
        var self = this;
        console.log(self)
        e.preventDefault();
        $.ajax({
            type: "POST",
            url: "/follows/",
            data: {'id': $(this).attr('name')

            },
            dataType: "json",
            success: function (response) {

                alert(response.message)
                $("[data-author-id='"+$(self).attr("data-author-id")+"']").hide();


            },
            error: function (rs, e) {
                alert("Aвторизируйтесь");
            }
        });
        return false
    })

});

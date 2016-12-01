$(function() {

    $('[id^="follows-"]').click(function (e) {

        e.preventDefault();
        $.ajax({
            type: "POST",
            url: "/follows/",
            data: {'id': $(this).attr('name')

            },
            dataType: "json",
            success: function (response) {

                alert(response.message)
                document.getElementById("nameID").style.visibility = "hidden";
            },
            error: function (rs, e) {
                alert("Aвторизируйтесь");
            }
        });
        return false
    })

});

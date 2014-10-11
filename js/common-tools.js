(function() {
    function setClickable() {
        $('.clickable').click(function() {
            var url = $(this).attr('data-click-url');

            if(typeof url != typeof undefined) {
                location.href = url;
            }
        });
    }

    setClickable();
})();

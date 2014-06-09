(function() {
    function setClickable() {
        d3.selectAll('.clickable')
            .on('click', function() {
                location.href = this.getAttribute('data-click-url');
            });
    }

    setClickable();
})();

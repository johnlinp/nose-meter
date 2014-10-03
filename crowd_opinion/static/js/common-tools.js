(function() {
    function setClickable() {
        d3.selectAll('.clickable')
            .on('click', function() {
                if(this.getAttribute('data-click-url') != undefined) {
                    location.href = this.getAttribute('data-click-url');
                }
            });
    }

    setClickable();
})();

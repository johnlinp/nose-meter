(function() {
    function setCandidatesClick() {
        d3.selectAll('.clickable')
            .on('click', function() {
                location.href = this.getAttribute('data-click-url');
            });
    }

    setCandidatesClick();
})();

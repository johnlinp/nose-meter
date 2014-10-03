(function() {
    function setPromiseShow() {
        $('.single-promise').each(function() {
            var icon = $(this).find('.promise-icon');
            var brief = $(this).find('.promise-brief');
            var content = $(this).find('.promise-content');
            var stars = $(this).find('.promise-stars');
            var statuss = $(this).find('.promise-status');
            var progress = $(this).find('.promise-progress');

            brief.click(function() {
                if(icon.hasClass('fui-radio-checked')) {
                    content.slideDown();
                    icon.removeClass('fui-radio-checked')
                            .addClass('fui-radio-unchecked');
                } else if(icon.hasClass('fui-radio-unchecked')) {
                    content.slideUp();
                    icon.removeClass('fui-radio-unchecked')
                            .addClass('fui-radio-checked');
                }
            });

            stars.hover(function() {
                statuss.fadeIn('fast');
            }, function() {
                statuss.fadeOut('fast');
            });

            stars.click(function() {
                if(progress.hasClass('visible')) {
                    progress.slideUp();
                    progress.removeClass('visible');
                } else {
                    progress.slideDown();
                    progress.addClass('visible');
                }
            });
        });
    }

    setPromiseShow();
})();

(function() {
    angular.module('noseMeter')

        .directive('errSrc', function() {
            return {
                link: function(scope, element, attrs) {
                    element.bind('error', function() {
                        if (attrs.src != attrs.errSrc) {
                            attrs.$set('src', attrs.errSrc);
                        }
                    });
                }
            };
        })

        .directive('gotoUrl', function() {
            return {
                link: function(scope, element, attrs) {
                    element.bind('click', function() {
                        location.href = attrs.gotoUrl;
                    });
                }
            }
        });
})();


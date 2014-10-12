(function() {
    var app = angular.module('noseMeter', []);
    var districtName = window.location.hash.substring(1);

    app.controller('district', function ($scope) {
        $scope.districtName = districtName;
        $scope.candidates = [
            {
                name: '游錫堃',
            },
            {
                name: '朱立倫',
            },
            {
                name: '李進順',
            },
        ];
        $scope.gotoUrl = function(evt) {
            var url = evt.currentTarget.getAttribute('data-click-url');
            location.href = url;
        };
    });

    app.directive('errSrc', function() {
        return {
            link: function(scope, element, attrs) {
                element.bind('error', function() {
                    if (attrs.src != attrs.errSrc) {
                        attrs.$set('src', attrs.errSrc);
                    }
                });
            }
        }
    });
})();

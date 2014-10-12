(function() {
    var districtName = window.location.hash.substring(1);

    angular.module('noseMeter', [])

        .controller('district', function ($scope) {
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
        });
})();

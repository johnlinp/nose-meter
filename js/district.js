(function() {
    var districtName = window.location.hash.substring(1);
    if(districtName == '') {
        location.href = '/nose-meter/';
    }

    angular.module('noseMeter', ['firebase'])

        .controller('district', function ($scope, $firebase) {
            $scope.districtName = districtName;

            var ref = new Firebase('https://shining-torch-3460.firebaseio.com/district-info/' + districtName + '/');
            var sync = $firebase(ref);
            $scope.candidates = sync.$asObject();
        });
})();

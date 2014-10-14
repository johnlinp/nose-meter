(function() {
    var candidateName = window.location.hash.substring(1);
    if(candidateName == '') {
        location.href = '/nose-meter/';
    }

    angular.module('noseMeter', ['firebase'])

        .directive('singlePromise', function() {
            return {
                link: function(scope, element, attrs) {
                    var icon = $(element).find('.promise-icon');
                    var brief = $(element).find('.promise-brief');
                    var content = $(element).find('.promise-content');
                    var stars = $(element).find('.promise-stars');
                    var statuss = $(element).find('.promise-status');
                    var progress = $(element).find('.promise-progress');

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
                }
            };
        })

        .controller('candidate', function ($scope, $firebase) {
            var ref = new Firebase('https://shining-torch-3460.firebaseio.com/candidate-info/' + candidateName + '/');
            var sync = $firebase(ref);
            $scope.candidate = sync.$asObject();
            console.log($scope.candidates);
        });
})();

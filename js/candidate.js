(function() {
    var app = angular.module('noseMeter', []);
    var candidateName = window.location.hash.substring(1);

    app.controller('candidate', function ($scope) {
        $scope.candidate = {
            name: candidateName,
            party: '民主進步黨',
            educations: [
                '某某大學某某系',
                '某某大學某某所某某組',
            ],
            experiences: [
                {
                    name: '1993 宜蘭縣縣長',
                    promises: [
                        {
                            brief: '資訊立縣',
                            content: '推行宜蘭資訊化，普遍建立縣政資訊及查詢系統，增進行政效能與服務品質，提供各種最新訊息，以形成吸引高技工業投資的良好環境。',
                            scores: '★★☆☆☆',
                            'status': '提案已交付審查',
                            progresses: [
                                {
                                    'target': '某甲提案',
                                    'state': '已交付審查',
                                    'link': 'javascript: void(0);'
                                },
                                {
                                    'target': '某乙提案',
                                    'state': '已交付審查',
                                    'link': 'javascript: void(0);'
                                },
                            ],
                        },
                        {
                            brief: '文化立縣',
                            content: '結合藝文人士，推展傳統及本土文教活動，籌建文化園區，提振藝文水準。',
                            scores: '★☆☆☆☆',
                            'status': '已提出提案',
                            progresses: [
                                {
                                    'target': '某丙提案',
                                    'state': '已提出',
                                    'link': 'javascript: void(0);'
                                },
                            ],
                        },
                    ],
                },
                {
                    name: '1989 宜蘭縣縣長',
                    promises: [
                    ],
                },
            ],
        };
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

angular.module("indexApp",[])
    .controller("indexCtrl" , myCtrl);

function myCtrl($scope){
}



(function() {
    var loadTaiwan = function() {

        /* debug only, please simply ignore*/
//         d3.json('https://dl.dropboxusercontent.com/u/46636026/data/tw.json', function(data) {
        /*  */

        d3.json('data/tw.json', function(data) {

            adjustTaiwanSize();
            var topo = topojson.feature(data, data.objects.counties);
            var prj = d3.geo.mercator().center([120.979531, 23.978567]).scale(7800);
            var path = d3.geo.path().projection(prj);

            putCounties(topo, path);
        });
    };

    var adjustTaiwanSize = function() {
        var leftWidth = 0;
        // parseFloat(d3.select('#left').style('width').replace('px', ''));
        d3.select('#taiwan')
            .attr('width', screen.width - leftWidth - 100)
            .attr('height', screen.height - 300);
    };

    var putCounties = function(topo, path) {
        d3.select('#taiwan').selectAll('path')
            .data(topo.features)
            .enter()
            .append('path')
            .attr('d', path)
            .attr('fill', 'DarkGreen')
            .on('mouseover', function(d) {
                d3.selectAll('path')
                    .attr('fill', 'DarkGreen');
                d3.select(this)
                    .attr('fill', 'LawnGreen')
                    .style('cursor', 'pointer');
                d3.select('#county-name')
                    .text(d.properties.name);
            })
            .on('mouseout', function() {
                d3.selectAll('path')
                    .attr('fill', 'DarkGreen');
                d3.select('#county-name')
                    .text('');
            })
            .on('click', function(d) {
                console.log(d);
                location.href = 'district.html#' + d.properties.name;
            });
    };

    loadTaiwan();
})();

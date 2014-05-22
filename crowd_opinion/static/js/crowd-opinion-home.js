(function() {
    var loadTaiwan = function() {
        d3.json("/static/data/tw.json", function(data) {
            adjustTaiwanSize();

            var topo = topojson.feature(data, data.objects.counties);

            var prj = d3.geo.mercator().center([120.979531, 23.978567]).scale(6000);
            var path = d3.geo.path().projection(prj);

            putCounties(topo, path);
        });
    };

    var adjustTaiwanSize = function() {
        d3.select('#taiwan')
            .attr('width', screen.width - 500)
            .attr('height', '500');
        console.log(screen.width);
    };

    var putCounties = function(topo, path) {
        d3.select("#taiwan").selectAll("path")
            .data(topo.features)
            .enter()
            .append("path")
            .attr("d", path)
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
            });
    };

    loadTaiwan();
})();

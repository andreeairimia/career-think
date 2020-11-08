let data = [];
let features = ["Satisfaction", "Opportunities", "Finance", "Skills", "Improvement", "WorklifeBalance"];


// Generate user data and persona data
var user_values = {}
var persona = {}

features.forEach(f => user_values[f] = values['user_values'][f]);
features.forEach(f => persona[f] = values['persona'][f]);

data.push(user_values);
data.push(persona);


// svg for the chart
let svg = d3.select("#persona-chart").append("svg")
    .attr("class", "mini_container")
    .style("padding", "10px")
    .attr("width", 550)
    .attr("height", 520);


// Plot gridlines
let radialScale = d3.scaleLinear()
    .domain([0,10])
    .range([0,210]);
let ticks = [1,4,7,10];

ticks.forEach(t =>
    svg.append("circle")
    .attr("cx", 260)
    .attr("cy", 250)
    .attr("fill", "none")
    .attr("stroke", "gray")
    .attr("r", radialScale(t))
    .style("fill", "#CDCDCD")
    .style("stroke", "#CDCDCD")
    .style("fill-opacity", 0.1)
);

ticks.forEach(t =>
    svg.append("text")
    .attr("x", 263)
    .attr("y", 250 - radialScale(t))
    .style("font-family", "DejaVu Sans Mono, monospace")
    .style("font-size", "12px")
    .text((t).toString())
);


// Maps angle and value into svg coordinates
function angleToCoordinate(angle, value) {
    let x = Math.cos(angle) * radialScale(value);
    let y = Math.sin(angle) * radialScale(value);
    return {"x": 260 + x, "y": 250 - y};
}


// Plot axes
for (var i = 0; i < features.length; i++) {
    let ft_name = features[i];
    let angle = (Math.PI / 2) + (2 * Math.PI * i / features.length);
    let line_coordinate = angleToCoordinate(angle, 10);
    let label_coordinate = angleToCoordinate(angle, 11.2);

    // draw axis line
    svg.append("line")
    .attr("x1", 260)
    .attr("y1", 250)
    .attr("x2", line_coordinate.x)
    .attr("y2", line_coordinate.y)
    .style("stroke", "#CDCDCD")
    .style("stroke-width", "2px");

    // draw axis label
    svg.append("text")
    .attr("x", label_coordinate.x)
    .attr("y", label_coordinate.y)
    .attr("text-anchor", "middle")
    .style("font-family", "DejaVu Sans Mono, monospace")
    .style("font-size", "14px")
    .text(ft_name);
}


// Plot data
let line = d3.line()
    .x(d => d.x)
    .y(d => d.y);
let colors = ["#f79e02", "#025bf7"];

function getPathCoordinates(data_point) {
    let coordinates = [];
    for (var i = 0; i < features.length; i++){
        let ft_name = features[i];
        let angle = (Math.PI / 2) + (2 * Math.PI * i / features.length);
        coordinates.push(angleToCoordinate(angle, data_point[ft_name]));
    }
    return coordinates;
}


// draw the persona path element
svg.append("path")
    .datum(getPathCoordinates(data[1]))
    .attr("d",line)
    .style("stroke-dasharray", ("4, 4"))
    .attr("stroke-width", 2)
    .attr("stroke", colors[1])
    .attr("fill", colors[1])
    .attr("stroke-opacity", 1)
    .attr("opacity", 0.7)
    .style("fill-opacity", 0.6);


// draw the user path element
svg.append("path")
    .datum(getPathCoordinates(data[0]))
    .attr("d", line)
    .style("stroke-dasharray", ("4, 4"))
    .attr("stroke-width", 2)
    .attr("stroke", colors[0])
    .attr("fill", colors[0])
    .attr("stroke-opacity", 1)
    .attr("opacity", 0.7)
    .style("fill-opacity", 0.7);


// add value points on axes
for (var i=0; i<data.length; i++) {
    svg.selectAll("myCircles")
        .data(getPathCoordinates(data[i]))
        .enter().append("circle")
        .attr("class", "data-circle")
        .attr("r", 3)
        .style("fill", colors[i])
        .attr("cx", function(d) { return d.x; })
        .attr("cy", function(d) { return d.y; });
}
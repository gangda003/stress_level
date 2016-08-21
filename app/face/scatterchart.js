
var script1 = document.createElement("script");
//     script2 = document.createElement("script"),
//     newD3;


// function noConflict() {
//     newD3 = d3;
//     console.log("loaded old");
//     script2.type = 'text/javascript';
//     script2.src = "http://d3js.org/d3.v2.min.js";
//     script2.addEventListener("load", ready, false);
//     document.head.appendChild(script2);
// }

// function ready() {
//     console.log("loaded new");
//     console.log(d3, newD3);


// console.log(newD3);

function noConflict(){
var data = [[5,3], [10,17], [15,4], [2,8]];
var dataFootStep = [[4213, new Date(2016,3,1)],[3340, new Date(2016,3,2)],[2345,
new Date(2016,3,3)],[6756, new Date(2016,3,4)],[5543, new Date(2016,3,5)]];


var dataFootStep1 = [[2450, new Date(2016,3,1)],[6262, new Date(2016,3,2)],[4360,
new Date(2016,3,3)],[5644,  1459753200000],[8810, new Date(2016,3,5)]];


var margin = {top: 20, right: 15, bottom: 60, left: 60}
  , width = 960 - margin.left - margin.right
  , height = 500 - margin.top - margin.bottom;

var mindate = new Date(2016,2,31),
    maxdate = new Date(2016,3,6);
var x = d3.time.scale()
// var x = d3.scaleTime()
      .domain([mindate, maxdate])
.range([0, width]);



// var y = d3.scaleLinear()
var y = d3.scale.linear()
	      .domain([0, 10000])
	      .range([ height, 0 ]);


var chart = d3.select('body')
.append('svg:svg')
.attr('width', width + margin.right + margin.left)
.attr('height', height + margin.top + margin.bottom)
.attr('class', 'chart')

var main = chart.append('g')
.attr('transform', 'translate(' + margin.left + ',' + margin.top + ')')
.attr('width', width)
.attr('height', height)
.attr('class', 'main')


//vertical lines
chart.selectAll(".vline").data(d3.range(21)).enter()
    .append("line")
    .attr("x1", function (d) {
    return d * (width / 6)-width/6/2;
})
    .attr("x2", function (d) {
    return d * (width / 6)-width/6/2;
})
    .attr("y1", function (d) {
    return 0;
})
    .attr("y2", function (d) {
    return height;
})
    .style("stroke", "#c2c2d6")
    .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

  // draw the x axis
var xAxis = d3.svg.axis()
.scale(x)
.orient('bottom')
.tickFormat(d3.time.format("%b-%d")).
ticks(d3.time.day,1);
// .tickArguments([d3.timeDay.every(1)]);
// .tickArguments([d3.time.day]);


 // var xAxis = d3
 //  .axisBottom(x)
 //  .ticks(d3.timeDay, 1)
 //  .tickFormat(d3.timeFormat("%b-%d"))


main.append('g')
.attr('transform', 'translate(0,' + height + ')')
.attr('class', 'main axis date')
.call(xAxis);

  // draw the y axis
var yAxis = d3.svg.axis()
.scale(y)
.orient('left');

// var yAxis = d3
//   .axisLeft(y);
  // .ticks(d3.timeDay, 1)
  // .tickFormat(d3.timeFormat("%b-%d"))



main.append('g')
.attr('transform', 'translate(0,0)')
.attr('class', 'main axis date')
.call(yAxis);

 // console.log(newD3.version);


// d3.xml("values.xml", "application/xml", function(xml) {
//   d3.select("#chart")
//     .selectAll("div")
//     .data(xml.documentElement.getElementsByTagName("value"))
//     .enter().append("div")
//       .style("width", function(d) { return d.textContent * 10 + "px"; })
//       .text(function(d) { return d.textContent; });
// });


// newD3.xml("footprintleft.svg").mimeType("image/svg+xml").get(function(error, xml) {
// d3.xml("happy.svg").mimeType("image/svg+xml").get(function(error, xml) {
d3.xml("happy.svg","image/svg+xml", function(error, xml) {
  if (error) throw error;
  var svgObject = jQuery(xml.documentElement);
  svgObject.attr("width", 40);
  svgObject.attr("height", 50);
  svgObject.css("position","absolute")
  svgObject.attr("left", 20+x(20));
  svgObject.attr("top", 20+y(20));
  // svgObject.attr("fill-opacity",0.3);
  // svgObject.attr("style","stroke:black;stroke-opacity:0.7");



  // svgObject.attr("fill","red");



  createLeftFoot(jQuery("body"),dataFootStep);
  // createLeftFoot(jQuery("body"),dataFootStep1,"red");
  function createLeftFoot(obj, data)
  {
    var leftOffset = 20;
    jQuery.each(data, function(i,d){
      console.log(i+"-"+d);
      var tempx1 = d[1];
      var tempy1 = d[0];
      var xx1 = (margin.left+x(tempx1))-leftOffset;
      var yy1 = (margin.top+y(tempy1));
      var mydiv1 = jQuery("<div></div>");
      mydiv1.attr("id","mydiv1");
      var svgObjecttemp = svgObject.clone();
      // svgObjecttemp.attr("fill",color);
      // svgObjecttemp.attr("fill","blue");
      mydiv1.append(svgObjecttemp);
      mydiv1.css("top",yy1+"px");
      mydiv1.css("left",xx1+"px");
      mydiv1.css("position","absolute");
      obj.append(mydiv1);
    });
  }
});


// newD3.xml("footprintright.svg").mimeType("image/svg+xml").get(function(error, xml) {
// d3.xml("sad.svg").mimeType("image/svg+xml").get(function(error, xml) {
d3.xml("sad.svg","image/svg+xml", function(error, xml) {
// d3.xml("Smiley.svg").mimeType("image/svg+xml").get(function(error, xml) {
  if (error) throw error;
  var svgObjectright = jQuery(xml.documentElement);
  svgObjectright.attr("width", 50);
  svgObjectright.attr("height", 50);
  svgObjectright.css("position","absolute")
  svgObjectright.attr("left", 20+x(20));
  svgObjectright.attr("top", 20+y(20));
  // svgObjectright.attr("fill-opacity",0.3);
  // svgObjectright.attr("style","stroke:black;stroke-opacity:0.7");



  // svgObjectright.attr("fill","red");
  createrightFoot(jQuery("body"),dataFootStep1);
  function createrightFoot(obj, data)
  {
    var leftOffset = 20;
    jQuery.each(data, function(i,d){
      console.log(i+"-"+d);
      var tempx1 = d[1];
      var tempy1 = d[0];
      var xx1 = (margin.left+x(tempx1)+leftOffset);
      var yy1 = (margin.top+y(tempy1));
      var mydiv1 = jQuery("<div></div>");
      mydiv1.attr("id","mydiv1");
      var svgObjecttemp = svgObjectright.clone();
      // svgObjecttemp.attr("fill",color);
      // svgObjecttemp.attr("fill","blue");
      mydiv1.append(svgObjecttemp);
      mydiv1.css("top",yy1+"px");
      mydiv1.css("left",xx1+"px");
      mydiv1.css("position","absolute");
      obj.append(mydiv1);
    });
  }
});


}

// showSteps();

// }



script1.type = 'text/javascript';
// script1.src = "http://d3js.org/d3.v4.min.js";
script1.src = "http://d3js.org/d3.v3.min.js";
script1.addEventListener("load", noConflict, false);
document.head.appendChild(script1);




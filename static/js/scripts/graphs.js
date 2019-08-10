d3.json('static/data/collection.json', function (error, data){

  if(error){
    console.error(error);
  }
console.log(data);

var ndx = crossfilter(data);
var parseDate = d3.time.format("%Y/%m/%d").parse;

data.forEach(function(d) {
  console.log("createdDate:" + d.createdDate);
  var croppedDate = d.createdDate.substr(0,10);
  console.log("CroppedDate:" + croppedDate);
  d.date = d3.time.format("%Y/%m/%d").parse(croppedDate);
  
  console.log("Parsed CroppedDate: " + parseDate(croppedDate));
});
console.warn("*****************");
print_filter(data);
console.warn("*****************");
var createdDim = ndx.dimension(function(d) { return d.createdDate; }); 
var hits = createdDim.group();
var difficulty = ndx.dimension(function(d){ return d.recipie_difficulty;});
var difgroup = difficulty.group();
var minDate = createdDim.bottom(1)[0].date;
var maxDate = createdDim.top(1)[0].date;

// var hitslineChart  = dc.lineChart("#chart");
// hitslineChart
// 	.width(500).height(200)
// 	.dimension(createdDim)
// 	.group(hits)
//   .x(d3.time.scale().domain([minDate,maxDate]));

barchart = dc.barChart('#chart')
.width(500).height(500)
.dimension(difficulty)
.group(difgroup)
.margins({ top: 10, right: 50, bottom: 30, left: 50 })
.x(d3.scale.ordinal())
.xUnits(dc.units.ordinal)
.xAxisLabel("Difficulty")
.yAxis()
.ticks(1);



dc.renderAll();
});

//Print filter
function print_filter(filter){
	var f=eval(filter);
	if (typeof(f.length) != "undefined") {}else{}
	if (typeof(f.top) != "undefined") {f=f.top(Infinity);}else{}
	if (typeof(f.dimension) != "undefined") {f=f.dimension(function(d) { return "";}).top(Infinity);}else{}
	console.log(filter+"("+f.length+") = "+JSON.stringify(f).replace("[","[\n\t").replace(/}\,/g,"},\n\t").replace("]","\n]"));
} 
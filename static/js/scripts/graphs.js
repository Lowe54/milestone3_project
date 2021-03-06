drawall();
function drawall(){
  d3.json('static/data/collection.json', function (error, data){
    if(error){
      console.error(error);
    }
    var ndx = crossfilter(data);
    var difficulty = ndx.dimension(function(d){ return d.recipie_difficulty;});
    var mealtype = ndx.dimension(function(d){return d.recipie_mealtype;});
    var difgroup = difficulty.group();
    var mealgroup = mealtype.group();

    barchart = dc.barChart('#difficultychart')
    .width(500).height(500)
    .dimension(difficulty)
    .group(difgroup)
    .margins({ top: 10, right: 50, bottom: 30, left: 50 })
    .x(d3.scale.ordinal())
    .xUnits(dc.units.ordinal)
    .xAxisLabel("Difficulty")
    .yAxis()  
    .ticks(1);

    mealbarchart = dc.barChart('#mealtypechart')
    .width(500).height(500)
    .dimension(mealtype)
    .group(mealgroup)
    .margins({ top: 10, right: 50, bottom: 30, left: 50 })
    .x(d3.scale.ordinal())
    .xUnits(dc.units.ordinal)
    .xAxisLabel("MealType")
    .yAxis()
    .ticks(1);

    dc.renderAll();
  });
}

resetchart = function(){
  $("#difficultychart").html("");
  $("#mealtypechart").html("");
  drawall();
  
};
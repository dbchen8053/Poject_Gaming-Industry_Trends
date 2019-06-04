
  var url = '/videogame'
  d3.json(url).then(function(data) {
    var trace1 = {
      x: data.Year,
      y: data.NA_Sales,
      name: "NA Sales",
      type: "bar"

    };

    var trace2 = {
      x: data.Year,
      y: data.EU_Sales,
      name: "EU Sales",
      type: "bar"

    };
    var trace3 = {
      x: data.Year,
      y: data.JP_Sales,
      name: "JP Sales",
      type: "bar"

    };
    var trace4 = {
      x: data.Year,
      y: data.Other_Sales,
      name: "Other Sales",
      type: "bar"

    };

    var data = [trace1, trace2, trace3, trace4];

    
    var layout1 = {
      title: 'Sales by Region',
      margin: { t: 30, b: 100 }, 
      barmode: "stack",
      xaxis: {
        title : {text : "Year"}
      },
      yaxis: {
        title : {text : "Sales (Million)"}
      }
    };
    
    Plotly.newPlot("bar", data, layout1);


  })

  var defaultURL = "/NA_sales_year";
  d3.json(defaultURL).then(function(data) {
    var data = [data]
    var layout = { 
      title: "Sales",
      margin: { t: 30, b: 100 }, 
      xaxis: {
        title : {text : "Year"}
      },
      yaxis: {
        title : {text : "Sales (Million)"}
      }
    };
    Plotly.plot("bar1", data, layout);
  });

  function updatePlotly(newdata) {
    Plotly.restyle("bar1", "x", [newdata.x]);
    Plotly.restyle("bar1", "y", [newdata.y]);
    Plotly.restyle("bar1", "marker", [newdata.marker]);
  }

  function getData(route) {
    console.log(route);
    d3.json(`/${route}`).then(function(data) {
      console.log("newdata", data);
      updatePlotly(data);
    });
  }



  var genre_pie = "/genre";
  d3.json(genre_pie).then(function(data) {
    var data = [data]
    var layout = {
      title: "Genre Distribution by Count of Title" 
      // margin: { t: 30, b: 100 } 
    };
    Plotly.plot("pie", data, layout);
  });

  var publisher_bar = "/publisher";
  d3.json(publisher_bar).then(function(data) {
    var data = [data]
    var layout = { 
      title: "Top 10 Publisher over 40 years", 
      margin: { t: 30, b: 100 },
      yaxis: {
        title : {text : "Game Released"}
      }
    };
    Plotly.plot("bar2", data, layout);
  });

  var platform_bar = "/platform";
  d3.json(platform_bar).then(function(data) {
    var data = [data]
    var layout = { 
      title: "Top 10 Platform over 40 years", 
      margin: { t: 30, b: 100 },
      yaxis: {
        title : {text : "Game Released"
      },
        
      }
    };
    Plotly.plot("bar3", data, layout);
  });

  var url = '/genre_year'
  d3.json(url).then(function(data) {
    console.log (data)
    var action_year = [];
    var action_count = [];

    var adventure_year = [];
    var adventure_count = [];

    var fightling_year = [];
    var fighting_count = [];

    var misc_year = [];
    var misc_count = [];

    var platform_year = [];
    var platform_count = [];

    var puzzle_year = [];
    var puzzle_count = [];

    var racing_year = [];
    var racing_count = [];

    var rp_year = [];
    var rp_count = [];

    var shooter_year = [];
    var shooter_count = [];

    var simulation_year = [];
    var simulation_count = [];

    var sports_year = [];
    var sports_count = [];

    var strategy_year = [];
    var strategy_count = [];

    data.forEach(function(item){
      if (item.genre == "Action"){
        // console.log (item.year);
        console.log (item.genre);
        // console.log (item.genre_count)
        action_year.push(item.year);
        action_count.push(item.genre_count);
        // console.log (action_year);
        // console.log (action_count)
    }
    else if (item.genre == "Adventure"){
      // console.log (item.year);
      console.log (item.genre);
      // console.log (item.genre_count)
      adventure_year.push(item.year);
      adventure_count.push(item.genre_count);
      // console.log (adventure_year);
      // console.log (adventure_count)
  }

    else if (item.genre == "Fighting"){
      // console.log (item.year);
      console.log (item.genre);
      // console.log (item.genre_count)
      fightling_year.push(item.year);
      fighting_count.push(item.genre_count);

  }  
    else if (item.genre == "Misc"){
      // console.log (item.year);
      console.log (item.genre);
      // console.log (item.genre_count)
      misc_year.push(item.year);
      misc_count.push(item.genre_count);

  }  

    else if (item.genre == "Platform"){
      // console.log (item.year);
      console.log (item.genre);
      // console.log (item.genre_count)
      platform_year.push(item.year);
      platform_count.push(item.genre_count);

}  

    else if (item.genre == "Puzzle"){
      // console.log (item.year);
      console.log (item.genre);
      // console.log (item.genre_count)
      puzzle_year.push(item.year);
      puzzle_count.push(item.genre_count);

}  

    else if (item.genre == "Racing"){
      // console.log (item.year);
      console.log (item.genre);
      // console.log (item.genre_count)
      racing_year.push(item.year);
      racing_count.push(item.genre_count);

}  

    else if (item.genre == "Role-Playing"){
      // console.log (item.year);
      console.log (item.genre);
      // console.log (item.genre_count)
      rp_year.push(item.year);
      rp_count.push(item.genre_count);

}  

    else if (item.genre == "Shooter"){
      // console.log (item.year);
      console.log (item.genre);
      // console.log (item.genre_count)
      shooter_year.push(item.year);
      shooter_count.push(item.genre_count);

}  

    else if (item.genre == "Simulation"){
      // console.log (item.year);
      console.log (item.genre);
      // console.log (item.genre_count)
      simulation_year.push(item.year);
      simulation_count.push(item.genre_count);

}  

    else if (item.genre == "Sports"){
      // console.log (item.year);
      console.log (item.genre);
      // console.log (item.genre_count)
      sports_year.push(item.year);
      sports_count.push(item.genre_count);

} 

    else if (item.genre == "Strategy"){
      // console.log (item.year);
      console.log (item.genre);
      // console.log (item.genre_count)
      strategy_year.push(item.year);
      strategy_count.push(item.genre_count);

}   
  
  })

  var trace_action = {
    x: action_year,
    y: action_count,
    name: "Action",
    type: "scatter",
    mode: 'lines',
    line: {
      color: 'black',
      width: 3
    }
  };

  var trace_adventure = {
    x: adventure_year,
    y: adventure_count,
    name: "Adventure",
    type: "scatter",
    mode: 'lines',
    line: {
      color: 'brown',
      width: 3
    }

  };

  var trace_fighting = {
    x: fightling_year,
    y: fighting_count,
    name: "Fighting",
    type: "scatter",
    line: {
      width: 3
    }
  };

  var trace_misc = {
    x: misc_year,
    y: misc_count,
    name: "Misc",
    type: "scatter",
    line: {
      width: 3
    }

  };

  var trace_platform = {
    x: platform_year,
    y: platform_count,
    name: "Platform",
    type: "scatter",
    line: {
      width: 3
    }

  };

  var trace_puzzle = {
    x: puzzle_year,
    y: puzzle_count,
    name: "Puzzle",
    type: "scatter",
    line: {
      width: 3
    }

  };

  var trace_racing = {
    x: racing_year,
    y: racing_count,
    name: "Racing",
    type: "scatter",
    line: {
      width: 3
    }

  };

  var trace_rp = {
    x: rp_year,
    y: rp_count,
    name: "Role-Playing",
    type: "scatter",
    line: {
      width: 3
    }

  };

  var trace_shooter = {
    x: shooter_year,
    y: shooter_count,
    name: "Shooter",
    type: "scatter",
    line: {
      width: 3
    }

  };

  var trace_simulation = {
    x: simulation_year,
    y: simulation_count,
    name: "Simulation",
    type: "scatter",
    line: {
      width: 3
    }

  };

  var trace_sports = {
    x: sports_year,
    y: sports_count,
    name: "Sports",
    type: "scatter",
    line: {
      width: 3
    }

  };

  var trace_strategy = {
    x: strategy_year,
    y: strategy_count,
    name: "Strategy",
    type: "scatter",
    line: {
      width: 3
    }

  };

  var data_genre = [trace_action, trace_adventure, trace_fighting, trace_misc, trace_platform, trace_puzzle, trace_racing, trace_rp, trace_shooter, trace_simulation, trace_sports, trace_strategy]

  var layout_genre = {
    title: 'Genre Released',
    height: 600,
    width: 1200,
    legend: {
      font:{ size: 20,

    }},
    xaxis: {
      title : {text : "Year"}
    },
    yaxis: {
      title : {text : "Genre Count"}
    }

  };
  


  Plotly.newPlot("line1", data_genre, layout_genre);



  })




  
// function init() {
//   // Grab a reference to the dropdown select element
//   var selector = d3.select("#selDataset");

//   // Use the list of sample names to populate the select options
//   d3.json("/names").then((sampleNames) => {
//     sampleNames.forEach((sample) => {
//       selector
//         .append("option")
//         .text(sample)
//         .property("value", sample);
//     });

//     // Use the first sample from the list to build the initial plots
//     const firstSample = sampleNames[0];
//     buildCharts(firstSample);
//     buildMetadata(firstSample);
//   });
// }

// function optionChanged(newSample) {
//   // Fetch new data each time a new sample is selected
//   buildCharts(newSample);
//   buildMetadata(newSample);
// }

// // Initialize the dashboard
// init();



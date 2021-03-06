const data1 = {"x":[],"y":[]};
const data2 = {"x":[],"y":[]};

chart1_data= {
      labels: data1["x"],
      datasets: [{
        label :"sin",
        pointRadius: 4,
        pointBackgroundColor: "rgb(0,0,255)",
        data: data1["y"]
      }]
    }
chart1_options={
      scaleOverride: true,
        scaleSteps: 10,
        scaleStepWidth: 10,
        scaleStartValue: 0,
      legend: {display: true},
      responsive: true,
      title:{display: true,text:"MyChart1"},
      scales: {
      //Number - The scale starting value
      }
    }

chart2_data= {
        labels: data2["x"],
        datasets: [{
          label :"cos",
          pointRadius: 4,
          pointBackgroundColor: "rgb(0,0,255)",
          data: data2["y"]
        }]
      }
chart2_options={
        scaleOverride: true,
          scaleSteps: 10,
          scaleStepWidth: 10,
          scaleStartValue: 0,
        legend: {display: true},
        responsive: true,
        title:{display: true,text:"MyChart2"},
        scales: {
        //Number - The scale starting value
        }
      }

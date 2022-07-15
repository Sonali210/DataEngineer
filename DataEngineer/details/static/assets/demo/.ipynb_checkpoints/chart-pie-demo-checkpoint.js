// Set new default font family and font color to mimic Bootstrap's default styling
Chart.defaults.global.defaultFontFamily = '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
Chart.defaults.global.defaultFontColor = '#292b2c';

// Pie Chart Example
var ctx = document.getElementById("get5308");
var get5308 = new Chart(ctx, {
  type: 'pie',
  data: {
    labels: ["Discharge Capacity", "Nominal Capacity"],
    datasets: [{
      data: [2992.02, 3000],
      backgroundColor: ['#007bff', '#dc3545'],
    }],
  },
});

var ctx = document.getElementById("get5329");
var get5329 = new Chart(ctx, {
  type: 'pie',
  data: {
    labels: ["Discharge Capacity", "Nominal Capacity"],
    datasets: [{
      data: [2822.56, 3000],
      backgroundColor: ['#007bff', '#dc3545'],
    }],
  },
});

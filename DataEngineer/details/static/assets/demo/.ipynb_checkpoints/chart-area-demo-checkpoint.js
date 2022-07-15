// Set new default font family and font color to mimic Bootstrap's default styling
Chart.defaults.global.defaultFontFamily = '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
Chart.defaults.global.defaultFontColor = '#292b2c';

// Pie Chart Example
var ctx = document.getElementById("vt5308");
var vt5308 = new Chart(ctx, {
  type: 'line',
  data: {
    labels: ["2019-11-15T19:38:18Z", "2019-11-15T19:38:19Z", "2019-11-15T19:38:20Z", "2019-11-15T19:38:21Z", "2019-11-15T19:38:22Z", "2019-11-15T19:38:23Z","2019-11-15T19:38:23Z", "2019-11-15T19:38:23Z", "2019-11-15T19:38:23Z", "2019-11-15T19:38:23Z"],
    datasets: [{
      label: 'Voltage vs Time',
      data: [3.5897, 3.5897, 3.5897, 3.5897, 3.5897, 3.5897, 3.5621, 3.5621, 3.5897, 3.5897],
      backgroundColor: '#007bff',
    }],

  },
});

var ctx = document.getElementById("ct5308");
var ct5308 = new Chart(ctx, {
  type: 'line',
  data: {
    labels: ["2019-11-15T19:38:18Z", "2019-11-15T19:38:19Z", "2019-11-15T19:38:20Z", "2019-11-15T19:38:21Z", "2019-11-15T19:38:22Z", "2019-11-15T19:38:23Z","2019-11-15T19:38:23Z", "2019-11-15T19:38:23Z", "2019-11-15T19:38:23Z", "2019-11-15T19:38:23Z"],
    datasets: [{
      label: 'Current vs Time',
      data: [0.0, 0.0, 0.0, 0.0, 0.0, 0.0,-900.2,-900.2,0.0,0.0],
      backgroundColor: '#007bff',
    }],

  },
});

var ctx = document.getElementById("cat5308");
var cat5308 = new Chart(ctx, {
  type: 'line',
  data: {
    labels: ["2019-11-15T19:38:18Z", "2019-11-15T19:38:19Z", "2019-11-15T19:38:20Z", "2019-11-15T19:38:21Z", "2019-11-15T19:38:22Z", "2019-11-15T19:38:23Z","2019-11-15T19:38:23Z", "2019-11-15T19:38:23Z", "2019-11-15T19:38:23Z", "2019-11-15T19:38:23Z"],
    datasets: [{
      label: 'Capacity vs Time',
      data: [0.0, 0.0, 0.0, 0.0, 0.0, 0.0,0.0,0.025,0.0,0.0],
      backgroundColor: '#007bff',
    }],
  },

});


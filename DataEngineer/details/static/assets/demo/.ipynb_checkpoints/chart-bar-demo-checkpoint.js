// Set new default font family and font color to mimic Bootstrap's default styling
Chart.defaults.global.defaultFontFamily = '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
Chart.defaults.global.defaultFontColor = '#292b2c';

// Pie Chart Example
const labels =["2019-11-15T19:28:43Z","2019-11-15T19:28:44Z","2019-11-15T19:28:45Z","2019-11-15T19:28:46Z","2019-11-15T19:28:47Z","2019-11-15T19:28:48Z","2019-11-15T19:28:49Z","2019-11-15T19:28:49Z","2019-11-15T19:28:49Z","2019-11-15T19:28:49Z"];

const data = {
    labels: labels,
    datasets: [{
      label: 'Voltage vs Time',
      backgroundColor: 'rgb(255, 99, 132)',
      borderColor: 'rgb(255, 99, 132)',
      data: [3.59,3.59,3.59,3.59,3.59,3.59,3.5627,3.5627,3.5894,3.5894],
    }]
  };

  const config = {
    type: 'line',
    data: data,
    options: {}
  };

const myChart = new Chart(
    document.getElementById('vt5329'),
    config
  );

const labels1 =["2019-11-15T19:28:43Z","2019-11-15T19:28:44Z","2019-11-15T19:28:45Z","2019-11-15T19:28:46Z","2019-11-15T19:28:47Z","2019-11-15T19:28:48Z","2019-11-15T19:28:49Z","2019-11-15T19:28:49Z","2019-11-15T19:28:49Z","2019-11-15T19:28:49Z"];

const data1 = {
    labels: labels1,
    datasets: [{
      label: 'Current vs Time',
      backgroundColor: 'rgb(255, 99, 132)',
      borderColor: 'rgb(255, 99, 132)',
      data: [0.0, 0.0, 0.0, 0.0, 0.0, 0.0,-900.6,-900.6,0.0,0.0],
    }]
  };

  const config1 = {
    type: 'line',
    data: data1,
    options: {}
  };

const myChart1 = new Chart(
    document.getElementById('ct5329'),
    config1
  );

const labels2 =["2019-11-15T19:28:43Z","2019-11-15T19:28:44Z","2019-11-15T19:28:45Z","2019-11-15T19:28:46Z","2019-11-15T19:28:47Z","2019-11-15T19:28:48Z","2019-11-15T19:28:49Z","2019-11-15T19:28:49Z","2019-11-15T19:28:49Z","2019-11-15T19:28:49Z"];

const data2 = {
    labels: labels2,
    datasets: [{
      label: 'Capacity vs Time',
      backgroundColor: 'rgb(255, 99, 132)',
      borderColor: 'rgb(255, 99, 132)',
      data: [0.0, 0.0, 0.0, 0.0, 0.0, 0.0,0.0,0.025,0.0,0.0],
    }]
  };

  const config2 = {
    type: 'line',
    data: data2,
    options: {}
  };

const myChart2 = new Chart(
    document.getElementById('cat5329'),
    config2
  );

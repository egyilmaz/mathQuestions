console.log("client landing page")

var app = new Framework7({
  // App root element
  root: '#app',
  // App Name
  name: 'My App',
  // App id
  id: 'com.myapp.test',
  // Enable swipe panel
  panel: {
    swipe: 'left',
  },
  // Add default routes
  routes: [
  ],
  // ... other parameters
});
var mainView = app.views.create('.view-main');
// Init top demo gauge
var demoGauge = app.gauge.create({
  el: '.demo-gauge',
  type: 'circle',
  value: 0.5,
  size: 250,
  borderColor: '#2196f3',
  borderWidth: 10,
  valueText: '50%',
  valueFontSize: 41,
  valueTextColor: '#2196f3',
  labelText: 'amount of something',
});

var $$ = Dom7;
// Change demo gauge on button click
$$('.button').on('click', function () {
  var value = $$(this).attr('data-value');
  demoGauge.update({
    value: value / 100,
    valueText: value + '%'
  });
});
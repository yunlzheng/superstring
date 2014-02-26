'use strict';

angular.module('superString')
  .controller('HomeCtrl', ['$scope', function ($scope) {

      $.jqplot.config.defaultWidth = 170;
      $.jqplot.config.defaultHeight = 170;

      $scope.data = [[
          ['当前任务', 12],['', 88]
        ]];

      $scope.data2 = [[1,2,3,1,2,3,3,4,4,3,2,5,2]];


      $scope.lineOptions = {

          // Give the plot a title.
          title: '',
          // You can specify options for all axes on the plot at once with
          // the axesDefaults object.  Here, we're using a canvas renderer
          // to draw the axis label which allows rotated text.
          axesDefaults: {
            labelRenderer: $.jqplot.CanvasAxisLabelRenderer
          },
          grid: {
            drawGridLines: true,        // wether to draw lines across the grid or not.
            gridLineColor: '#fff',    // *Color of the grid lines.
            background: '#fff',      // CSS color spec for background color of grid.
            borderColor: '#fff',     // CSS color spec for border around grid.
            borderWidth: 2.0,           // pixel width of border around grid.
            shadow: false,               // draw a shadow for grid.
            shadowAngle: 45,            // angle of the shadow.  Clockwise from x axis.
            shadowOffset: 1.5,          // offset from the line of the shadow.
            shadowWidth: 3,             // width of the stroke for the shadow.
            shadowDepth: 3,             // Number of strokes to make when drawing shadow.
            shadowAlpha: 0.07          // Opacity of the shadow

            },
          // An axes object holds options for all axes.
          // Allowable axes are xaxis, x2axis, yaxis, y2axis, y3axis, ...
          // Up to 9 y axes are supported.
          axes: {
            // options for each axis are specified in seperate option objects.
            xaxis: {
              label: "",
              // Turn off "padding".  This will allow data point to lie on the
              // edges of the grid.  Default padding is 1.2 and will keep all
              // points inside the bounds of the grid.
              pad: 0
            },
            yaxis: {
              label: ""
            }
          }

      };

      $scope.chartOptions = {
          seriesDefaults: {
            // Make this a pie chart.
            renderer: jQuery.jqplot.PieRenderer,
            rendererOptions: {
              // Put data labels on the pie slices.
              // By default, labels show the percentage of the slice.
              showDataLabels: false
            }
          },
          grid: {
            drawGridLines: true,        // wether to draw lines across the grid or not.
            gridLineColor: '#fff',    // *Color of the grid lines.
            background: '#fff',      // CSS color spec for background color of grid.
            borderColor: '#fff',     // CSS color spec for border around grid.
            borderWidth: 2.0,           // pixel width of border around grid.
            shadow: false,               // draw a shadow for grid.
            shadowAngle: 45,            // angle of the shadow.  Clockwise from x axis.
            shadowOffset: 1.5,          // offset from the line of the shadow.
            shadowWidth: 3,             // width of the stroke for the shadow.
            shadowDepth: 3,             // Number of strokes to make when drawing shadow.
            shadowAlpha: 0.07          // Opacity of the shadow

        },
         legend: { show:false, location: 'e' }
      };

}]);
'use strict';

angular.module('superString')
  .controller('HelperCtrl', ['$scope', function ($scope) {

    var message = 'hello world';

    $scope.hello = message;

}]);

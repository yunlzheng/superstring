'use strict';

angular.module('superString')
  .controller('NavbarCtrl', function ($scope, $location) {
    $scope.menu = [{
      'title': '首页',
      'link': '#/'
    },
    {
      'title': '帮助',
      'link': '#/help'
    }];
    
    $scope.isActive = function(route) {
      return route === '#'+$location.path();
    };
  });

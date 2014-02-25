'use strict';

angular.module('superString')
  .controller('NavbarCtrl', function ($scope, $location) {
    $scope.menu = [{
      'title': '首页',
      'link': '#/',
      'icon': 'fa-home'
    },
    {
      'title': '计算',
      'link': '#/compute',
      'icon': 'fa-tachometer'
    },
    {
        'title': '存储',
        'link': '#/compute',
        'icon': 'fa-tasks'
    },
    {
        'title': '网络',
        'link': '#/compute',
        'icon': 'fa-cloud'
    },
    {
      'title': '文档',
      'link': '#/help',
      'icon': 'fa-star'
    },
    {
      'title': '设置',
      'link': '#/settings',
      'icon': 'fa-gear'
    }
    ];
    
    $scope.isActive = function(route) {
      return route === '#'+$location.path();
    };
  });

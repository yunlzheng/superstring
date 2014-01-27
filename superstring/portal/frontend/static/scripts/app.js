'use strict';

angular.module('superString', [
  'ngCookies',
  'ngResource',
  'ngSanitize',
  'ngRoute'
])
  .config(function ($routeProvider) {
    $routeProvider
      .when('/', {
        templateUrl: 'partials/home.html',
        controller: 'HomeCtrl'
      })
      .when('/help', {
        templateUrl: 'partials/helper.html',
        controller: 'HelperCtrl'
      })
      .otherwise({
        redirectTo: '/'
      });
  });
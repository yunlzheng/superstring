'use strict';

angular.module('superString', [
  'ngCookies',
  'ngResource',
  'ngSanitize',
  'ngRoute'
])
  .config(function ($routeProvider, $locationProvider) {
    $routeProvider
      .when('/', {
        templateUrl: 'partials/home',
        controller: 'HomeCtrl'
      }).
      .otherwise({
        redirectTo: '/'
      });
      
    //$locationProvider.html5Mode(true);
  });
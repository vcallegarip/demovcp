(function () {
  'use strict';

  angular
    .module('thinkster.routes')
    .config(config);

  config.$inject = ['$routeProvider'];

  function config($routeProvider) {
    $routeProvider.when('/', {
      controller: 'IndexController',
      controllerAs: 'vm',
      templateUrl: '/templates/layout/index.html'
    }).when('/register', {
      controller: 'RegisterController',
      controllerAs: 'vm',
      templateUrl: '/templates/authentication/register.html'
    }).when('/login', {
      controller: 'LoginController',
      controllerAs: 'vm',
      templateUrl: '/templates/authentication/login.html'
    }).otherwise({ redirectTo: '/' });
  }

})();

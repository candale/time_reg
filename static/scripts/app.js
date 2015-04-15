angular.module('TimeReg', [
  'TimeReg.controllers',
  'TimeReg.services',
  'xeditable',
  'ui.bootstrap',
]).config(function($interpolateProvider, $httpProvider){
    $interpolateProvider.startSymbol('[[').endSymbol(']]');

    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
}).run(function(editableOptions) {
  editableOptions.theme = 'bs3'; // bootstrap3 theme. Can be also 'bs2', 'default'
});

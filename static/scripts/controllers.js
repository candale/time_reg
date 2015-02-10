angular.module('TimeReg.controllers', [])
  .controller('RegistrationCtrl', function($scope, timeRegService) {
    $scope.date = moment().format('MM/DD/YYYY');
    timeRegService.getRegistrations().success(
      function(response) {
        $scope.registrations = response;
      });

    $scope.register = function() {
      var serverDelta = $scope.toServerDelta($scope.timeSpent);

      var message = {
        "registration_day": $scope.date,
        "task_code": $scope.taskCode,
        "project": $scope.project,
        "time": $scope.toServerDelta($scope.timeSpent),
        "source": "M"
      };
      console.log(message);

      timeRegService.newRegistration(message).success(function(response) {
        $scope.registrations.unshift(response);
      });
    };

    $scope.toClientDelta = function(delta) {
      delta_str = parseInt(delta);
      var hours = Math.floor(delta / 60);
      var minutes = (delta / 60) - hours;

      return hours.toString() + "." + (minutes.toFixed(1) * 10).toString() + "h";
    };

    $scope.toServerDelta = function(delta) {
      delta_float = parseFloat(delta);
      return delta_float * 60;
    };

    $scope.updateRegistration = function(data, regId) {
      data.id = regId;
      if(data.time.indexOf('h') > -1) {
        data.time = $scope.toServerDelta(
          data.time.substring(0, data.time.length - 1));
      } else {
        data.time = $scope.toServerDelta(data.time);
        $scope.time = $scope.time + "h";
      }
      data.source = "M";

      timeRegService.updateRegistration(regId, data);
    };

});
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
        "time_str": $scope.timeSpent,
        "source": "M"
      };
      console.log(message);

      timeRegService.newRegistration(message).success(function(response) {
        $scope.registrations.unshift(response);
      });
    };

    $scope.updateRegistration = function(data, regId) {
      data.id = regId;
      data.source = "M";

      timeRegService.updateRegistration(regId, data).success(function(response) {
        for(var timeReg in $scope.registrations) {

          if($scope.registrations[timeReg].id == response.id) {
            $scope.registrations[timeReg] = response;
          }
        }
      }).error(function(response) {
        var a = 1;
      });
    };

    $scope.checkEmptyText = function(data) {
      if(!data) {
        return "Cannot be empty";
      }
    };

    $scope.validateTime = function(data) {
      if(!data || isNaN(data)) {
        return "Invalid time";
      }
    }

    $scope.delete = function(data) {

    }

});
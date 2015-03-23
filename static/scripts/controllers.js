angular.module('TimeReg.controllers', [])
  .controller('RegistrationCtrl', function($scope, timeRegService, $timeout) {

    $scope.date = moment().format('MM/DD/YYYY');

    // get the data
    timeRegService.getRegistrations().success(
      function(response) {
        $scope.registrations = response;
      });

    // FUNCTION DECLARATIONS

    function clearAddFields() {
      $scope.taskCode = '';
      $scope.project = '';
      $scope.timeSpent = '';
      $scope.datePicker.dt = $scope.date;
    }


    $scope.register = function() {
      if(!($scope.datePicker.dt && $scope.taskCode && $scope.project && $scope.timeSpent)) {
        return;
      }
      var message = {
        "registration_day": $scope.datePicker.dt,
        "task_code": $scope.taskCode,
        "project": $scope.project,
        "time_str": $scope.timeSpent,
        "source": "M"
      };

      timeRegService.newRegistration(message).success(function(response) {
        $scope.registrations.unshift(response);
        clearAddFields();
      }).error(function(err) {
        $scope.errors = err;
        console.log($scope.errors);
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

    // date-picker
    $scope.datePicker = {};
    $scope.datePicker.format = 'MM/dd/yyyy';
    $scope.datePicker.dt = $scope.date;


    $scope.datePicker.open = function($event) {
      $timeout(function() {
        $scope.datePicker.opened = true;
        console.log('opened');
      })
    };

    $scope.disabled = function(date, mode) {
      return ( datePicker.mode === 'day' && ( date.getDay() === 0 || date.getDay() === 6 ) );
    };

    $scope.today = function() {
      $scope.datePicker.dt = new Date();
    };

    $scope.clear = function () {
      $scope.datePicker.dt = null;
    };

    $scope.toggleMin = function() {
      $scope.datePicker.minDate = $scope.datePicker.minDate ? null : new Date();
    };

    $scope.datePicker.dateOptions = {
      formatYear: 'yy',
      startingDay: 1
    };

    $scope.test = function() {
      console.log('loool');
    }

    $scope.openDatepickerForRecord = function(regId) {
      console.log('in openDatepickerForRecord' + regId.toString());
      for(reg in $scope.registrations) {
        if($scope.registrations[reg].id == regId) {
          console.log('did it');
          $scope.registrations[reg].datepicker_open = true;
          break;
        }
      }
    }

});
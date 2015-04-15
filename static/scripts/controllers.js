angular.module('TimeReg.controllers', ['toaster'])
  .controller('RegistrationCtrl', function($scope, timeRegService, toaster) {

    function updateHeaderStatistics() {
      timeRegService.getHeaderStatistics().success(
        function(response) {
          $scope.statistics = response;
        });
    }
        // get the data
    function updateList() {
      timeRegService.getRegistrations().success(
        function(response) {
          $scope.registrations = response;
          updateHeaderStatistics();
        });
    }

    $scope.date = moment().format('MM/DD/YYYY');
    $scope.errors = {};
    updateList();

    // FUNCTION DECLARATIONS

    function clearAddFields() {
      $scope.taskCode = '';
      $scope.project = '';
      $scope.timeSpent = '';
      $scope.datePicker.dt = $scope.date;
    }

    function markMandatory() {
      if(!$scope.datePicker.dt) {
        $scope.errors.registration_day = true;
      }

      if(!$scope.taskCode) {
        $scope.errors.task_code = true;
      }

      if(!$scope.project) {
        $scope.errors.project = true;
      }

      if(!$scope.timeSpent) {
        $scope.errors.time_str = true;
      }
    }

    function clearMandatory() {
      $scope.errors.registration_day = false;
      $scope.errors.task_code = false;
      $scope.errors.project = false;
      $scope.errors.time_str = false;
    }


    $scope.register = function() {
      if(!($scope.datePicker.dt && $scope.taskCode && $scope.project && $scope.timeSpent)) {
        toaster.warning("Warning!", "All fields are required");
        markMandatory()
        return;
      }
      var message = {
        "registration_day": moment($scope.datePicker.dt).format("MM/DD/YYYY"),
        "task_code": $scope.taskCode,
        "project": $scope.project,
        "time_str": $scope.timeSpent,
        "source": "M"
      };

      timeRegService.newRegistration(message).success(function(response) {
        updateList();
        clearAddFields();
        clearMandatory();
        toaster.success('Success', 'Sucessfully logged', 3000);
      }).error(function(err) {
        $scope.errors = err;
        console.log($scope.errors);
      });

    };

    $scope.updateRegistration = function(data, regId) {
      data.id = regId;
      data.source = "M";
      console.log(data);

      timeRegService.updateRegistration(regId, data).success(function(response) {
        for(var timeReg in $scope.registrations) {

          if($scope.registrations[timeReg].id == response.id) {
            $scope.registrations[timeReg] = response;
            toaster.success('Success', 'Updated successfully');
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

    $scope.delete = function(index) {
      regId = $scope.registrations[index].id;
      timeRegService.deleteRegistration(regId).success(function(response) {
        $scope.registrations.splice(index, 1);
        updateHeaderStatistics();
        toaster.success('Success', 'Deleted Sucessfully');
      }).error(function(err) {
        toaster.error('Error', 'Failed to delete');
      })
    }

    // date-picker
    $scope.datePicker = {};
    $scope.datePicker.format = 'MM/dd/yyyy';
    $scope.datePicker.opened = false;
    $scope.datePicker.dt = $scope.date;
    $scope.datePicker.open = function($event) {
      $scope.datePicker.opened = true;
    }

    $scope.today = function() {
      $scope.datePicker.dt = new Date();
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

    $scope.getHoursOffsetClass = function() {
      if(!angular.isUndefined($scope.statistics)) {
        if($scope.statistics.hoursOffset < -4) {
          return 'red-offset';
        } else if ($scope.statistics.hoursOffset < 4) {
          return '';
        } else {
          return 'green-offset';
        }
      }
    }

});

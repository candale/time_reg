angular.module('TimeReg.services', []).factory('timeRegService', function($http) {
    var timeRegApi = {};

    timeRegApi.getRegistrations = function() {
        return $http({
            method: 'GET',
            url: '/api/time_registrations/'
        });
    };

    timeRegApi.newRegistration = function(message) {
        return $http({
            method: 'POST',
            url: "/api/time_registrations/",
            data: message
        });
    };

    timeRegApi.updateRegistration = function(pk, message) {
        return $http({
            method: 'PUT',
            url: "/api/time_registrations/" + pk + "/",
            data: message
        });
    }

    return timeRegApi;
});
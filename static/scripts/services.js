angular.module('TimeReg.services', []).factory('timeRegService', function($http) {
    var timeRegApi = {};

    timeRegApi.getRegistrations = function() {
        return $http({
            method: 'GET',
            url: '/api/time_registrations.json'
        });
    };

    timeRegApi.newRegistration = function(message) {
        return $http({
            method: 'POST',
            url: "/api/time_registrations.json",
            data: message
        });
    };

    timeRegApi.updateRegistration = function(pk, message) {
        return $http({
            method: 'PUT',
            url: "/api/time_registrations/" + pk + ".json",
            data: message
        });
    }

    timeRegApi.deleteRegistration = function(pk) {
        return $http({
            method: 'DELETE',
            url: "/api/time_registrations/" + pk + ".json"
        });
    }

    timeRegApi.getHeaderStatistics = function() {
        return $http({
            method: 'GET', 
            url: '/api/statistics/header-statistics.json'
        });
    }

    return timeRegApi;
});

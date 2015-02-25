$(function() {
  $('#sandbox-container input').datepicker({
    format: "dd/mm/yyyy",
    todayBtn: "linked",
    calendarWeeks: true,
    todayHighlight: true
  });


  $.ajaxSetup({
    beforeSend: function(xhr, settings) {
      if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
        xhr.setRequestHeader("X-CSRFToken", csrftoken);
      }
    }
  });
});
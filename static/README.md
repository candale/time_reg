Angular-Xeditable has a problem, until further releases. Editable datepicker
is not customizable to show the calendar on input focus. That is changed in
file xeditable.js in editableBsdate directive.
buttonDatePicker and buttonWrapper should no longer be used (or made in such a
way that they should be customizable) and the ng-click handle shoule be put on
inputDatePicker.
Another thing that prevents the xeditable rows to perform properly is the
timeout from function $cancel in which the call to $hide is enclosed. If that
is not removed (the timout) cancel button does not work properly.

To install packages: bower install bower.json

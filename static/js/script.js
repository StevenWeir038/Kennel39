/* jshint esversion: 8 */

// Test connection
console.log("Connection to static/js/script.js - OK")

/**
 * Datepicker widget
 * Long date format
 * Limit date range from today to 12 months hence
 * 
*/
$(document).ready(function() {
    $( "#datepicker" ).datepicker({ dateFormat: "DD, d MM, yy", minDate: +0, maxDate: "+12M +0D" });
    $( "#datepicker" ).datepicker("option", "showAnim", "fold");
    $( "#datepicker" ).datepicker("setDate", '0');
});
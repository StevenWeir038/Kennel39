/* jshint esversion: 8, jquery: true */


/**
 * Datepicker widget
 * Long date format
 * Limit date range from today + 12 months
*/
$(document).ready(function() {
    $( "#datepicker" ).datepicker({ dateFormat: "MM d, yy", minDate: +0, maxDate: "+12M +0D" });
    $( "#datepicker" ).datepicker("option", "showAnim", "fold");
    $( "#datepicker" ).datepicker("setDate", '0');
});


// live filter of datepicker
const datepicker = document.getElementById("datepicker");
const filterResults = (e) => {
    let resultRows = document.querySelectorAll(".booking-row");
    let filterData = datepicker.value;
    resultRows.forEach(row => {
        row.classList.add("d-none");
        if (row.innerText.includes(filterData)) {
            row.classList.remove("d-none");
        }
    });
}
$(datepicker).on("change", filterResults);
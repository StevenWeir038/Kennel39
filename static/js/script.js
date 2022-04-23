/* jshint esversion: 8, jquery: true */


// filter view-booking-table by current user
const currentUser = document.getElementById("current-user");
const myBookingsBtn = document.getElementById("table-filter-user");
const myBookingsFilter = (e) => {
    let resultRows = document.querySelectorAll(".booking-row");
    let filterUser = currentUser.innerText;
    resultRows.forEach(row => {
        row.classList.add("d-none");
        if (row.innerText.includes(filterUser)) {
            row.classList.remove("d-none");
        }
    });
}

$(myBookingsBtn).on("click", myBookingsFilter);


/**
 * Datepicker widget
 * Long date format
 * Limit date range from today + 12 months
*/
$(document).ready(function() {
    $( "#datepicker" ).datepicker({ dateFormat: "MM d, yy", minDate: +0, maxDate: "+12M +0D", beforeShowDay: $.datepicker.noWeekends });
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


// remove d-none class to unfilter table data
const refreshBtn = document.getElementById("refresh-table");
const removeFilter = (e) => {
    let resultRows = document.querySelectorAll(".booking-row");
    resultRows.forEach(row => {
        row.classList.remove("d-none");
        });
}

$(refreshBtn).on("click", removeFilter);
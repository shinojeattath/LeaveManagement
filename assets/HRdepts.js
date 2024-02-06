function showDepartment(department) {
    // Hide buttons container
    document.querySelector('.buttons-container').style.transform = 'translateX(-100%)';

    // Show left side scrollable bar
    document.querySelector('.scrollable-bar').style.display = 'block';

    // Show staff list for the selected department
    var staffList = document.getElementById('staff-list');
    staffList.style.display = 'block';

    // Dummy staff list for demonstration

    ////////////////////////////////////

    const departmentData = leaveApplicationData.filter(item => item.fields.department === department);
    console.log('################################################');
    console.log(departmentData);
    // Show staff list for the selected department
    var staffList = document.getElementById('staff-list');
    staffList.style.display = 'block';

    var staffListHtml = '<ul>';
    departmentData.forEach(function (staff) {
        staffListHtml += '<li onclick="navigateToStaffPage(\'' + staff.fields.name + '\')">' + staff.fields.name + '</li>';
    });
    staffListHtml += '</ul>';

    staffList.innerHTML = staffListHtml;


    ////////////////////////////////////
    var staffData = getStaffListByDepartment(department);
    var staffListHtml = '<ul>';
    staffData.forEach(function (staff) {
        staffListHtml += '<li onclick="navigateToStaffPage(\'' + staff + '\')">' + staff + '</li>';
    });
    staffListHtml += '</ul>';

    staffList.innerHTML = staffListHtml;
}

function navigateToStaffPage(staffName) {
    // Redirect to another page or perform any other action when a staff is selected
    console.log('Selected Staff:', staffName);
}


function fetchDataFromDjango() {
    fetch('/hr/get_data/')
        .then(response => response.json())
        .then(data => {
            
            leaveApplicationData = data.data;
            console.log('Data received from Django:', leaveApplicationData);
            console.log('________________________________________');

            // Your logic to handle the received data goes here
            showDepartment('CSE');
        })
        .catch(error => {
            console.error('Fetch error:', error);
        });
}

fetchDataFromDjango();
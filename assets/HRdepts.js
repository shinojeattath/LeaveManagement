function showDepartment(department) {
    // Hide buttons container
    document.querySelector('.buttons-container').style.transform = 'translateX(-100%)';

    // Show left side scrollable bar
    document.querySelector('.scrollable-bar').style.display = 'block';

    // Show staff list for the selected department
    var staffList = document.getElementById('staff-list');
    staffList.style.display = 'block';

    // Dummy staff list for demonstration
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

// Dummy function to get staff list based on the selected department
function getStaffListByDepartment(department) {
    switch (department) {
        case 'Computer Science':
            return ['John Doe', 'Jane Smith', 'Alice Johnson'];
        case 'Civil':
            return ['Bob Williams', 'Eva Brown', 'Charlie Davis'];
        case 'Mechanical':
            return ['David Wilson', 'Sophie White', 'Frank Miller'];
        case 'Electrical':
            return ['Grace Taylor', 'Henry Moore', 'Ivy Green'];
        case 'Electronics':
            return ['Jack Harris', 'Kelly Clark', 'Leo Turner'];
        case 'ASH':
            return ['Mia Turner', 'Noah Hall', 'Olivia Scott'];
        default:
            return [];
    }
}

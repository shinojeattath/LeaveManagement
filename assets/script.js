var dataDictionary=JSON.parse('{{dataDictionary_json|safe}}');
    console.log(dataDictionary);


function toggleDetails(request) {
    const details = document.querySelector('.leave-details');
    const leaveName = request.querySelector('strong').innerText;
    const leaveReason = request.querySelector('p:nth-child(2)').innerText;
    const leaveType = request.querySelector('p:nth-child(3)').innerText;

    details.innerHTML = `
        <p><strong>Name:</strong> ${leaveName}</p>
        <p><strong>Branch:</strong> XYZ Branch</p>
        <p><strong>Designation:</strong> Manager</p>
        <p><strong>Reason for Leave:</strong> ${leaveReason.slice(8)}</p>
        <p><strong>Leave Type:</strong> ${leaveType.slice(6)}</p>
        <p><strong>Time of Request:</strong> 2023-10-15 10:30 AM</p>
        <button class="approve-btn" onclick="approveRequest()">Approve</button>
        <button class="reject-btn" onclick="rejectRequest()">Reject</button>
    `;

    details.style.display = 'block';
}

function approveRequest() {
    alert('Request Approved');
}

function rejectRequest() {
    alert('Request Rejected');
}

function logout() {
    alert('Logout');
    // Implement your logout logic here
}

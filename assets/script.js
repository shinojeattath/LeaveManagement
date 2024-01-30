var dataDictionary=JSON.parse('{{dataDictionary_json|safe}}');
    console.log(dataDictionary);


function toggleDetails(request) {
    const details = document.querySelector('.leave-details');
    const leaveName = request.querySelector('strong').innerText;
    const leaveReason = request.querySelector('p:nth-child(2)').innerText;
    const leaveType = request.querySelector('p:nth-child(3)').innerText;
    const Branch = request.querySelector('p:nth-child(4)').innerText;
    const Designation = request.querySelector('p:nth-child(5)').innerText;
    const TimeOfRequst = request.querySelector('p:nth-child(6)').innerText;


    details.innerHTML = `
        <p><strong>Name:</strong> ${leaveName}</p>
        <p><strong>Branch:</strong>${Branch}</p>
        <p><strong>Designation:</strong>${Designation}</p>
        <p><strong>Reason for Leave:</strong> ${leaveReason}</p>
        <p><strong>Leave Type:</strong> ${leaveType.slice(6)}</p>
        <p><strong>Time of Request:</strong>${TimeOfRequst}</p>
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

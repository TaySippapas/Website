document.getElementById('loginForm').addEventListener('submit', async function(event) {
    event.preventDefault();
    const EmailOrUsername = document.getElementById('EmailOrUsername').value;
    const password = document.getElementById('password').value;
    try {
        const response = await fetch('/login', {
            method: 'POST',
            headers: 
            {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                EmailOrUsername: EmailOrUsername,
                password: password
            })
        });

        const data = await response.json();
        // Handle the response
        if (data.success) 
            {
            alert('Login successful!');
            // Redirect to the dashboard or home page
            window.location.href = '/'; // Adjust the path as needed
        } 
        else 
        {
            alert('Error: ' + data.error);
        }
    } 
    catch (error) 
    {
        console.error('Error:', error);
        alert('An unexpected error occurred.');
    }
});
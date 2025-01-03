document.getElementById('signupForm').addEventListener('submit', async function(event) {
    event.preventDefault();
    const email = document.getElementById('email').value;
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;
    const response = await fetch('/signup',{
        method:'POST',
        headers:
        {
             'Content-Type': 'application/json'
        },
        body: JSON.stringify
        ({
            gmail: email,
            username: username,
            password: password
        })
    });
    const data=await response.json();
    if (data.success)
    {
        alert('Account created successfully!');
        window.location.href='/'
    }
    else
    {
        alert('Error: ' + data.error);
    }
});
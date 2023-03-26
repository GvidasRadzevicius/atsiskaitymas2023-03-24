const form = document.querySelector('.login-form');
const message = document.querySelector('.message');

form.addEventListener('submit', function(event) {
  event.preventDefault();
  const username = form.querySelector('input[type="text"]').value;
  const password = form.querySelector('input[type="password"]').value;
  
  if (username === 'admin' && password === 'password') {
    
    window.location.href = '/home';
  } else {
   
    message.textContent = 'Invalid username or password';
    message.style.color = 'red';
  }
});

username = document.getElementById('user_name');
email = document.getElementById('email');
is_superuser = document.getElementById('is_superuser');

fetch('/home/usuario/json_response/')
  .then(response => response.text())
  .then(data => {
    const jsonData = JSON.parse(data);

    if (jsonData.username && jsonData.email) {
        username.innerText = `${jsonData.username}`;
        email.innerText = `${jsonData.email}`;
    } else {
        console.log('Usuario não localizado')
    }
  })
  .catch(error => {
    console.error('Erro ao buscar dados:', error);
  });



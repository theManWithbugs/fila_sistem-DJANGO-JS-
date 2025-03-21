function validarDados() {
    var username = document.getElementById('username').value;
    var senha = document.getElementById('senha').value;
    var alerta = document.getElementById('msg_alerta')
    var botao_enviar = document.getElementById('btn_enviar')

    function showAlert(message) {
        alerta.style = 'display: block';
        var span = alerta.querySelector('span.me-1');
        span.innerHTML = message;

        setTimeout(function() {
            alerta.style = 'display: none';
        }, 4000)};

    console.log(`Nome de usúario: ${username}\nSenha: ${senha}`)

    if (username && senha) {
        if(senha.length >= 8) {
            if (username.includes('.')) {
                botao_enviar.type = 'submit'
            } else {
                showAlert('Error: username deve conter "." ')
            }
        } else {
            showAlert('Error: A senha deve ter mais de 8 caracteres!')
        }
    } else {
        showAlert('Error: Ambos os campos devem ser preenchidos!')
    }
    return username, senha
}



function showPage(pageId) {
    document.querySelectorAll('.page').forEach(page => {
        page.classList.add('hidden');
    });
    document.getElementById(pageId).classList.remove('hidden');
}

function armazenar_valor() {
    let valor = document.getElementById('password').value;

    document.getElementById('password_confirm').value = valor;

    return valor
}

// Esse é o comando para chamar a função que realiza a ação de passar o valor
// É definido o id de destino na função, deve ser alterado de acordo com a pagina destino
document.getElementById('password').addEventListener('input', armazenar_valor);

password = document.getElementById('password').value
password_confirm = document.getElementById('password_confirm').value

function check_password(password, password_confirm) {

    password = document.getElementById('password').value
    password_confirm = document.getElementById('password_confirm').value

    const regex = /[A-Z]/; 
    if (password == password_confirm) {
        if (regex.test(password)) {
            console.log('Registrado com sucesso!')
        }
        else {
            console.log('A senha deve conter ao menos uma letra maiscula!')
        }
    }
    else {
        console.log('Ambas as senhas devem ser iguais!');
    }
}
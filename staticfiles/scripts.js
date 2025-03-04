document.getElementById('form-contato').addEventListener('submit', function (event) {
    event.preventDefault(); // Impede o envio do formulário

    // Validação do nome
    const nome = document.getElementById('nome').value.trim();
    if (nome === '') {
        alert('Por favor, insira seu nome.');
        return;
    }

    // Validação do e-mail
    const email = document.getElementById('email').value.trim();
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailRegex.test(email)) {
        alert('Por favor, insira um e-mail válido.');
        return;
    }

    // Validação do assunto
    const assunto = document.getElementById('assunto').value.trim();
    if (assunto === '') {
        alert('Por favor, insira um assunto.');
        return;
    }

    // Validação da mensagem
    const mensagem = document.getElementById('mensagem').value.trim();
    if (mensagem === '') {
        alert('Por favor, insira uma mensagem.');
        return;
    }

    // Se tudo estiver válido, envie o formulário
    this.submit();
});
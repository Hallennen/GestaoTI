
function AlterarSenha(){
    var senha1 = document.getElementById('password1').value;
    let senha2 = document.getElementById('password2').value;

    if((senha1 != senha2) || (senha1 === '')){
        document.getElementById("password1").style.borderColor="#f00";
        document.getElementById("password2").style.borderColor="#f00";
        document.getElementById('salvar').style.display='none';
        document.getElementById('helpSenha').style.display='block';

    }
    else{
        document.getElementById("password1").style.borderColor="green";
        document.getElementById("password2").style.borderColor="green";
        document.getElementById('salvar').style.display='block';
        document.getElementById('helpSenha').style.display='none';

    }
}

function ConfirmarAlteracao(){
    alert('Será necessario que faça login novamente com a nova senha, para continuar a navegar no sistema.')
}
    
    

document.addEventListener('DOMContentLoaded',function(){
    const folgas_status = document.getElementById('linha_status_folga');

    function adicionar_classe(folgas) {
        let teste = document.querySelectorAll('#linha_status_folga')
        console.log(teste)

        for(var i = 0, index=0; i < teste.length; i++,index++){
            let div_folga = document.querySelectorAll('#linha_status_folga')[index];

            if(div_folga.textContent === 'APROVADO'){
                div_folga.classList.add('aprovado')
            }
            if(div_folga.textContent === 'RECUSADO'){
                div_folga.classList.add('recusado')
            }
        }   
    }
    adicionar_classe(folgas_status)
})



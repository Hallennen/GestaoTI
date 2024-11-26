document.addEventListener('DOMContentLoaded',function() {
    const monthBR= ['janeiro','fevereiro','março','abril','maio','junho','julho','agosto','setembro','outubro','novembro','dezembro'];
    const tableDays = document.getElementById('dias');
    function GetDaysCalendar(mes, ano) {
        document.getElementById('mes').innerHTML = monthBR[mes];
        document.getElementById('ano').innerHTML = ano;

        let firstDayOfWeek = new Date(ano,mes,1).getDay()-1;
        let getLastDayThisMonth = new Date(ano,mes+1,0).getDate();
        var teste_dados = document.getElementById('dados');
        console.log(teste_dados)
    //     if (teste_dados){

            
    //         var teste = document.getElementById('dados').textContent.split(',')[1];
    //         var dia_informado = (parseInt(teste.split('-'))[2]);
    //         var mes_informado = (parseInt(teste.split('-'))[1]);
    //         var ano_informado = (ParseInt(teste.split('-'))[0]);
    //     }


    //    var datas_folga = document.querySelectorAll('#dados');


        for (var i = -firstDayOfWeek ,index=0; i < (42-firstDayOfWeek); i++ , index++){
            let dt = new Date(ano, mes, i);
            let dtNow = new Date();
            let dayTable = tableDays.getElementsByTagName('td')[index];


            dayTable.classList.remove('dia-atual');
            dayTable.classList.remove('mes-anterior');
            dayTable.classList.remove('proximo-mes');
            dayTable.classList.remove('event');

            dayTable.innerHTML = dt.getDate();
            
         
            if (dt.getFullYear() == dtNow.getFullYear() && dt.getMonth() == dtNow.getMonth() && dt.getDate() == dtNow.getDate()){
                dayTable.classList.add('dia-atual')
                dayTable.classList.add('event')

            }

            if (i < 1){
                dayTable.classList.add('mes-anterior')
            }


            if (i > getLastDayThisMonth){
                dayTable.classList.add('proximo-mes')
            }
            
            // if (dt.getFullYear() == ano_informado && dt.getMonth()+1 == mes_informado && dt.getDate() == dia_informado){
            //     alert('sim');
            //     console.log('true');
            //     dayTable.classList.add('event')
            // }

        }

        
        // if(datas_folga.length > 0){
            
        //     for (i = 0 ; i <=datas_folga.length; i++){
        //         folga = document.querySelectorAll('#dados')[i].textContent;
        //         console.log(folga)
        //         var dia_informado = (folga.split('-'))[2];
        //         var mes_informado = (folga.split('-'))[1];
        //         var ano_informado = (folga.split('-'))[0];
        //         data.getFullYear() == ano_informado && data.getMonth()+1 == mes_informado && data.getDate() == dia_informado

        //         console.log('true');
        //         dayTable.classList.add('event')
        //     }
        // }

      

    }

    
    
    let now = new Date();
    let mes = now.getMonth();
    let ano = now.getFullYear();

    GetDaysCalendar(mes, ano);


    const botao_anterior = document.getElementById('btn_prev');
    const botao_proximo = document.getElementById('btn_next');

    
    botao_proximo.onclick = function(){
        mes ++;
        if(mes > 11){
            mes = 0 ;
            ano++;
            
        }
        GetDaysCalendar(mes, ano)
    }
    
    botao_anterior.onclick = function(){
        mes--;
        if(mes < 0){
            mes = 11 ;
            ano--;

        }
        GetDaysCalendar(mes, ano)
    }

})

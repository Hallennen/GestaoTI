# GestaoTI
SISTEMA DE AGENDAMENTO DE FOLGAS DO DEPARTAMENTO DE T.I

# Motivação
Esta projeto surgiu através do problema que tinhamos em nossa equipe de T.I; a GESTÃO DE FOLGAS da equipe é um desafio comum enfrentado por muitas empresas, especialmente aquelas com equipes grandes. A falta de uma abordagem estruturada para controlar e planejar as folgas pode levar a problemas como sobrecarga de trabalho, falta de pessoal em momentos críticos e etc...

# Como Rodar o Projeto Localmente (Windows)
 - CLONE/FORK o repositório;
 - Com o repositorio clonado, e dentro da pasta raiz do arquivo rode os comandos;
   
 - Crie o ambiente virtual
```
   python -m venv venv
```
 - Ative o ambiente virtual
```
   .\venv\scripts\activate
```
 - Instale as dependencias
```
   pip install -r requeriments.txt 
```

 - Configure o Banco de Dados de sua preferencia no arquivo "app.settings.py"
Ex: PostgreSQL
   
   ![image](https://github.com/user-attachments/assets/6b66f60a-ef31-4bc5-9a66-f3301a0a8daf)

 - Crie um database 'gestaoti' no seu banco
```
   CREATE DATABASE gestaoti 
```


 - Popule o banco de dados com as tabelas necessarias:
```
   python manage.py migrate 
```

 - Crie um superusuario
 ```
    python manage.py createsuperuser
 ```

 - Rode o servidor local 
 ```
    python manage.py runserver
 ```

 - Abra o navegador no link
```
   127.0.0.1:8000/login   
```
   ou
```
   localhost:8000/login
```


# Stacks  Utilizadas
Backend: Python (Framework Django), PostgreSQL
Frontend: HTML, CSS

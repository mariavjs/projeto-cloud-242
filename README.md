# Projeto-Cloud-242

**Feito por: Maria Vitória Sartori**

# Parte 1 - Dockerinzing

## Explicação do Projeto
Este projeto foi desenvolvido para criar uma aplicação web integrada, uma API RESTful, com FastAPI e PostgreSQL. Ele utiliza **Docker** para containerização e apresenta funcionalidades tais como:

- **Cadastro de Usuários**: Criação e armazenamento seguro de informações no banco de dados.
- **Login de Usuários**: Permite que os usuários façam login com suas credenciais e recebam um token JWT para acessar a API.
- **Autenticação JWT**: Emissão de tokens para autenticação segura.
- **Consulta de API Externa**: Integração com uma API que retorna curiosidades aleatórias sobre marcos mundiais.
- **Scraping**: Utiliza uma API pública para buscar e exibir curiosidades sobre lugares históricos e culturais.

## Como Executar a Aplicação

### 1. Clonar o Repositório
```bash
git clone https://github.com/mariavjs/projeto-cloud-242.git
cd projeto-cloud-242
```

### 2. Configurar Variáveis de Ambiente (env)
Adicione um arquivo `.env` na raiz do projeto com o seguinte conteúdo:
```env
POSTGRES_USER=cloud
POSTGRES_PASSWORD=cloud
POSTGRES_DB=usuarios
POSTGRES_HOST=db
POSTGRES_PORT=5432
SECRET_KEY=secret
```

### 3. Subir os Contêineres com Docker Compose
Execute:
```bash
docker-compose up --build
```

### 4. Acessar a Documentação da API
Acessar:
[http://localhost:8000/docs](http://localhost:8000/docs)

---

## Documentação dos Endpoints

![Endpoints](imgs\endpoints.png)

### **POST /registrar**
Registra um novo usuário no banco de dados.

![Register](imgs\register.png)


### **POST /login**
Autentica um usuário e retorna um token JWT.

![Login](imgs\login.png)

### **GET /consulta**
Consulta uma curiosidade aleatória sobre marcos mundiais, através da autenticação do token JWT

![Consultar](imgs\consultar.png)


## Vídeo de execução da aplicação:

https://youtu.be/tQ5MqUDKZtA 

## Link para docker hub do projeto:

dockerhub: https://hub.docker.com/r/mariavjs/projeto-cloud-242 

# Parte 2 - AWS

A aplicação foi implantada no **AWS Elastic Kubernetes Service (EKS)**, garantindo escalabilidade e gestão eficiente de contêineres. A implantação incluiu:  
- Configuração de um **cluster** no **EKS**.  
- Deploy de dois Pods no Kubernetes:  
  - Um para a aplicação.  
  - Outro para o banco de dados **PostgreSQL**.  

### Reproduzir o Deploy na AWS  

1. **Configuração do Cluster EKS**  
   ```bash  
   eksctl create cluster --name projeto-cloud --region us-east-1 --nodegroup-name nodegroup --nodes 2 --nodes-min 1 --nodes-max 3 --managed  
   ```  

2. **Criação dos Arquivos de Configuração do Kubernetes**  
   Os principais arquivos incluem:  
   - **Deployment.yml**: Define os Pods e seus recursos.  
   - **Postgres-Deployment.yml**: Gerencia um Deployment para o banco de dados
   - **Service.yml**: Configura o serviço para expor a aplicação.  

***Exemplo de Arquivo .yml***

   - [postgres-deployment.yml](postgres-deployment.yml)
   - [deployment.yml](deployment.yml)
   - [service.yml](service.yml)

3. **Aplicação dos Arquivos no Cluster**  
   Para aplicar os arquivos, utilize o comando:  
   ```bash  
   kubectl apply -f deployment.yml  
   kubectl apply -f service.yml  
   kubectl apply -f postgres-deployment.yml  
   ```  

4. **Verificação dos Pods e Serviços**  
   Confirmação de execução dos PODs:  
   ```bash  
   kubectl get pods  
   ```  
   ![pods](imgs\pods.png)

   Verificação dos serviços:  
   ```bash  
   kubectl get svc  
   ```  
    ![services](imgs\services.png)

5. **Aplicação**

A aplicação está acessível publicamente na seguinte URL:

http://a2106d20f94614475ac81799589167c3-2084239673.us-west-2.elb.amazonaws.com

## Vídeo de execução da aplicação:

https://youtu.be/fwArwSr6miU


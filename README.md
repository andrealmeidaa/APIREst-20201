# APIRest-20201
Código para o projeto final da disciplina de Programação para Ambientes de Redes
## Configurando o ambiente
1. Realize o fork do projeto inicialmente
2. Instalar a biblioteca  MySQL-python e os arquivos para desenvolvimento do MySQL através do comando
```
sudo yum install MySQL-python mysql-devel
```
3. Para configurar o ambiente de desenvolvimento proceda com a instalação dos pacotes Python constantes no arquivo requeriments.txt, executando o comando a seguir
```
sudo pip3 install -r requirements.txt
```
4. Criar a instância do banco de dados e configurar o acesso através do grupo de segurança, conforme demonstrado na videoaula

> Apesar de estarmos instalando com sudo pip3, em ambientes de desenvolvimento e até de produção, o mais adequado é utilizar um ambiente virtual do Python, o virtualenv. Para saber mais clique [aqui](https://www.treinaweb.com.br/blog/criando-ambientes-virtuais-para-projetos-python-com-o-virtualenv/ "VirtualEnv - TreinaWeb").

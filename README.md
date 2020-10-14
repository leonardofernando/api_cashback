###Desafio – “Eu revendedor ‘O Boticário’ quero ter benefícios de acordo com o meu volume de vendas”.

#####1. PROBLEMA/OPORTUNIDADE
O Boticário tem várias soluções para ajudar seus revendedores(as) a gerir suas finanças e
alavancar suas vendas. Também existem iniciativas para impulsionar as operações de vendas
como metas gameficadas e desconto em grandes quantidades de compras.

Agora queremos criar mais uma solução, e é aí que você entra com seu talento ;)

A oportunidade proposta é criar um sistema de Cashback, onde o valor será disponibilizado
como crédito para a próxima compra da revendedora no Boticário;

Cashback quer dizer “dinheiro de volta”, e funciona de forma simples: o revendedor faz uma
compra e seu benefício vem com a devolução de parte do dinheiro gasto no mês seguinte.

Sendo assim o Boticário quer disponibilizar um sistema para seus revendedores(as)
cadastrarem suas compras e acompanhar o retorno de cashback de cada um.

Vamos lá?

##BACK-END
###Requisitos back-end:

- Rota para cadastrar um novo revendedor(a) exigindo no mínimo nome completo, CPF,
e- mail e senha;
- Rota para validar um login de um revendedor(a);
- Rota para cadastrar uma nova compra exigindo no mínimo código, valor, data e CPF do
revendedor(a). Todos os cadastros são salvos com o status “Em validação” exceto
quando o CPF do revendedor(a) for 153.509.460-56, neste caso o status é salvo como
“Aprovado”;
- Rota para listar as compras cadastradas retornando código, valor, data, % de cashback
aplicado para esta compra, valor de cashback para esta compra e status;
- Rota para exibir o acumulado de cashback até o momento, essa rota irá consumir essa
informação de uma API externa disponibilizada pelo Boticário.

##Rotas:
[Rotas/Exemplos no Postman](BoticarioApi.postman_collection.json) - arquivo de rotas para importação

## Endpoints/Exemplos:

####/healthcheck

Rota para verificar saúde da api.

######Métodos: GET
######Headers/Authorization: Não
######Retorno: JSON
        {
            "status": "OK",
        }

---

####/revendedor/cadastrar

Rota para realizar cadastro de novo revendedor.

######Métodos: POST
        {
            "nome": "Leonardo Venancio",
            "cpf": "123.456.789-52",
            "email": "leonardo@teste.com",
            "senha": "senha123",
        }
######Headers/Authorization: Não
######Retorno: JSON
        {
            "mensagem": "O revendedor foi inserido com sucesso!",
        }

---

####/revendedor/login

Rota para realizar login de um revendedor cadastrado.

######Métodos: POST
        {
            "cpf": "123.456.789-52",
            "senha": "senha123",
        }
######Headers/Authorization: Não
######Retorno: JSON
        {
            "mensagem": "O revendedor foi logado com sucesso!",
            "token": <token jwt>,
        }

---

####/compras/cadastrar

Rota para realizar cadastro de compras realizadas.

######Métodos: POST
        {
            "codigo": 254513,
            "valor": 1253,
            "data": "09/10/2020",
            "cpf": "123.456.789-52",
        }
######Headers/Authorization: Sim
        {
            "authorization": <token jwt>
        }
######Retorno: JSON
        {
            "mensagem": "O revendedor foi logado com sucesso!",
            "token": <token jwt>,
        }

---

####/compras/listar

Rota para visualizar lista de compras cadastradas.

######Métodos: GET
######Headers/Authorization: Sim
        {
            "authorization": <token jwt>
        }
######Retorno: JSON
        {   
            compras: [
                {
                    "mensagem": "O revendedor foi logado com sucesso!",
                    "token": <token jwt>,
                },
            ],
        }

---

####/compras/listar

Rota para visualizar quantidade de cashback acumulado.

######Métodos: GET
######Headers/Authorization: Não
######Retorno: JSON
        {   
            "credito_cashback": <valor do cashback>,
        }

---

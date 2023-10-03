#Exercícios Banco de Dados - semana 3 
#pesquisas: 
#https://www.sqlite.org/lang_createtable.html
#https://docs.python.org/3/library/sqlite3.html#sqlite3.Cursor.execute
#https://pt.stackoverflow.com/questions/245530/como-contar-o-numero-de-rows-em-uma-tabela-em-python

#importando sqlite3 e conectando e criando meu db
import sqlite3
connection = sqlite3.connect("my_database")
cur = connection.cursor()

#1. Crie uma tabela chamada "alunos" com os seguintes campos: id(inteiro | INTEGER), nome (texto|VARCHAR), idade (inteiro) e curso (texto).

cur.execute("CREATE TABLE IF NOT EXISTS alunos (id INTEGER , nome VARCHAR(250), idade INTEGER, curso VARCHAR (250));")

#2. Insira pelo menos 5 registros de alunos na tabela que você criou no exercício anterior.

#cur.execute("INSERT INTO alunos (id,nome,idade, curso) "
#              "VALUES (1,'Cesar',42,'TI')")
# cur.execute("INSERT INTO alunos (id,nome,idade, curso) "
#              "VALUES (2,'Jujuba',38,'Vet')")
# cur.execute("INSERT INTO alunos (id,nome,idade, curso) "
#              "VALUES (3,'Clair',13,'Meca')")
# cur.execute("INSERT INTO alunos (id,nome,idade, curso) "
#              "VALUES (4,'Mary',12,'Desing')")
# cur.execute("INSERT INTO alunos (id,nome,idade, curso) "
#               "VALUES (5,'Mel',8,'Arte')")
# cur.execute("INSERT INTO alunos (id,nome,idade, curso) "
#                "VALUES (6,'Ero',60,'Historia')")
# cur.execute("INSERT INTO alunos (id,nome,idade, curso) "
#                "VALUES (7,'Alci',61,'Biologia')")
# cur.execute("INSERT INTO alunos (id,nome,idade, curso) "
#                "VALUES (8,'Lau',38,'Linguagens')")
# cur.execute("INSERT INTO alunos (id,nome,idade, curso) "
#                "VALUES (9,'Fabricio',43,'Engenharia')")
#cur.execute("INSERT INTO alunos (id,nome,idade, curso) "
#                "VALUES (10,'Anna',19,'Engenharia')")
#cur.execute("INSERT INTO alunos (id,nome,idade, curso) "
#                "VALUES (11,'Gab',18,'Engenharia')")

# # definindo dados para testar no python 
# res = cur.execute(ACAO + FROM + alunos + detalhes)
# for alunos in res:
#     print(alunos)

# 3. Consultas Básicas
# Escreva consultas SQL para realizar as seguintes tarefas:
# a) Selecionar todos os registros da tabela "alunos".
print("\n"'Os registros da tabela alunos são:'"\n")
res = cur.execute("SELECT * FROM alunos")
for alunos in res:
    print(alunos)

# b) Selecionar o nome e a idade dos alunos com mais de 20 anos.
print("\n"'Os alunos com mais de 20 anos são:'"\n")
res = cur.execute("SELECT nome, idade FROM alunos WHERE idade>20")
for alunos in res:
    print(alunos)
  
#c) Selecionar os alunos do curso de "Engenharia" em ordem alfabética  - usar GROUP BY e, para agregar info especifica, usa o HAVING após o GROUP BY.
print("\n"'Os alunos que cursam engenharia, em ordem alfabética, são:'"\n")
res = cur.execute("SELECT nome, curso FROM alunos GROUP BY nome HAVING curso = 'Engenharia'")
for alunos in res:
    print(alunos)

#d) Contar o número total de alunos na tabela
cur.execute("SELECT count(1) FROM alunos")
count = list(cur)[0]
print("\n" "A quantidade de alunos na tabela é: %d" %(count))


# 4. Atualização e Remoção UPDATE
# a) Atualize a idade de um aluno específico na tabela.
print("\n"'A idade correta da Mel é:'"\n")
cur.execute("UPDATE alunos SET idade= 7 WHERE id=5")
res = cur.execute("SELECT id,nome,idade FROM alunos WHERE id=5")
for alunos in res:
    print(alunos)

#b) Remova um aluno pelo seu ID.
#print("\n"'A idade correta do :'"\n")
cur.execute("DELETE FROM alunos WHERE id=11")
print("\n"'Tabela atualizada. Agora os registros da tabela alunos são:'"\n")
res = cur.execute("SELECT * FROM alunos")
for alunos in res:
    print(alunos)

#5. Criar uma Tabela e Inserir Dados
#Crie uma tabela chamada "clientes" com os campos: id (chave primária), nome (texto), idade (inteiro) e saldo (float). 

# cur.execute ("CREATE TABLE IF NOT EXISTS clientes (id INTEGER primary key, nome VARCHAR(250),idade INTEGER, saldo FLOAT);")

# #Insira alguns registros de clientes na tabela.
# cur.execute("INSERT INTO clientes (id,nome,idade, saldo)"
#               "VALUES (1,'Cesar',24, 1000)")
# cur.execute("INSERT INTO clientes (id,nome,idade, saldo)"
#               "VALUES (2,'Jujuba',38,3000)")
# cur.execute("INSERT INTO clientes (id,nome,idade, saldo)"
#               "VALUES (3,'Clair',13, 1000)")
# cur.execute("INSERT INTO clientes (id,nome,idade, saldo)"
#               "VALUES (4,'Mary',12,5000)")
# cur.execute("INSERT INTO clientes (id,nome,idade, saldo)"
#                "VALUES (5,'Mel',8,500)")
# cur.execute("INSERT INTO clientes (id,nome,idade, saldo)"
#                 "VALUES (6,'Ero',60, 7000)")
# cur.execute("INSERT INTO clientes (id,nome,idade, saldo)"
#                 "VALUES (7,'Alci',61,7000)")
# cur.execute("INSERT INTO clientes (id,nome,idade, saldo)"
#                 "VALUES (8,'Lau',38,8000)")
# cur.execute("INSERT INTO clientes (id,nome,idade, saldo)"
#                 "VALUES (9,'Fabricio',43,900)")
# cur.execute("INSERT INTO clientes (id,nome,idade, saldo)"
#                 "VALUES (10,'Anna',19,700)")
#testando a tabela
print("\n"'Os registros da tabela clientes são:'"\n")
res = cur.execute("SELECT * FROM clientes")
for clientes in res:
    print(clientes)

#6. Consultas e Funções Agregadas
#materiais pesquisados: https://www.devmedia.com.br/sql-max-min-avg-sum-e-count/41218

#Escreva consultas SQL para realizar as seguintes tarefas:
#a) Selecione o nome e a idade dos clientes com idade superior a 30 anos.
print("\n"'Os clientes com mais de 30 anos:'"\n")
res = cur.execute("SELECT nome, idade FROM clientes WHERE idade>30")
for clientes in res:
    print(clientes)

#b) Calcule o saldo médio dos clientes.
print("\n"'O saldo médio dos clientes é:'"\n")
res = cur.execute("SELECT AVG (saldo) as SALDO_MEDIO FROM clientes")
for clientes in res:
    print(clientes)

#c) Encontre o cliente com o saldo máximo.
print("\n"'O cliente com saldo maior de todos é:'"\n")
res = cur.execute("SELECT C.nome as Rico, MAX(saldo) as MAIOR_SALDO FROM clientes C ")
for clientes in res:
    print(clientes)

#d) Conte quantos clientes têm saldo acima de 1000.
cur.execute("SELECT count(1) FROM clientes WHERE saldo >1000")
count = list(cur)[0]
print("\n" "A quantidade de clientes com saldo acima de 1000 é: %d" %(count))

print("\n"'Os clientes com saldo acima de mil são:'"\n")
res = cur.execute("SELECT nome, saldo FROM clientes WHERE saldo >1000")
for clientes in res:
    print(clientes)


#7. Atualização e Remoção com Condições
#a) Atualize o saldo de um cliente específico.
print("\n"'O novo saldo da Ana é:'"\n")
res = cur.execute("UPDATE clientes SET saldo=1300 WHERE id=10")
res = cur.execute("SELECT nome,saldo FROM clientes WHERE id=10")
for clientes in res:
    print(clientes)

#b) Remova um cliente pelo seu ID.
print("\n"'A lista atualizada de clientes excluindo o 9 é:'"\n")
res = cur.execute("DELETE FROM clientes WHERE id=9")
res = cur.execute("SELECT * FROM clientes")
for clientes in res:
    print(clientes)

#8. Junção de Tabelas
#material pesquisa: https://www.devmedia.com.br/sql-aprenda-a-utilizar-a-chave-primaria-e-a-chave-estrangeira/37636
#https://www.sqlite.org/foreignkeys.html
#https://www.javatpoint.com/sqlite-foreign-key

#Crie uma segunda tabela chamada "compras" com os campos: id(chave primária), cliente_id (chave estrangeira referenciando o id da tabela "clientes"), produto (texto) e valor (real). 
cur.execute ("CREATE TABLE IF NOT EXISTS compras (id INTEGER primary key, cliente_id INTEGER, produto VARCHAR(250), valor REAL, CONSTRAINT fk_clientes FOREIGN KEY (cliente_id) REFERENCES clientes (id));")

#Insira algumas compras associadas a clientes existentes na tabela "clientes".
# cur.execute("INSERT INTO compras (id, cliente_id, produto, valor)"
#                 "VALUES (1, 1, 'notebook', 7000.03)")
# cur.execute("INSERT INTO compras (id, cliente_id, produto, valor)"
#                 "VALUES (2, 1, 'mouse', 450.03)")
# cur.execute("INSERT INTO compras (id, cliente_id, produto, valor)"
#                  "VALUES (3, 2, 'caderno', 90.50)")
# cur.execute("INSERT INTO compras (id, cliente_id, produto, valor)"
#                  "VALUES (4, 2, 'caneta', 10.50)")
# cur.execute("INSERT INTO compras (id, cliente_id, produto, valor)"
#                  "VALUES (5, 3, 'kindle', 580.50)")

print("\n"'A nova tabela, compras, é:'"\n")
res = cur.execute("SELECT * FROM compras")
for compras in res:
    print(compras)

#Escreva uma consulta para exibir o nome do cliente, o produto e o valor de cada compra.
print("\n"'Os clientes e suas compras:'"\n")
res = cur.execute("SELECT c.nome, co.produto, co.valor FROM compras as co inner join clientes as c on c.id = co.cliente_id")
for item in res:
    print(item)

#Commit changes
connection.commit()

#Close the connection
connection.close()
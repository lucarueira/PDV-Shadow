--criando banco de dados

CREATE DATABASE cadastro_produtos
--Criando uma tabela

CREATE TABLE produtos (
    id INT NOT NULL AUTO_INCREMENT,
    codigo INT,
    descricao VARCHAR(50),
    codigodebarras VARCHAR(50),
    preco DOUBLE,
    ncm VARCHAR(8),
    categoria VARCHAR(20),
    PRIMARY KEY (id)
);

-- usar banco de dados 
use cadastro_produtos;
--mostrar tabelas do banco
show tables;
--visualisar estrutura da tabela
describe produtos;
--selecionar toda a tabela produtos
select * from produtos;
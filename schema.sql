drop table if exists dicas;

create table dicas(
	id integer primary key autoincrement,
	criacao timestamp not null default current_timestamp,
	titulo text not null,
	conteudo1 text not null,
	conteudo2 text,
	conteudo3 text,
	conteudo4 text,
	conteudo5 text,
	conteudo6 text,
	conteudo7 text,
	conteudo8 text,
	conteudo9 text,
	conteudo10 text,
	conteudo11 text,
	conteudo12 text,
	conteudo13 text,
	conteudo14 text,
	conteudo15 text,
	conteudo16 text,
	conteudo17 text,
	conteudo18 text,
	conteudo19 text,
	conteudo20 text,
	fonte text,
	fontelink text
);
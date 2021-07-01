use master
go

use abcdasd
go

if object_id('dbo.book', 'u') is not null
drop table dbo.book
go

create table dbo.book
(
	id int not null,
	name nvarchar(50) not null,
	author_amount int not null check(author_amount >= 0),
	first_author int not null,
	second_author int,
	third_author int,
	fourth_author int,
	extra_info nvarchar(75),
	publisher_id int not null,
	year int not null,
	pages int not null
)

if object_id('dbo.regulatory_doc', 'u') is not null
drop table dbo.regulatory_doc
go

create table dbo.regulatory_doc
(
	id int not null,
	name nvarchar(150) not null,
	first_author int not null,
	extra_info nvarchar(75),
	publisher_id int not null,
	year int not null,
	journal_num int,
	first_page int,
	last_page int
)

if object_id('dbo.regulatory_tech_doc', 'u') is not null
drop table dbo.regulatory_tech_doc
go

create table dbo.regulatory_tech_doc
(
	id int not null,
	name nvarchar(50) not null,
	first_author int not null,
	extra_info nvarchar(75),
	date date not null,
	publisher_id int not null,
	year int not null,
	pages int not null
)

if object_id('dbo.patent', 'u') is not null
drop table dbo.patent
go

create table dbo.patent
(
	id int not null,
	name nvarchar(50) not null,
	author_amount int not null check(author_amount >= 1),
	first_author int not null,
	second_author int,
	third_author int,
	fourth_author int,
	publisher_id int not null,
	journal_num int,
	year int,
	pages int

)

if object_id('dbo.info_sheet', 'u') is not null
drop table dbo.info_sheet
go

create table dbo.info_sheet
(
	id int not null,
	name nvarchar(50) not null,
	author_amount int not null check(author_amount >= 1),
	first_author int not null,
	second_author int,
	third_author int,
	fourth_author int,
	publisher_id int not null,
	year int not null,
	pages int not null
)

if object_id('dbo.multi_volume', 'u') is not null
drop table dbo.multi_volume
go

create table dbo.multi_volume
(
	id int not null,
	name nvarchar(50) not null,
	author_amount int not null check(author_amount >= 0),
	first_author int not null,
	second_author int,
	third_author int,
	fourth_author int,
	extra_info nvarchar(75),
	publisher_id int not null,
	year int not null,
	amount_of_vols int not null
)

if object_id('dbo.not_published_yet', 'u') is not null
drop table dbo.not_published_yet
go

create table dbo.not_published_yet
(
	id int not null,
	name nvarchar(50) not null,
	author int not null,
	extra_info nvarchar(75),
	defend_date date not null,
	approval_date date not null,
	publisher_id int not null,
	year int not null
)

if object_id('dbo.elec_local', 'u') is not null
drop table dbo.elec_local
go

create table dbo.elec_local
(
	id int not null,
	name nvarchar(50) not null,
	author_amount int not null check(author_amount >= 0),
	first_author int not null,
	second_author int,
	third_author int,
	fourth_author int,
	extra_info nvarchar(75),
	type nvarchar(25),
	publisher_id int not null,
	year int not null,
	material_desc nvarchar(35)
)

if object_id('dbo.elec_internet', 'u') is not null
drop table dbo.elec_internet
go

create table dbo.elec_internet
(
	id int not null,
	name nvarchar(150) not null,
	author_amount int not null check(author_amount >= 0),
	first_author int not null,
	second_author int,
	third_author int,
	fourth_author int,
	extra_info nvarchar(75),
	publisher_id int,
	year int not null,
	url nvarchar(100),
	material_desc nvarchar(35)
)

if object_id('dbo.book_article', 'u') is not null
drop table dbo.book_article
go

create table dbo.book_article
(
	id int not null,
	name nvarchar(50) not null,
	author_amount int not null check(author_amount >= 0),
	first_author int not null,
	second_author int,
	third_author int,
	fourth_author int,
	extra_info nvarchar(75),
	book_id int not null,
	year int not null,
	page int not null
)

if object_id('dbo.newspaper_article', 'u') is not null
drop table dbo.newspaper_article
go

create table newspaper_article
(
	id int not null,
	name nvarchar(50) not null,
	author_amount int not null check(author_amount >= 0),
	first_author int not null,
	second_author int,
	third_author int,
	fourth_author int,
	extra_info nvarchar(75),
	newspaper_name nvarchar(25) not null,
	newspaper_year int not null, 
	newspaper_number int not null,
	year int not null,
	page int not null
)

if object_id('dbo.review', 'u') is not null
drop table dbo.review
go

create table review
(
	id int not null,
	name nvarchar(50) not null,
	author_amount int not null check(author_amount >= 0),
	first_author int not null,
	second_author int,
	third_author int,
	fourth_author int,
	extra_info nvarchar(75),
	journal_name nvarchar(25) not null,
	journal_year int not null, 
	journal_number int not null,
	year int not null,
	page int not null
)


if object_id('dbo.publisher', 'u') is not null
drop table dbo.publisher
go

create table dbo.publisher
(
	id int not null,
	name nvarchar(50) not null,
	place_of_ed nvarchar(50),
	extra_ed_info nvarchar(50)
)

if object_id('dbo.author', 'u') is not null
drop table dbo.author
go

create table dbo.author
(
	id int not null,
	name nvarchar(50) not null,
	stuff_id int not null
)


alter table dbo.book add 
	constraint pk_id1 primary key(id),
    constraint fk_name12 foreign key (first_author) references dbo.author(id) on delete cascade,
	constraint fk_name15 foreign key (second_author) references dbo.author(id),
	constraint fk_name13 foreign key (third_author) references dbo.author(id),
	constraint fk_name14 foreign key (fourth_author) references dbo.author(id),
	constraint fk_name1234 foreign key (publisher_id) references dbo.publisher(id)
go

alter table dbo.book_article add 
	constraint pk_id2 primary key(id),
	constraint fk_name2177 foreign key (first_author) references dbo.author(id),
	constraint fk_name2178 foreign key (second_author) references dbo.author(id),
	constraint fk_name2179 foreign key (third_author) references dbo.author(id),
	constraint fk_name2180 foreign key (fourth_author) references dbo.author(id),
	constraint fk_name2181 foreign key (id) references dbo.book(id)

go

alter table dbo.elec_internet add 
	constraint pk_id3 primary key(id),
	constraint fk_name177 foreign key (first_author) references dbo.author(id),
	constraint fk_name178 foreign key (second_author) references dbo.author(id),
	constraint fk_name179 foreign key (third_author) references dbo.author(id),
	constraint fk_name180 foreign key (fourth_author) references dbo.author(id),
	constraint fk_name124134 foreign key (publisher_id) references dbo.publisher(id)

go

alter table dbo.elec_local add 
	constraint pk_id4 primary key(id),
	constraint fk_name77 foreign key (first_author) references dbo.author(id),
	constraint fk_name78 foreign key (second_author) references dbo.author(id),
	constraint fk_name79 foreign key (third_author) references dbo.author(id),
	constraint fk_name80 foreign key (fourth_author) references dbo.author(id),
	constraint fk_name12123334 foreign key (publisher_id) references dbo.publisher(id)
go

alter table dbo.info_sheet add 
	constraint pk_id5 primary key(id),
	constraint fk_name16 foreign key (first_author) references dbo.author(id),
	constraint fk_name17 foreign key (second_author) references dbo.author(id),
	constraint fk_name18 foreign key (third_author) references dbo.author(id),
	constraint fk_name19 foreign key (fourth_author) references dbo.author(id),
	constraint fk_name1212334 foreign key (publisher_id) references dbo.publisher(id)
go

alter table dbo.multi_volume add 
	constraint pk_id7 primary key(id),
	constraint fk_name20 foreign key (first_author) references dbo.author(id),
	constraint fk_name21 foreign key (second_author) references dbo.author(id),
	constraint fk_name22 foreign key (third_author) references dbo.author(id),
	constraint fk_name23 foreign key (fourth_author) references dbo.author(id),
	constraint fk_name123224 foreign key (publisher_id) references dbo.publisher(id)
go

alter table dbo.newspaper_article add 
	constraint pk_id8 primary key(id),
	constraint fk_name241 foreign key (first_author) references dbo.author(id),
	constraint fk_name251 foreign key (second_author) references dbo.author(id),
	constraint fk_name261 foreign key (third_author) references dbo.author(id),
	constraint fk_name271 foreign key (fourth_author) references dbo.author(id)
go

alter table dbo.not_published_yet add 
	constraint pk_id9 primary key(id),
	constraint fk_name12234 foreign key (publisher_id) references dbo.publisher(id)
go

alter table dbo.patent add 
	constraint pk_id10 primary key(id),
	constraint fk_name24 foreign key (first_author) references dbo.author(id),
	constraint fk_name25 foreign key (second_author) references dbo.author(id),
	constraint fk_name26 foreign key (third_author) references dbo.author(id),
	constraint fk_name27 foreign key (fourth_author) references dbo.author(id),
	constraint fk_name15234 foreign key (publisher_id) references dbo.publisher(id)
go


alter table dbo.regulatory_doc add 
	constraint pk_id11 primary key(id),
	constraint fk_name152374 foreign key (publisher_id) references dbo.publisher(id)
go

alter table dbo.regulatory_tech_doc add 
	constraint pk_id12 primary key(id),
	constraint fk_name1523674 foreign key (publisher_id) references dbo.publisher(id)
go

alter table dbo.publisher add 
	constraint pk_id14 primary key(id)
go

alter table dbo.author add 
	constraint pk_id15 primary key(id)
go
create database if not exists mydataorgenizer character set = utf8mb4;

create table if not exists servr (
drID int auto_increment unique key primary key,
designation varchar(128),
location varchar(64),
Marke varchar(32),
ITid int);

alter table servr
add constraint it_mitarbeiterForeignKey foreign key (ITid) references it_mitarbeiter (ITid);

alter table servr
add ITid int;

create table if not exists it_mitarbeiter(
ITid int auto_increment unique key primary key,
last_name varchar(64),
first_name varchar(64),
address varchar(32),
birth_date date); 

create table if not exists programme(
pgID int auto_increment unique key primary key,
designation varchar(32),
developer varchar(64),
last_update date,
publication_date date);

create table if not exists ProgrammeSevr(
PgSrvID int auto_increment unique key primary key,
drID int,
pgID int,
constraint servrForeignKey foreign key (drID) references servr (drID),
constraint programmeForeignKey foreign key (pgID) references programme (pgID));


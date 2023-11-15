use tcc;

create table `user` (
    id BIGINT NOT NULL AUTO_INCREMENT,
    address_user varchar(255),
    name_user varchar(255) NOT NULL,
    date_birth date,
    cpf varchar(11) UNIQUE,
    cellphone varchar(30),
    email varchar(30) NOT NULL UNIQUE,
    password_user varchar(255) NOT NULL,
    credit BIGINT,
    terms_conditions boolean NOT NULL,
    share_data boolean NOT NULL,
    PRIMARY KEY (id)
)ENGINE=InnoDB DEFAULT CHARSET=latin1;

create table `battery` (
    id BIGINT NOT NULL AUTO_INCREMENT,
    type_battery varchar(8) NOT NULL,
    PRIMARY KEY (id)
)ENGINE=InnoDB DEFAULT CHARSET=latin1;

create table `deposit` (
    id BIGINT NOT NULL AUTO_INCREMENT,
    date_deposit date NOT NULL,
    id_user BIGINT,
    earned_credit BIGINT,
    id_battery BIGINT,
    number_of_batteries BIGINT,
    PRIMARY KEY (id),
    FOREIGN KEY (id_user) REFERENCES `user`(id),
    FOREIGN KEY (id_battery) REFERENCES `battery`(id)
)ENGINE=InnoDB DEFAULT CHARSET=latin1;

create table `prize` (
    id BIGINT NOT NULL AUTO_INCREMENT,
    name_prize varchar(255) NOT NULL,
    cost BIGINT NOT NULL,
    description_prize varchar(255) NOT NULL,
    PRIMARY KEY (id)
)ENGINE=InnoDB DEFAULT CHARSET=latin1;

create table `trade` (
    id BIGINT NOT NULL AUTO_INCREMENT,
    date_trade date NOT NULL,
    id_user BIGINT,
    id_prize BIGINT,
    PRIMARY KEY (id),
    FOREIGN KEY (id_user) REFERENCES `user`(id),
    FOREIGN KEY (id_prize) REFERENCES `prize`(id)
)ENGINE=InnoDB DEFAULT CHARSET=latin1;

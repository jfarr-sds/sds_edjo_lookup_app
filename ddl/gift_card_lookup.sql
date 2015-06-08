create table cards(
	row_id serial primary key,
	card_id char(50) not null
);

create table claimed_cards(
	row_id serial primary key,
	respondent_id char(50) not null,
	card_id char(50) not null
);

create table eligible_respondents(
	row_id serial primary key,
	respondent_id char(50) not null
);
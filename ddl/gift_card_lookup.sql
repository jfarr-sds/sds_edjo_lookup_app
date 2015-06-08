create table cards(
	row_id serial primary key,
	card_id char(50) not null
);

CREATE INDEX ON cards (card_id);

create table claimed_cards(
	row_id serial primary key,
	respondent_id char(50) not null,
	card_id char(50) not null
);

create index on claimed_cards (respondent_id);
create index on claimed_cards (card_id);

create table eligible_respondents(
	row_id serial primary key,
	respondent_id char(50) not null
);

create index on eligible_respondents (respondent_id);
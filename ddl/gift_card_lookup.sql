create table cards(
	row_id serial primary key,
	card_id char(50) not null
);

create index on cards (card_id);

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

grant select on cards to flask_user;

grant select, insert on claimed_cards to flask_user;

grant select, insert on eligible_respondents to flask_user;

grant usage on cards_row_id_seq to flask_user;
grant usage on claimed_cards_row_id_seq to flask_user;
grant usage on eligible_respondents_row_id_seq to flask_user;
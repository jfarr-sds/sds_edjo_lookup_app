\c edjo_lookup;

create table decoded_lookup(
	row_id serial primary key,
	key int not null,
	value char(8) not null
);

copy decoded_lookup(key, value) from '/tmp/decoded_lookup.csv' delimiter ',' csv;

grant select on decoded_lookup to flask_user;
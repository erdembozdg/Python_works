select distinct city from station where city regexp "^[a,e,i,o,u].*"
select distinct city from station where city regexp "^[^aeiou].*"
select distinct city from station where left(city,1) not in ('a','e','i','o','u')
select distinct city from station where city regexp '^[^aeuio]|.*[^aeuio]$'
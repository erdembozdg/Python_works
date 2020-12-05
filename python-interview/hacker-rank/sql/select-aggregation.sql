select floor(avg(population)) from city;
select max(population) - min(population) from city;
select (salary*months) as earnings, count(*) from employee group by earnings order by 1 desc limit 1
select round(long_w,4) from station where lat_n = (select max(lat_n) from station where lat_n < 137.2345)

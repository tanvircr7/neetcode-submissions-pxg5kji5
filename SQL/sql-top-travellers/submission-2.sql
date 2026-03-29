-- Write your query below
select u.name, COALESCE(SUM(r.distance),0) as travelled_distance
from users u left join rides r 
on u.id = r.user_id
GROUP BY u.id
ORDER BY travelled_distance DESC, u.name ASC
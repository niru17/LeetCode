# Write your MySQL query statement below
select c1.id, c1.movie, c1.description, c1.rating
from Cinema c1
inner join Cinema c2
ON c1.id=c2.id
WHERE c1.description NOT IN ("boring") 
GROUP BY c1.id, c1.movie, c1.description, c1.rating
HAVING MOD(c1.id,2)<>0
ORDER BY c1.rating desc;
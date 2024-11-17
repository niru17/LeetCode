# Write your MySQL query statement below
(select 'Low Salary' as Category,count(if(income<20000,1,null)) as accounts_count
from Accounts)
UNION 
(select 'Average Salary' as Category,count(if(income>=20000 and income<=50000,1,null)) as accounts_count
from Accounts)
UNION
(select 'High Salary' as Category,count(if(income>50000,1,null)) as accounts_count
from Accounts)
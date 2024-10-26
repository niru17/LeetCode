# Write your MySQL query statement below
SELECT w2.id
FROM Weather w1, Weather w2
WHERE DATEDIFF(W2.recordDate,W1.recordDate)=1 AND w1.temperature<w2.temperature;
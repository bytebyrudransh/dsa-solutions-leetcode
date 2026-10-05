# Write your MySQL query statement below
select sell_date,
    COUNT(DISTINCT product) as num_sold,
    GROUP_CONCAT(DISTINCT product order by product ASC separator ',') as products
from Activities
group by sell_date
order by sell_date
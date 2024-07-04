select e.id, e.name, count(s.id) as sales_c, rank() over(order by count(s.id) desc) as sales_rank_c, sum(s.price) as sales_s, rank() over(order by sum(s.price) desc) as sales_rank_s
from employee e
left join sales s on e.id=s.employee_id
GROUP by e.id
ORDER BY e.id
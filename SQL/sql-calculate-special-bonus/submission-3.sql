-- Write your query below
SELECT
    e.employee_id,
    CASE
        WHEN e.employee_id%2 = 1 AND e.name NOT LIKE 'M%' THEN salary
        ELSE 0
    END AS bonus
FROM employees as e
ORDER BY employee_id
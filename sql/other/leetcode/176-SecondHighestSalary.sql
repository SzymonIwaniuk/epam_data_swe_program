SELECT
    CASE 
        WHEN (
            SELECT DISTINCT salary AS SecondHighestSalary
            FROM Employee
            ORDER BY salary DESC
            OFFSET 1 LIMIT 1
        ) IS NULL
        THEN NULL
        ELSE (
            SELECT DISTINCT salary AS SecondHighestSalary
            FROM Employee
            ORDER BY salary DESC
            OFFSET 1 LIMIT 1
        )
    END AS SecondHighestSalary;

USE phonepe;
SELECT state, SUM(transaction_amount) AS total_amount
FROM aggregated_transaction
GROUP BY state
ORDER BY total_amount DESC;
SELECT year, SUM(transaction_count) AS total_transactions
FROM aggregated_transaction
GROUP BY year
ORDER BY year;
SELECT transaction_type, SUM(transaction_amount) AS total_amount
FROM aggregated_transaction
GROUP BY transaction_type
ORDER BY total_amount DESC;
SELECT quarter, SUM(transaction_amount) AS total_amount
FROM aggregated_transaction
WHERE year = 2022
GROUP BY quarter
ORDER BY quarter;
SELECT *
FROM aggregated_transaction
WHERE state = 'karnataka' AND year = 2022;

SELECT
    company_name,
    COUNT(*) AS vagas
FROM vagas_dados_gupy
GROUP BY company_name
ORDER BY vagas DESC
LIMIT 10;
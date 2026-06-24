SELECT
    type,
    COUNT(*) AS total
FROM vagas_dados_gupy
GROUP BY type
ORDER BY total DESC;
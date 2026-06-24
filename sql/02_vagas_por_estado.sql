SELECT
    state,
    COUNT(*) AS total_vagas
FROM vagas_dados_gupy
GROUP BY state
ORDER BY total_vagas DESC;
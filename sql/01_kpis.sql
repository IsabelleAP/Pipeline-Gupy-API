-- Total de vagas
SELECT COUNT(*) AS total_vagas
FROM vagas_dados_gupy;

-- Estado com mais vagas

SELECT
    state,
    COUNT(*) AS total
FROM vagas_dados_gupy
GROUP BY state
ORDER BY total DESC
LIMIT 1;

-- Tipo de contrato predominante

SELECT
    type,
    COUNT(*) AS total
FROM vagas_dados_gupy
GROUP BY type
ORDER BY total DESC
LIMIT 1;
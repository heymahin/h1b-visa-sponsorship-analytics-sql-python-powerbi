USE h1b_project;

-- =====================================================
-- H1B VISAS CAPSTONE PROJECT
-- analysis_queries.sql
-- =====================================================

-- 1. Top Sponsoring Employers
SELECT EMPLOYER_NAME, COUNT(*) AS total_filings
FROM h1b_clean
GROUP BY EMPLOYER_NAME
ORDER BY total_filings DESC
LIMIT 10;


-- 2. Highest Paying Job Roles
SELECT JOB_TITLE,
       ROUND(AVG(ANNUAL_SALARY), 2) AS avg_salary
FROM h1b_clean
GROUP BY JOB_TITLE
HAVING COUNT(*) >= 20
ORDER BY avg_salary DESC
LIMIT 10;


-- 3. Best States for H1B Opportunities
SELECT WORKSITE_STATE,
       COUNT(*) AS total_jobs
FROM h1b_clean
GROUP BY WORKSITE_STATE
ORDER BY total_jobs DESC
LIMIT 10;


-- 4. Job Concentration by State
SELECT WORKSITE_STATE,
       JOB_TITLE,
       COUNT(*) AS total_jobs
FROM h1b_clean
GROUP BY WORKSITE_STATE, JOB_TITLE
ORDER BY total_jobs DESC
LIMIT 20;


-- 5. Top Industries Hiring H1B Workers
SELECT NAICS_CODE,
       COUNT(*) AS total_filings
FROM h1b_clean
GROUP BY NAICS_CODE
ORDER BY total_filings DESC
LIMIT 10;


-- 6. Average Salary by State
SELECT WORKSITE_STATE,
       ROUND(AVG(ANNUAL_SALARY), 2) AS avg_salary
FROM h1b_clean
GROUP BY WORKSITE_STATE
ORDER BY avg_salary DESC
LIMIT 10;


-- 7. Visa Class Distribution
SELECT VISA_CLASS,
       COUNT(*) AS total_filings
FROM h1b_clean
GROUP BY VISA_CLASS
ORDER BY total_filings DESC;


-- 8. Full-Time vs Part-Time Positions
SELECT FULL_TIME_POSITION,
       COUNT(*) AS total_positions
FROM h1b_clean
GROUP BY FULL_TIME_POSITION;


-- 9. Quarterly Filing Trend
SELECT quarter,
       COUNT(*) AS total_filings
FROM h1b_clean
GROUP BY quarter
ORDER BY quarter;


-- 10. Highest Paying Employers
SELECT EMPLOYER_NAME,
       ROUND(AVG(ANNUAL_SALARY), 2) AS avg_salary,
       COUNT(*) AS total_jobs
FROM h1b_clean
GROUP BY EMPLOYER_NAME
HAVING COUNT(*) >= 20
ORDER BY avg_salary DESC
LIMIT 10;
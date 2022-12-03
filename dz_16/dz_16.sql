"""1. Запит на отримання всіх даних з таблиці employees упорядкованих за
прізвищами"""
SELECT * FROM pds.employees order by LAST_NAME

"""2. Запит на отримання даних: імена, прізвища, зарплатня, податок (15% від
зарплатні) з таблиці employees упорядкованих за прізвищами"""
SELECT FIRST_NAME, LAST_NAME,  SALARY, (SALARY * 0.15) AS TAX
FROM pds.employees
order by LAST_NAME

"""3. Запит на отримання загальної суми зарплатні всіх робітників з таблиці
employees"""
SELECT SUM(SALARY)
FROM pds.employees

"""4. Запит на отримання максимальної та мінімальної зарплатні з таблиці
employees"""
SELECT MAX(SALARY), MIN(SALARY)
FROM pds.employees

"""5. Запит на отримання середньої зарплатні та кількості працівників з таблиці
employees"""
SELECT AVG(SALARY), count(EMPLOYEE_ID)
FROM pds.employees;

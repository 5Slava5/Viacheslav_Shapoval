"""1. Запит на отримання кількості вакансій з таблиці employees"""
select count(JOB_ID) from employees

"""2. Запит на отримання середньої заробітної плати та кількості працівників
відділу 90 з таблиці employees"""
SELECT AVG(SALARY) as AVG_SALARY, count(EMPLOYEE_ID) as NUM_STUFF_90 from employees
where DEPARTMENT_ID = 90

"""3. Запит на отримання кількості працівників з тією ж самою роботою"""
SELECT JOB_ID, count(JOB_ID) from employees
group by JOB_ID

"""4. Запит на отримання всіх імен та прізвищ працівників з номером та назвою
відділу"""
SELECT * from employees right join departments
on employees.DEPARTMENT_ID = departments.DEPARTMENT_ID

"""5. Запит на отримання всіх імен та прізвищ працівників, з назвою роботи,
ідентифікатором відділу, та імен співробітників, які працюють у Лондоні"""
SELECT * from employees left join departments
on employees.DEPARTMENT_ID = departments.DEPARTMENT_ID
where LOCATION_ID = 2400

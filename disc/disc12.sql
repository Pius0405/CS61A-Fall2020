-- 2.1
select Name 
from records
where Supervisor = "Oliver Warbucks";

-- 2.2
select Name
from records
where Supervisor = Name;

-- 2.3
select Name
from records
where Salary > 50000
order by name;

-- 3.1
select meetings.Day, meetings.Time
from records, meetings
where records.Supervisor = "Oliver Warbucks"  
and records.Division = meetings.Division;

-- 3.2
-- A pair of employees will appear more than once since they can have meetings at the same time for more than once (ans for 3.3)
select r1.Name, r2.Name 
from records as r1, records as r2, meetings as m1, meetings as m2
where r1.name <> r2.Name and r1.Name < r2.Name and r1.Division = m1.Division
and r2.Division = m2.Division and m1.Day = m2.Day and m1.Time = m2.Time;

-- 3.3
-- No, a pair of employee might have meetings at the same time for more than once so the same record will appear twice and will not
-- be filtered.

-- 3.4
select r1.Name 
from records as r1, records as r2
where r1.Supervisor = r2.Name and r1.Division <> r2.Division;

-- 4.1
select Supervisor, sum(Salary)
from records
group by Supervisor;

--4.2
select meetings.Day
from records, meetings
where records.Division = meetings.Division
group by meetings.Day
having count(records.Name) < 5;

-- 4.3
select r1.Division
from records as r1, records as r2
where r1.Name <> r2.Name and r1.Name < r2.Name and r1.Division = r2.Division
group by r1.Division
having max(r1.Salary + r2.Salary) < 100000;

-- 5.1
-- Joining two tables will result in a unique combination of one row from each table so joining tables A, B will have 5 x 3 = 15 rows
create table num_taught as 
select Professor as Professor, Course as Course, count(Course) as times
from courses
group by Professor, Course;

-- 5.2
select a.Professor, b.Professor, a.Course
from num_taught as a, num_taught as b
where a.Course = b.Course and a.Professor < b.Professor and a.times = b.times;

-- 5.3
select a.Professor, b.Professor 
from courses as a, courses as b
where a.Professor < b.Professor and a.semester = b.semester and a.course = b.course
group by a.Professor, b.Professor, a.course
having count(*) > 1;


# air_call
## The main idea of my solution is:
Create a delta table with the daily or hourly information, once we have that information, we insert it into the fact table with a left outer join. 
So we only insert the new users,  taking into account the repository and the user's name.

## Consideration:
* The table has a PK per repository and name and would have to be partitions with the same columns.
* You would have to do a delete with the same period, because  if we have rerun the pipeline we need to remove the olds rows.
* Rate limit, you could look for more efficient algorithms such as Leaky Bucket or Fixed Window.

## Test:
I have generated a server mock using postman and some unit tests have been done.

## Problems:
I have had several problems with the API, mainly the speed limit, the second with trying to develop an algorithm for failures (in my opinion, this responsibility should have a three-part tool like airflow or Azkaban).

## Data base:
```` sql
DROP TABLE `fact_commit`;
CREATE TABLE `fact_commit` (
  `date_commit` varchar(10) ,
  `repository` varchar(30),
  `user` varchar(30),
  PRIMARY KEY (`repository`,`user`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

INSERT INTO fact_commit (date_commit,repository,user) 
SELECT date(s.date_commit) as date_commit, s.repository, s.user
  FROM delta_commit s
  LEFT OUTER JOIN aircall.fact_commit a 
  ON a.repository = s.repository
  AND a.user = s.user
  WHERE a.user IS NULL;
  ````

# Docker:
````sh
 docker run --name some-mysql -e MYSQL_ROOT_PASSWORD=my-secret-pw  -p 3306:3306 -d mysql:5.7
 ````
  
## Librerias:  
time
dateutil
requests
pandas
sqlalchemy
requests

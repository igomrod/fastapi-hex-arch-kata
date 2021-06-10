# Kata: Simple TODOs but qith nice arch

## STEP 1

* Create project from cookiecutter template https://github.com/Gradiant/fastapi-cookiecutter-template
* Install requirements and run tests 
* Run server and check http://0.0.0.0:5000/status

## STEP 2 

* Implement and endpoint "/api/todos"
* POST should add a new todo
* GET should return all todos
* Each retrieved todo includes: title, description
* title is required and max 5 words
* description is required and max 15 words

Note: It is ok to store todos in memory

## STEP 3 - NEW REQUIREMENT
* Each retrieved todo must include a field "daysSinceCreated" set to number of days since todo was originally created

## STEP 4 - NEW REQUIREMENT
* We need to store todos not only from HTTP API but also from a Kafka topic

Note: Do not actually implement it, just think of how you would do it 

## STEP 5 - NEW REQUIREMENT
* Each new todo must be notified to a service maintained by a different team in your org
* Suddenly your TODOs app achieve a big success, you are storing millions of TODO per minute

Note: Do not implement, just think of how you could do it.
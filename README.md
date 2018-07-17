# web_data_collector_with_PostgreSQL

This web-application allow users to enter their height and calculate average height of all users. 
Then, send the email, which contains height information, to the user who just submitted data.
The data is stored in PostgreSQL. The web is bulit by Flask, which is python web framework.
It uses psycopg2 and Flask-SQLAlchemy to build the database object to communicate with Flask.


This page allows users to enter their information.
<img width="685" alt="screen shot 2018-07-17 at 11 57 17 am" src="https://user-images.githubusercontent.com/35472776/42839569-fc3bef38-89b8-11e8-85cf-a2288e9998c1.png">





If the user enter the email which has already existed, the page would inform the user to retype the email because the app would check if the database has this email or not.

<img width="682" alt="screen shot 2018-07-17 at 11 58 09 am" src="https://user-images.githubusercontent.com/35472776/42839577-025df33e-89b9-11e8-8ec6-76f334096911.png">






<img width="997" alt="screen shot 2018-07-17 at 11 58 41 am" src="https://user-images.githubusercontent.com/35472776/42839583-075f19b2-89b9-11e8-9428-8ca8e0ed5186.png">






<img width="1278" alt="screen shot 2018-07-17 at 12 02 56 pm" src="https://user-images.githubusercontent.com/35472776/42839721-7081e01e-89b9-11e8-8aec-700ffafd7484.png">






<img width="681" alt="screen shot 2018-07-17 at 11 57 00 am" src="https://user-images.githubusercontent.com/35472776/42839596-0ce78630-89b9-11e8-93e1-010c906955fb.png">

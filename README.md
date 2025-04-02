<h1>World Landmarks</h1>
<hr>
<p>Web application for manipulating data about world landmarks</p>
<hr>
<h2>Technologies</h2>
<li>Python</li>
<li>Flask</li>
<li>SQLAlchemy</li>
<li>Flask-JWT-Extended</li>
<li>Flask-RESTful</li>
<li>Werkzeug</li>


<h2>Basic functionality</h2>
<h3>Users</h3>
<li>Registering a new user</li>
<li>User Authentication (JWT)</li>
<li>Получение информации о пользователе</li>
<hr>
<h3>Landmarks</h3>
<li>Creating a new landmark (available only to registered users)</li>
<li>Getting a list of all the attractions</li>
<li>Getting information about a specific landmark</li>
<li>Editing and deleting only your own landmarks</li>
<hr>
<h3>Photo</h3>
<li>Uploading a new photo to a landmark</li>
<li>Getting a list of photos of a specific landmark</li>
<li>Deleting only your photos</li>
<hr>
<h3>Rating</h3>
<li>Adding a rating to a landmark</li>
<li>Getting an average rating for a specific attraction</li>
<li>Deleting and editing only your own rating</li>
<hr>
<h3>Filtering and sorting</h3>
<li>Filtering landmarks by country</li>
<li>Sort by rating</li>
<hr>
<h3>Endpoint</h3>
<li></li>
<li></li>
<b>Work in Progress</b>
<hr>
<h3>Security</h3>
<li>Hashing passwords</li>
<li>authentication via JWT</li>
<li>Users can edit and delete only their own data (photos, landmarks, ratings)</li>
<hr>
<h2>License</h2>
<p>Open and read the License of the project</p>

<h2>Project Setup</h2>

```
pip install -r requirements.txt
```

<h2>Run</h2>

```
flask --app main run
```

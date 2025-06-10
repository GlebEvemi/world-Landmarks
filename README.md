
# World Landmarks
---

Web application for manipulating data about world landmarks  
---

## Technologies

- Python  
- Flask  
- SQLAlchemy  
- Flask-JWT-Extended  
- Flask-RESTful  
- Werkzeug  

## Basic functionality

### Users

- Registering a new user  
- User Authentication (JWT)  
- Getting user information  

---

### Landmarks

- Creating a new landmark (available only to registered users)  
- Getting a list of all the attractions  
- Getting information about a specific landmark  
- Editing and deleting only your own landmarks  

---

### Photo

- Uploading a new photo to a landmark  
- Getting a list of photos of a specific landmark  
- Deleting only your photos  

---

### Rating

- Adding a rating to a landmark  
- Getting an average rating for a specific attraction  
- Deleting and editing only your own rating  

---

### Filtering and sorting

- Filtering landmarks by country  
- Sort by rating  

---

### Endpoint

-  
-  
**Work in Progress**  

---

### Security

- Hashing passwords  
- Authentication via JWT  
- Users can edit and delete only their own data (photos, landmarks, ratings)  

---

## License

Open and read the License of the project  

## Project Setup

```bash
pip install -r requirements.txt
```

## Run


## Authentication
| Method | Endpoint                | Description                                                       | Auth Required |
| ------ | ----------------------- | ----------------------------------------------------------------- | ------------- |
| POST   | `/user/register`        | Register a new user and receive a JWT token                       | Open             |
| POST   | `/user/login`           | Login with username/email and password, get a JWT                 | Open             |
| GET    | `/user/me`              | Get info about the current authenticated user                     | Authorized user             |

## Landmarks
| Method | Endpoint                | Description                                                       | Auth Required |
| ------ | ----------------------- | ----------------------------------------------------------------- | ------------- |
| POST   | `/landmark`             | Create a new landmark                                             | Authorized user             |
| GET    | `/landmark`             | Get a list of landmarks, with optional country filter and sorting | Open             |
| GET    | `/landmark/{id}`        | Get detailed info about a specific landmark                       | Authorized user             |
| PUT    | `/landmark/{id}`        | Update a landmark by ID                                           | Owner             |
| DELETE | `/landmark/{id}`        | Delete a landmark                                                 | Owner             |

## Landmark Photos
| POST   | `/landmark/{id}/photo`  | Upload a photo for the specified landmark                         | Authorized user |
| GET    | `/landmark/{id}/photo`  | Get a list of photos for the specified landmark                   | Open             |
| DELETE | `/photo/{id}`           | Delete a photo by its ID                                          | Owner             |

## Rating 
| GET    | `/landmark/{id}/rating` | Get average rating and comments for the specified landmark        | Open             |
| POST   | `/landmark/{id}/rating` | Add a new rating and comment for a landmark                       | Authorized user |
| PUT    | `/rating/{id}`          | Update a rating and comment                                       | Owner             |
| DELETE | `/rating/{id}`          | Delete a rating                                                   | Owner             |

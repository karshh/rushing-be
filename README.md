# TSI "the Rush" Challenge

The purpose of this server is to provide endpoints in order to load and recieve player data. See
* [Frontend Project](https://github.com/karshh/rushing-fe)

### Installation and setup
- Clone the repository
- Set up the environment variables.
   ```
   cp .env.example .env
   vim .env
   ```
The following 2 ways can be used to run the application in development.
**1. venv**

- Update `MONGO_URL` in .env to your local mongo connection. Example `mongodb://localhost:27017/rushing`
- Run `python3 -m venv venv` to set up the virtual environment.
- Activate the virtual environement with `source ./venv/bin/activate`
- Install all dependencies with `pip install -r requirements.txt`
- Run `python -m main` to start the server
- To run unit tests, run `pytest`

**2. docker**

- Update `MONGO_URL` in .env to `mongodb://mongo:27017/rushing`
- Run `docker-compose build` to build docker images, and `docker-compose up` to start the containers. Alternatively, we can run `docker-compose up --build` to do both.


### Using the App

The server exposes 2 endpoints.


### `GET /players`


**Parameters**
- `sortColumn`: The column to sort by. By default, this is `Player`
- `sortDirection`: A value of 1 representing ascending, and -1 representing descending. By default, this value is 1
- `filter`: filters the list by `Player` property. This is case-insensitive.
- `skip`: Skip players and return the remaining list.
- `limit`: Limits the number of players returned.

Note that `size` is unaffected by all parameters except `filter`.

**Response**
Returns a list consisting of the following
- `size`: The size of the list
- `players`: The list of players

**Example**: 
```
GET /players/?skip=5&limit=2&sortColumn=Lng&sortDirection=1&filter=As
{
    "players": [
        {
            "1st": 7,
            "1st%": 35.0,
            "20+": 0,
            "40+": 0,
            "Att": 20,
            "Att/G": 2.0,
            "Avg": 2.6,
            "FUM": 0,
            "Lng": "13",
            "Player": "Case Keenum",
            "Pos": "QB",
            "TD": 1,
            "Team": "LA",
            "Yds": 51,
            "Yds/G": 5.1
        },
        {
            "1st": 1,
            "1st%": 25.0,
            "20+": 1,
            "40+": 0,
            "Att": 4,
            "Att/G": 0.3,
            "Avg": 7.3,
            "FUM": 0,
            "Lng": "23",
            "Player": "De'Anthony Thomas",
            "Pos": "WR",
            "TD": 0,
            "Team": "KC",
            "Yds": 29,
            "Yds/G": 2.4
        }
    ],
    "size": 12
}
```

### `/POST /players/upload`

**Body**
A list of players. See [rushing.json](https://raw.githubusercontent.com/tsicareers/nfl-rushing/master/rushing.json) as example.

**Response**
A `null` response with the status code indicating success.


### Deployment
For the purpose of demonstration, this project is deployed in heroku at the moment at https://tsi-karsh-backend.herokuapp.com/. 

Install Heroku CLI and log in using the command ```heroku login```

Create your heroku project.
```
heroku create app-name
```
Add MONGO_URL to heroku config. (Replace string with your mongo cloud URL, this is just an example): 
```
heroku config:set MONGO_URL='mongodb://<username>:<password>@hostname/prod?retryWrites=false'
```
Once done, push the code to heroku.
```
git push heroku master
```

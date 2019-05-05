Flask API Flisol 2019
=====================

API criada no [FLISOL 2019](https://flisol.info/FLISOL2019/Brasil/SaoLuis) usando [Flask](http://flask.pocoo.org/). Esta edição aconteceu na [Universidade Ceuma Renasçenca](https://www.extranet.ceuma.br/novoportal/) em São Luís do Maranhão.

### API actions of People

|Action	 |HTTP Verb |URL Path                |Description
|--------|----------|------------------------|---------------------------------------------
|Create  |POST	    |/api/people/            |URL to create a new person, unique person
|Read    |GET       |/api/people/            |URL to read a collection of people
|Read    |GET       |/api/people/{person_id} |URL to read a single person by person_id
|Update  |PUT       |/api/people/{person_id} |URL to update an existing person by person_id
|Delete  |DELETE    |/api/people/{person_id} |URL to delete an existing person by person_id

### [LICENSE](./LICENSE)

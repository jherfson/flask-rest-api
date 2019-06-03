Flask REST API
==============

Flask API Flisol 2019
---------------------

API criada no [FLISOL 2019](https://flisol.info/FLISOL2019/Brasil/SaoLuis) usando [Flask](http://flask.pocoo.org/). Esta edição aconteceu na [Universidade Ceuma Renasçenca](https://www.extranet.ceuma.br/novoportal/) em São Luís do Maranhão.

### API actions of People

|Action	 |HTTP Verb |URL Path                |Description                                  |
|--------|----------|------------------------|---------------------------------------------|
|Create  |POST	    |/api/people/            |URL to create a new person, unique person    |
|Read    |GET       |/api/people/            |URL to read a collection of people           |
|Read    |GET       |/api/people/{person_id} |URL to read a single person by person_id     |
|Update  |PUT       |/api/people/{person_id} |URL to update an existing person by person_id|
|Delete  |DELETE    |/api/people/{person_id} |URL to delete an existing person by person_id|

### API actions of Notes

|Action	 |HTTP Verb |URL Path                                |Description                                                 |
|--------|----------|----------------------------------------|------------------------------------------------------------|
|Create  |POST      |/api/people/{person_id}/notes           |URL to create a new note                                    |
|Read    |GET       |/api/people/{person_id}/notes/{note_id} |URL to read a single person’s single note                   |
|Update  |PUT       |/api/people/{person_id}/notes/{note_id} |URL to update a single person’s single note                 |
|Delete  |DELETE    |/api/people/{person_id}/notes/{note_id} |URL to delete a single person’s single note                 |
|Read    |GET       |/api/notes                              |URL to get all notes for all people sorted by note.timestamp|

### TO DO

[ ] Adicionar tratamento de erros em funções.
[ ] Criar estrutura própria de tratamento de erros.
[ ] Adicionar Docker ao projeto.
[ ] Cria funcoes únicas de nos resources que compartilhem mais de um verbo HTTP.

### [LICENSE](./LICENSE)

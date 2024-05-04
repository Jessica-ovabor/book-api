<!-- Back to Top Navigation Anchor -->
<a name="readme-top"></a>

<!-- Project Shields -->
<div align="center">

  [![Contributors][contributors-shield]][contributors-url]
  [![Forks][forks-shield]][forks-url]
  [![Issues][issues-shield]][issues-url]
  [![MIT License][license-shield]][license-url]
  [![Twitter][twitter-shield]][twitter-url]
</div>

<!-- Project Name -->
<div align="center">
  <h1>Fast API-Book Api</h1>
</div>

<div>
  <p align="center">
    <a href="https://github.com/Jessica-ovabor
/book-api#readme"><strong>Explore the Documentation »</strong></a>
    <br />
    <a href="https://github.com/Jessica-ovabor
/JessiSchool/blob/main/images/student_api_full_page.png">View Demo</a>
    ·
    <a href="https://github.com//Jessica-ovabor
/book-api/issues">Report Bug</a>
    ·
    <a href="https://github.com/Jessica-ovabor
/book-api/issues">Request Feature</a>
  </p>
</div>

---

<!-- Table of Contents -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-book-api">About Book API</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>

  </ol>
  <p align="right"><a href="#readme-top">back to top</a></p>
</details>

---

<!-- About the Project -->
## About Book Api

Book API is a simple API built with FAST Api that in which perform a simple CRUD operation for user to update a book by id , create a book with the required paraameters like title, year etc , delete a book by its id , get a book by its id and get all books present in the database.

Also there is an easy-to-use Swagger UI setup for testing in the absence of testing tools like insomnia and postman.


This Book Api was built with FAST Api by <a href="https://www.github.com/Jessica-ovabor">Jessica Ovabor</a> 
<p align="right"><a href="#readme-top">back to top</a></p>

### Built With:

![Python][python]
![FASTApi][fastapi]
![SQLite][sqlite]


<p align="right"><a href="#readme-top">back to top</a></p>

---
<!-- Lessons from the Project -->
## Deliverables

Creating this API:
* API Development with FAST Api
* Unit Testing using Postman
* Routing
* Swagger Documentation
* Debugging
* Database Management
* Deployment

<p align="right"><a href="#readme-top">back to top</a></p>

---
<!-- What the API can do -->
## Component

The Book API handles the following:
* Create a new book
* Get a new book by ID
* Get all books
* Update book by ID
* Delete book by ID



---

<!-- GETTING STARTED -->
## Usage

To explore and use this API, follow these steps:

1. After cloning and making sure the app is running click on the url and add / docs to it : example (http://127.0.0.1:8000/docs)

2. Create a new book:
   - Click '/create/books' to create a new book
3. Get New Book By ID
   -  Click '/get/books/id
4. Get list of Books
   - Click on '/get/books/'
5. Update Books By ID
   - Click on '/update/books/id'
6.  Delete Books By ID
    - Click on '/delete/books/id'

  

<p align="right"><a href="#readme-top">back to top</a></p>

---

<!-- Installing this app on your machine locally -->
## Installation

<div></div>
<ul style="font-size:18px;">
    <li>Clone the repository to your local machine.</li>
    <li>Navigate to the project directory.</li>
    <li>Create a virtual environment and activate it:</li>
    <li>Open the requirements.txt file</li>
    <li>Install the dependencies:</li>
    <li>Run the application:</li>
</ul>

### To create a virtual environment called 'env' and activate it.

```console
python -m venv env
env/Scripts/Activate
```

**Note:** Make sure the `requirement.txt` file is present

```console
pip install -r requirements.txt
```

### To create your database locally.

```console
run `utils.py` 

```

### Finally, To run the application.

```console
uvicorn app:app --reload 
```

# Endpoints for the Book  API

<div style="margin-top:8px; margin-bottom:10px; font-size:20px; font-weight:bold;">Book Api Endpoints</div>
<!-- Tables for routing in each models -->

| ROUTE                          | METHOD | DESCRIPTION                                   | AUTHORIZATION          | USER TYPE |
|--------------------------------| ------ |-----------------------------------------------|------------------------|-----------|
| `/create/books/`               | _POST_ |  Creation of books                            |     `None`             | Any       |
| `/get/books/id`                | _GET_  |  Get books by ID                              |    `None`              | Any       |
| `/get/books/  `                | _GET_  |  Get All Books                                |    `None`              | Any       |  
| `/delete/books/id`             | _DEL_  |  Deletion of books                            |     `None`             | Any       |
| `/update/books/id`             | _PUT_  |  Update books by ID                           |    `None`              | Any       |






---



<p align="right"><a href="#readme-top">back to top</a></p>

---

<!-- License -->
## License

Distributed under the MIT License. See <a href="https://github.com/Jessica-ovabor/book-apiblob/main/LICENSE">LICENSE</a> for more information.

<p align="right"><a href="#readme-top">back to top</a></p>

---

<!-- Contact -->
## Contact

You can contact me with my social media handles:

[LinkedIn](https://www.linkedin.com/in/jovabor) | [Twitter](https://twitter.com/jovabor) | [Github](https://github.com/Jessica-ovabor) | Email: ovaborjessica85@gmail.com

Project Link: [Book Api](https://github.com/Jessica-ovabor/book-api)

<p align="right"><a href="#readme-top">back to top</a></p>

---



<p align="right"><a href="#readme-top">back to top</a></p>

---

<!-- Markdown Links & Images -->
[contributors-shield]: https://img.shields.io/github/contributors/Oluwatemmy/Student-Management-API.svg?style=for-the-badge
[contributors-url]: https://github.com/Oluwatemmy/Student-Management-API/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Oluwatemmy/Student-Management-API.svg?style=for-the-badge
[forks-url]: https://github.com/Oluwatemmy/Student-Management-API/network/members
[issues-shield]: https://img.shields.io/github/issues/Jessica-ovabor/JessiSchool.svg?style=for-the-badge
[issues-url]: https://github.com/Jessica-ovabor/BOOK-API/issues
[license-shield]: https://img.shields.io/github/license/Jessica-ovabor/JessiSchool.svg?style=for-the-badge
[license-url]: https://github.com/Jessica-ovabor/JessiSchool-API/blob/main/LICENSE
[twitter-shield]: https://img.shields.io/badge/-@jovabor-1ca0f1?style=for-the-badge&logo=twitter&logoColor=white&link=https://twitter.com/ze_austin
[twitter-url]: https://twitter.com/jovabor

[python]: https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54
[![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=flat&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)

[sqlite]: https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white!(https://user-images.githubusercontent.com/74324460/226195821-80565e9c-bc4a-450b-8f5f-aa2e4535ba83.png)


# Tamu Foods
Tamu Foods is afood deliery web application that enables our users to order food online from our patner restaurants.


# App screenshot
![Tamu Foods](/app/static/assets/Tamu-Foods.png)
## Installation

Guide to install Blog APP application:

### Clone this repository
```bash
https://github.com/John-Kimani/Tamu-Foods-BackEnd.git
```
* Move into the cloned directory:
```bash
cd Tamu-Foods_BackEnd
```
* Create and activate your virtual environment:
```bash
mkvirtualenv virtual
```
* Install project dependancies within your active environment: (Read: requirements.txt and use command below)
```bash
(virtual)$ pip3 Install -r requirements.txt
```
* Environment variables:
    *  Create a file called ```.env``` in the root folder
    ```bash
    (virtual)$ touch .env
    ```
    * Add the following lines to the file as seen in ```.env-template```
    ```bash 
    SECRET_KEY=
    DATABASE_URL=
    ```
* Start the flask server
```bash
(Virtual)$ flask run
```
* or

```bash
(Virtual)$ python3 tamu.py
```
## Features and BDD

- Users are able to create user profile and login to their accounts for them to make orders.


## Technology Used

**Framework:** Flask
**Language** Python

### Developed with
**Structure:** Bootstrap, HTML
**Styles:** CSS

## Author

* Developed by: [John Kimani](https://github.com/John-Kimani)

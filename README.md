# increase
It is a social media website for companies and developers for the enhancement of the products and the software.<br><br>
- This social media is having two types of usertype:-<br>
1. company
2. developer

- The people who have signup as company will create a social page. They can post the product or software information. They can accept the idea which have been given by developers
- The people who have signup as developer can only give suggestions for the enhancement of the products or softwares.
- If the idea of a developer is accepted by the company then a green line will be shown in the background of that particular suggestion.
- On the suggestion box their will be a accept/decline option which people can select to upvote the idea.

## To run locally on the system
### setup virtual env and installing require package
- `python3 -m venv venv`
- `source venv/bin/activate` (Linux user)
- `venv\Scripts\activate` (Windows user)
- `pip3 install django`

### to run locally
- `cd increase`
- `python3 manage.py makemigrations`
- `python3 manage.py migrate`
- `python3 manage.py runserver`

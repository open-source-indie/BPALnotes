[![Build and deploy Python app to Azure Web App - BPAL](https://github.com/wathika-eng/BPALnotes/actions/workflows/main_bpal.yml/badge.svg?branch=main)](https://github.com/wathika-eng/BPALnotes/actions/workflows/main_bpal.yml)

# Class Notes.
A platform where students can access class notes shared by the lectures
And also past papers/ CAT papers

## Run Website
To run this website
1. Clone the repository to your local machine.
```
git clone https://github.com/wathika-eng/BPALnotes.git
```
2. Create a virtual enviroment & Activate it:
```python -m venv (desired env. name)```
```
source (your env name)/scripts/activate
```
3. Install requirements:
```
pip install -r requirements.txt
```
4. Run the app: (http://127.0.0.1:5000/)
```
flask run 
```
OR

5. Debugger turned on
```
flask --app app.py --debug run 
```
Runs with Debugger enabled

## REQUIREMENTS SPECIFICATION

### Technical Requirements
You can use your phone or laptop to view the website

To view on your phone you need to use a private or trusted network:

Then on your terminal type (Confirm your IP Address first by running ipconfig on CMD)
```
flask run --host=0.0.0.0 
```
Can run on your default host(e.t.c :5000)

### Non-functional requirements
- Data should be secure.
- The system should be light weight for ease of access and should load within two seconds.
- Should be responsive to different screen sizes.
- Shows notification when user is offline and reloads on re-connection.
- 396kb installable web app.

![image](https://user-images.githubusercontent.com/71040609/232247818-660e1e81-6e10-4d94-901c-d1fa23851d21.png)

![image](https://user-images.githubusercontent.com/71040609/232247828-9ffbbcf5-cdff-4a7e-94c6-4f864c3d3222.png)

![image](https://user-images.githubusercontent.com/71040609/232247843-085e625d-bff8-459b-adae-75083e02f3b3.png)

![image](https://user-images.githubusercontent.com/71040609/232247848-3d98e0a5-f33b-45ca-af43-98aa7c99eb39.png)

### Tweaks

1. Vibrates on large downloads.

2. Accordion cannot be closed.

### ISSUES
1. Lacks a download progress bar.

2. Dark-Mode not yet set-up

3. Search bar not yet working.

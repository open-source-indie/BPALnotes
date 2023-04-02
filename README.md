# Class Notes.
A platform where students can access class notes shared by the lectures
And also past papers/ CAT papers

## Run Website
To run this website
1. Clone the repository to your local machine.
```
git clone https://github.com/wathika-eng/BPALnotes.git
```
2. Create a virtual enviroment:
```
python -m venv (desired env. name)
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

4. Debugger turned on
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


![image](https://user-images.githubusercontent.com/71040609/221318019-a22c8d3b-e4e7-4dab-9b1d-2d7454415f49.png)

![image](https://user-images.githubusercontent.com/71040609/221318194-9f9fa469-7bc4-44d4-8ab3-42229b69c633.png)

![bpal azurewebsites net_research(iPhone SE)](https://user-images.githubusercontent.com/71040609/221318652-e7f1b356-42ed-49b4-a317-2e4757cfd697.png)

![bpal azurewebsites net_](https://user-images.githubusercontent.com/71040609/221318721-0938ddc7-7f61-4452-bac9-e9178452f460.png)

Sign-up form

![image](https://user-images.githubusercontent.com/71040609/221444743-8de99ff3-f02c-4ab6-b48f-c0a22dbb60c7.png)



###ISSUES
1. Lacks a download progress bar.

2. Accordion does't turn dark despite dark mode settings.

3. Search bar not yet working.
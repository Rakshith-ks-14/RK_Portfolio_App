import os
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import json

app = FastAPI()

root = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(root, 'templates')
template = Jinja2Templates(directory=file_path)

file_path = os.path.join(root, 'static')
app.mount('/static', StaticFiles(directory=file_path), name='static')

@app.get('/')
def welcome(request: Request):
    return template.TemplateResponse("welcome.html", {'request': request})

@app.get('/portfolio')
async def porfolio_page(request: Request):
    project_data = read_json_data()['portfolio']
    return template.TemplateResponse("basic.html", {'request': request, 'page': 'portfolio', 
                                                    'start_h1': project_data['start_h1'], 
                                                    'project_contents': project_data['project_contents'],
                                                    'end_h1': project_data['end_h1'],
                                                    'background': project_data['background']})

@app.get('/services')
async def services_page(request: Request):
    project_data = read_json_data()['services']
    return template.TemplateResponse("basic.html", {'request': request, 'page': 'services',
                                                    'start_h1': project_data['start_h1'],
                                                    'project_contents': project_data['project_contents'],
                                                    'end_h1': project_data['end_h1'],
                                                    'background': project_data['background']})

@app.get('/portfolio/{pid}')
async def get_project_details_by_id(request: Request, pid: str):
    project_data = read_json_data()[pid]
    return template.TemplateResponse("basic.html", {'request': request, 'page': project_data['start_h1'][0], 
                                                    'start_h1': project_data['start_h1'], 
                                                    'project_contents': project_data['project_contents'],
                                                    'end_img': project_data['end_img'],
                                                    'background': project_data['background']})

@app.get('/aboutme')
async def about_me(request: Request):
    project_data = read_json_data()['about_me']
    return template.TemplateResponse("about_me.html", {'request': request, 'page': 'about_me',
                                                       'background': project_data['background']})

@app.get('/contactme')
async def contact_me(request: Request):
    project_data = read_json_data()['contact_me']
    return template.TemplateResponse("contact_me.html", {'request': request, 'page': 'contact_me',
                                                       'background': project_data['background']})

def read_json_data():
    file_path = os.path.join(os.getcwd(), 'portfolio_data.json')
    with open(file_path, 'r') as f:
        project_data = json.loads(f.read())

    return project_data

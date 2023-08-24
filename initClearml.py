# load .env
from dotenv import load_dotenv
load_dotenv()

# ClearML
from clearml import Task
task = Task.init(project_name='rpod6', task_name='test')
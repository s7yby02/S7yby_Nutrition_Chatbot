import importlib
import os


script_directory = os.path.dirname(os.path.abspath(__file__))
module_path = os.path.join(script_directory,'..', 'model', 'model')
model = importlib.import_module(module_path)

predict_class, get_response = model.predict_class, model.get_response
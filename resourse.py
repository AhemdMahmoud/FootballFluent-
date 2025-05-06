from setfit import SetFitModel
from gliner import GLiNER
import os 
from dotenv import load_dotenv
import os


load_dotenv()
hf_token = os.getenv("hf_token")

def load_model():
    
    setfit_model_id = os.getenv("setfit_model_id","Ah7med/setfit-football_bootpress_paraph-multi-v2")
    gliner_model_id = os.getenv("gliner_model_id","urchade/gliner_multi-v2.1")
    
    
    models = {
        "intent_detection" : SetFitModel.from_pretrained(setfit_model_id),
        "entity_recongnition" : GLiNER.from_pretrained(gliner_model_id)
    }
    return models
    


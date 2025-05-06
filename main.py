# First install FastAPI using: pip install fastapi uvicorn
from fastapi import FastAPI, Response
from fastapi.middleware.cors import CORSMiddleware
from schemes import message,Team
from resourse import load_model
import uvicorn
from football import get_team_id_by_name,get_team_matches


app = FastAPI()

models= load_model()
@app.get("/")  # Fixed decorator from @get_app to @app.get
async def message_handler():
        return {"message": "Hello World"}

@app.post("/nlu")
async def get_result(message: message,
                   response: Response):
        
        
        if message.message is None  or message.message == "":
            response.status_code = 400
            return {"message": "Message is required"}
    
        intent_probs = models["intent_detection"].predict_proba(message.message).tolist()
        # intent = models["intent_detection"].predict([message.message])[0]
        max_prob_value = max(intent_probs)
        max_prob_index = intent_probs.index(max_prob_value)
        intent_label = message.intent_labels[max_prob_index]
        
        
        # Perform entity prediction
        entities = models["entity_recongnition"].predict_entities(message.message, message.entities_labels,)
        entities_values = []
        
        
        for ent in entities:
                value_id = None
                
                if ent["label"] == "team_name":
                        value_id = get_team_id_by_name(search_name= ent["text"])
                
                
                entities_values.append({
                        "entity": ent["label"],
                        "start": ent["start"],
                        "end": ent["end"],
                        "confidence_entity": ent["score"],
                        "value": ent["text"],
                        "extractor": "_",
                        "value_id": value_id
                        })
                
        return {
                "result": {
               "text": message.message,
                "intent": {
                           "name": intent_label,
                           "confidence": max_prob_value,
                     },
                "entities": entities_values
        }
                }
        
@app.post("/football/team_next_match")
async def get_team_next_match(Team:Team,
                              response:Response):
        matches = get_team_matches(Team.team_1_id,
                         Team.team_2_id,
                          mode="next")
        return {"results": matches}


@app.post("/football/team_prev_match")
async def team_prev_match(Team:Team,
                         response: Response):
    
    matches = get_team_matches(team_1_id=Team.team_1_id,
                              team_2_id=Team.team_2_id,
                              mode="last")
    
    return {"results": matches}
        
        

        
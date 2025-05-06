from pydantic import BaseModel
from typing import ClassVar, List, Optional

class message(BaseModel):
    message: str
    
    intent_labels:ClassVar[List[str]] = ['greet-hi',
                     'greet-who_are_you',
                     'greet-good_bye',
                     'matches-team_next_match',
                     'matches-match_time',
                     'matches-match_result']
    
    entities_labels:ClassVar[List[str]] = ["team_name"]
    
class Team(BaseModel):
    team_1_id: int
    team_2_id: Optional[int]= -1
    
    
def load_teams_names():
    return {
         'manchester united': 33,
         'mun': 33,
         'newcastle': 34,
         'new': 34,
         'watford': 38,
         'wat': 38,
         'wolves': 39,
         'wol': 39,
         'liverpool': 40,
         'liv': 40,
         'southampton': 41,
         'sou': 41,
         'arsenal': 42,
         'ars': 42,
         'burnley': 44,
         'bur': 44,
         'everton': 45,
         'eve': 45,
         'leicester': 46,
         'lei': 46,
         'tottenham': 47,
         'tot': 47,
         'west ham': 48,
         'wes': 48,
         'chelsea': 49,
         'che': 49,
         'manchester city': 50,
         'mac': 50,
         'brighton': 51,
         'bri': 51,
         'crystal palace': 52,
         'crystal': 52,
         'cry': 52,
         'brentford': 55,
         'bre': 55,
         'leeds': 63,
         'lee': 63,
         'aston villa': 66,
         'aston': 66,
         'villa': 66,
         'ast': 66,
         'norwich': 71,
         'nor': 71
    }
    
    
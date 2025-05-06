from schemes import load_teams_names
import textdistance
import requests
import os 


url = "https://api-football-v1.p.rapidapi.com/v3/fixtures"

football_api = os.getenv("football_api","")
headers = {
"X-RapidAPI-Key": football_api,
"X-RapidAPI-Host": "api-football-v1.p.rapidapi.com"
}



teams_names = load_teams_names()



def get_team_id_by_name(search_name: str, min_score=0.60):
    found_teams = {}
    
    for team_name, team_id in teams_names.items():
        
        sim_score = textdistance.cosine.normalized_similarity(search_name.lower(), team_name)
        
        if sim_score < min_score:
            continue
        
        found_teams[team_id] = sim_score
        
        if len(found_teams):
        
            found_teams =sorted(found_teams.items(), key=lambda item: item[1], reverse=True)
            
            return {"team_id": found_teams[0][0],"Score":found_teams[0][1]}
        
        return False 
    
def get_team_matches(team_1_id: int,
                     team_2_id: int=-1,
                    league_id: int=39,
                    season: str = "2022",
                    mode: str="last",
                    limit=99):

                    
                     
    querystring = {"league":league_id,"season":season,"team":team_1_id,f"{mode}":limit}

    ts = set([team_1_id, team_2_id])

    response = requests.request("GET", url, headers=headers, params=querystring)
    
    if response.status_code != 200:
        return False
    
    
    result = []
    response_data =  response.json   
    
    for rec in response_data:
        if team_2_id > 0:
            
            if int(rec["teams"]["home"]["id"]) not in ts or int(rec["teams"]["away"]["id"]) not in ts:
                continue   
        
        match_date = rec["fixture"]["date"]
        match_timezone = rec["fixture"]["timezone"]
        team_home = rec["teams"]["home"]
        team_away = rec["teams"]["away"]  
      
    result.append({
        "match_date": match_date,
        "match_timezone": match_timezone,
        "team_home": team_home,
        "team_away": team_away,
        "goals": rec["goals"]
    })
    
    return result
    
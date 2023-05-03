#your main api code goes on here 

#import the necessary Libraries
import random
import fastapi

#create your fastAPI app
app = fastapi.FastAPI()

#define the generate_name route with a custom status code response
@app.get("/generate_name", responses={404: {}})
async def generate_name(max_len: int = None, starts_with: str = None):#add arguments with types- pydantic
    names = ["Minnie", "Margaret", "Myrtle", "Noa", "Nadia"] #init a list of names
    # test one - if max_len given
    if max_len: 
        names = [name for name in names if len(name) <= max_len]
    # test two - if name starts with
    if starts_with:
        names = [name for name in names if name.startswith(starts_with)]
    #test three - if length of name is equal to zero return exception error
    if len(names) == 0:
        raise fastapi.HTTPException(status_code=404, detail='No matching names')
    
    #generate the name randomly
    random_name = random.choice(names)
    #return a dict with the name as the key and a random name given as a value
    return {"name": random_name}
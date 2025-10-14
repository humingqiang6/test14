from fastapi import FastAPI
import uuid
import os

app = FastAPI()

@app.post("/data/")
async def receive_data(item: dict):
    # Generate a random filename
    random_filename = f"received_data_{uuid.uuid4().hex}.py"
    
    # Save the received data to the file
    with open(random_filename, 'w') as f:
        f.write(f"data = {item!r}\n")
    
    return {"filename": random_filename, "message": "Data saved successfully"}
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    input_value = 7

    for i in range(len(array)):
        if array[i] == input_value:
            return {
                "message": "Element found",
                "index": i
            }

    return {"message": "Element not found"}
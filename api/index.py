from fastapi import FastAPI

app = FastAPI()

@app.get("/search/{value}")
def search(value: int):
    array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    for i in range(len(array)):
        if array[i] == value:
            return {
                "found": True,
                "index": i
            }

    return {
        "found": False,
        "message": "Element not found"
    }
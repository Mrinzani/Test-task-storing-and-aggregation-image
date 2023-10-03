from fastapi import FastAPI

app = FastAPI()


@app.get("/download_image/{id}")
def download_image(id: int):
    return ""


@app.get("/get_information/{id}")
def get_information(id: int):
    return ""


@app.delete("/delete_image/{id}")
def delete_image(id: int):
    return ""


@app.get("/get_information")
def get_all_information_image():
    return ""


@app.post("/upload_image/{image}")
def upload_image(image: str):
    return""

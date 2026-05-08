from fastapi import FastAPI
from fastapi.responses import FileResponse

server = FastAPI()

@server.get("/download/{package}")
async def download_file(package: str):
    #
    return FileResponse(
        path=f"resources/{package}",
        filename=f"{package}.zip",
        media_type="application/octet-stream"
    )
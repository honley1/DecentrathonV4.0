from fastapi import APIRouter, HTTPException
from fastapi.responses import HTMLResponse, FileResponse
import os

router = APIRouter()

@router.get("/")
async def root():
    return {"message": "Mapbox Traffic API"}

@router.get("/traffic", response_class=HTMLResponse)
async def get_traffic_map():
    """Serve the Mapbox traffic visualization"""
    file_path = os.path.join("files", "mapbox_traffic.html")
    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            return HTMLResponse(content=f.read(), status_code=200)
    return HTMLResponse(content="<h1>Traffic map not found</h1>", status_code=404)

@router.get("/files/{filename}")
async def get_file(filename: str):
    """Serve files from the files directory"""
    file_path = os.path.join("files", filename)
    if os.path.exists(file_path) and os.path.isfile(file_path):
        return FileResponse(file_path)
    return {"error": "File not found"}


# @router.get('/api', response_model=)
# async def sultan_huesos():
#     try:

#     except HTTPException:
#         raise
#     except Exception as e:
#         return {
#             "success": false,
#             "data": {
#                 "message": "Internal server error"
#             }
#         }
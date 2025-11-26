from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from typing import Optional, List
from fastapi.middleware.cors import CORSMiddleware
import os

from models import MobileAccessory, PaginatedResponse
from data import mobile_accessories

app = FastAPI(
    title="Mocom API", description="API for Mobile Accessories", version="1.0.0"
)

# Create static directory if it doesn't exist
STATIC_DIR = os.path.join(os.path.dirname(__file__), "static")
os.makedirs(STATIC_DIR, exist_ok=True)

# Mount static files
app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with your frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root() -> dict[str, str | List[str]]:
    return {
        "message": "Mobile Accessories API is running",
        "endpoints": ["/accessories", "/accessories/{id}"],
    }


@app.get("/accessories", response_model=PaginatedResponse)
def get_all_accessories(
    q: Optional[str] = None,
    max_price: Optional[int] = None,
    on_sale: Optional[bool] = None,
    page: int = 1,
    limit: int = 10,
):
    """Get all mobile accessories with optional search and filtering, with pagination"""
    if page < 1:
        raise HTTPException(status_code=400, detail="Page must be greater than 0")
    if limit < 1 or limit > 100:
        raise HTTPException(status_code=400, detail="Limit must be between 1 and 100")

    filtered_accessories = mobile_accessories

    # Apply search filter if query provided
    if q:
        filtered_accessories = [
            a
            for a in filtered_accessories
            if q.lower() in a.phone_model.lower() or q.lower() in a.name.lower()
        ]

    # Apply price filter if max_price provided
    if max_price is not None:
        filtered_accessories = [a for a in filtered_accessories if a.price <= max_price]

    # Apply sale status filter if on_sale provided
    if on_sale is not None:
        filtered_accessories = [a for a in filtered_accessories if a.on_sale == on_sale]

    start_idx = (page - 1) * limit
    end_idx = start_idx + limit

    return PaginatedResponse(
        data=filtered_accessories[start_idx:end_idx], total=len(filtered_accessories)
    )


@app.get("/accessories/{accessory_id}", response_model=MobileAccessory)
def get_accessory_by_id(accessory_id: int):
    """Get a specific mobile accessory by ID"""
    accessory = next((a for a in mobile_accessories if a.id == accessory_id), None)
    if accessory is None:
        raise HTTPException(status_code=404, detail="Mobile accessory not found")
    return accessory

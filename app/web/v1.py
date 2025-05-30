import logging

from fastapi import APIRouter


router = APIRouter(prefix="/ecommerce-backend/v1")

logger = logging.getLogger(__name__)


@router.get("/{item_id}")
def get_item(item_id):
    pass


@router.patch("/{item_id}")
def mofify_item(item_id, chamges):
    pass


@router.post("/item")
async def new_item(

):
    pass


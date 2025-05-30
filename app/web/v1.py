import logging

from fastapi import APIRouter, Depends

from app.model import EcomRequest, EcomResponse
from app.data import get_db
from app.service import create_item
from app.exceptions import EcommerceBackendException

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
    req: EcomRequest,
    db = Depends(get_db)
):
    try:
        return create_item(req, db)

    except Exception as e:
        raise EcommerceBackendException(f"Failed to staisfy request: {req}\n {e}")






from fastapi import APIRouter, Security
from application.utils import VerifyToken

router = APIRouter()
auth = VerifyToken()

@router.get("/api/public")
def public():
    """No access token required to access this route"""

    result = {
        "status": "success",
        "msg": (
            "Hello from a public endpoint! You don't need to be "
            "authenticated to see this."
        ),
    }
    return result

@router.get("/api/private")
def private(auth_result: str = Security(auth.verify)):
    """A valid access token is required to access this route"""
    return {"text": "Hello World from the protected API"}
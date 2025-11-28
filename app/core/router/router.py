from fastapi import APIRouter


def get_versioned_router(version: str):
    """get versioned router

    Args:
        version (str): _description_

    Return:
        ApiRouter: Versioned router
    """
    return APIRouter(prefix=f"/{version}")

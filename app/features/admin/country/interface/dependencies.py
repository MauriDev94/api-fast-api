from typing import Annotated
from fastapi import Depends
from sqlalchemy.orm import Session

from app.core.providers.db import get_db_session
from app.features.admin.country.application.country_service import CountryService
from app.features.admin.country.application.interface.icountry_repository import (
    ICountryRepository,
)
from app.features.admin.country.infrastructure.repositories.country_repository import (
    CountryRepository,
)


def get_country_repository(
    db_session: Annotated[Session, Depends(get_db_session)],
) -> ICountryRepository:
    """Get Country

    Args:
        db_session (Annotated[Session, Depends(get_db_session)]): database session

    Returns:
        ICountryRepository: Country repository
    """
    return CountryRepository(session=db_session)


def get_country_service(
    country_repository: Annotated[ICountryRepository, Depends(get_country_repository)],
) -> CountryService:
    """Get a country service

    Args:
        country_repository (Annotated(ICountryRepository, Depends(get_country_repository)]): Country repository

    Returns:
        CountryService: Country service
    """
    return CountryService(repository=country_repository)

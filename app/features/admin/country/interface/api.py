from typing import Annotated

from fastapi import Depends, status
from app.core.router.router import get_versioned_router
from app.features.admin.country.application.country_service import CountryService
from app.features.admin.country.domain.country_entity import CountryEntity
from app.features.admin.country.interface.dependencies import get_country_service
from app.features.admin.country.interface.schemas import (
    CountryListResponse,
    CountryResponse,
)


v1_router = get_versioned_router("v1")


@v1_router.get("/admin/countries", status_code=status.HTTP_200_OK)
def get_countries(
    country_service: Annotated[CountryService, Depends(get_country_service)],
) -> CountryListResponse:
    # Call the service method to get the countries
    result = country_service.get_all_countries()
    # Return CountryListResponse(status="success", data=result)
    return CountryListResponse(status="success", data=result)


@v1_router.get("/admin/countries/{country_id}", status_code=status.HTTP_200_OK)
def get_country_by_id(
    country_id: int,
    country_service: Annotated[CountryService, Depends(get_country_service)],
) -> CountryResponse:
    # Call the service method to get the country by his id
    result = country_service.get_country_by_id(country_id)
    # Return CountryResponse(status="success", data=result)
    return CountryResponse(status="success", data=result)


@v1_router.post("/admin/countries", status_code=status.HTTP_201_CREATED)
def create_country(
    data: CountryEntity,
    country_service: Annotated[CountryService, Depends(get_country_service)],
) -> CountryResponse:
    # Call the service method to create a country
    result = country_service.create_country(data)
    # return CountryResponse(status="succes", data=result)
    return CountryResponse(status="success", data=result)


@v1_router.patch("/admin/country/{country_id}", status_code=status.HTTP_200_OK)
def patch_country(
    country_id: int,
    data: CountryEntity,
    country_service: Annotated[CountryService, Depends(get_country_service)],
) -> CountryResponse:
    # Call the service method to patch a country
    result = country_service.update_country(country_id, data)
    # return CountryResponse(status="succes", data=result)
    return CountryResponse(status="success", data=result)


@v1_router.delete("/admin/country/{country_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_country(
    country_id: int,
    data: CountryEntity,
    country_service: Annotated[CountryService, Depends(get_country_service)],
) -> None:
    # Call the service method to delete a country
    result = country_service.delete_country(country_id, data)
    # Return CountryResponse(status="succes", data=result
    # return CountryResponse(status="succes", data=result)

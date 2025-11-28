from sqlalchemy.orm.session import Session
from typing_extensions import override
from sqlalchemy import update

from app.features.admin.country.domain.country_entity import CountryEntity
from app.features.admin.country.infrastructure.models.country_model import CountryModel
from app.features.admin.country.application.interface.icountry_repository import (
    ICountryRepository,
)
from app.features.admin.country.infrastructure.mappers.map_country_entity_to_model import (
    map_country_entity_to_model,
)
from app.features.admin.country.infrastructure.mappers.map_country_model_to_entity import (
    map_country_model_to_entity,
)


class CountryRepository(ICountryRepository):

    def __init__(self, session: Session):
        self.session: Session = session

    # ----------------------------------------------------
    @override
    def get_all_countries(self) -> list[CountryEntity]:
        """
        Get all countries

        Returns:
            list[CountryEntity]: List of CountryEntity objects
        """
        countries = self.session.query(CountryModel).all()
        # Map CountryModel to CountryEntity
        result = [map_country_model_to_entity(country) for country in countries]
        # Return list of country entities
        return result

    # ----------------------------------------------------
    @override
    def get_country_by_id(self, country_id: int) -> CountryEntity:
        """
        Get Country by ID

        Args:
            country_id (int): country id

        Returns:
            CountryEntity: Country Entity

        Raises:
            ValueError: If country not found
        """
        result = (
            self.session.query(CountryModel)
            .filter(CountryModel.id == country_id)
            .first()
        )
        return map_country_model_to_entity(result)

    # ----------------------------------------------------
    @override
    def create_country(self, country: CountryEntity) -> CountryEntity:
        """
        Create a new Country

        Args:
            country (Country): Country Entity

        Returns:
            CountryEntity: Country Entity
        """
        # Map Country entity to Country model
        country_model = map_country_entity_to_model(country)
        # Add country model to session
        self.session.add(country_model)
        # Commit session
        self.session.commit()
        self.session.refresh(country_model)
        # Map country model to country entity and return
        return map_country_model_to_entity(country_model)

    # ----------------------------------------------------
    @override
    def update_country(self, country_id: int, country: CountryEntity) -> CountryEntity:
        """
        Update a Country

        Args:
            country_id (int): Country ID
            country (CountryEntity): Country Entity

        Returns:
            CountryEntity: Country Entity
        """

        # Get country by id
        country_model = (
            self.session.query(CountryModel)
            .filter(CountryModel.id == country_id)
            .first()
        )
        # TODO: raise exception if country not found

        # Map country entity to country model
        country_model = map_country_entity_to_model(country)
        # update country model
        self.session.update(country_model)
        # Commit session
        self.session.commit()
        # Map country model to country entity and return
        return map_country_model_to_entity(country_model)

    # ----------------------------------------------------
    @override
    def delete_country(self, country_id: int) -> bool:
        """
        Delete a Country

        Args:
            country_id (int): Country ID
        """
        # Get country by id
        country_model = (
            self.session.query(CountryModel)
            .filter(CountryModel.id == country_id)
            .first()
        )
        # TODO: raise exception if country not found

        # Delete country model
        self.session.delete(country_model)
        # Commit session
        self.session.commit()
        return True

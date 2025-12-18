import math
from typing_extensions import override
from sqlalchemy import func
from sqlalchemy.orm.session import Session
from sqlalchemy.exc import OperationalError, SQLAlchemyError, IntegrityError

from app.core.exceptions.repository import (
    ConnectionFailure,
    RepositoryException,
    TransactionFailure,
    UniqueConstraintFailure,
)
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
    def get_all_countries(
        self, skip: int, limit: int
    ) -> tuple[list[CountryEntity], int, int]:
        try:
            """
            Get all countries

            Returns:
                list[CountryEntity]: List of CountryEntity objects
            """
            countries = self.session.query(CountryModel).offset(skip).limit(limit).all()
            # count all the record by id
            total = self.session.query(func.count(CountryModel.id)).scalar() or 0
            # total pages
            total_pages = math.ceil(total / limit) if limit > 0 else 1
            # Map CountryModel to CountryEntity
            result = [map_country_model_to_entity(country) for country in countries]
            # Return list of country entities
            return result, total, total_pages
        except OperationalError as e:
            raise ConnectionFailure() from e
        except SQLAlchemyError as e:
            raise TransactionFailure() from e
        except Exception as e:
            raise RepositoryException() from e

    # ----------------------------------------------------
    @override
    def get_country_by_id(self, country_id: int) -> CountryEntity:
        try:
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
        except OperationalError as e:
            raise ConnectionFailure() from e
        except SQLAlchemyError as e:
            raise TransactionFailure() from e
        except Exception as e:
            raise RepositoryException() from e

    # ----------------------------------------------------
    @override
    def create_country(self, country: CountryEntity) -> CountryEntity:
        try:
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
        except IntegrityError as e:
            self.session.rollback()
            raise UniqueConstraintFailure() from e
        except OperationalError as e:
            raise ConnectionFailure() from e
        except SQLAlchemyError as e:
            raise TransactionFailure() from e
        except Exception as e:
            raise RepositoryException() from e

    # ----------------------------------------------------
    @override
    def update_country(self, country_id: int, country: CountryEntity) -> CountryEntity:
        try:
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
            country_model = map_country_entity_to_model(country, country_model)
            # Commit session
            self.session.commit()
            # Map country model to country entity and return
            return map_country_model_to_entity(country_model)
        except IntegrityError as e:
            self.session.rollback()
            raise UniqueConstraintFailure() from e
        except OperationalError as e:
            raise ConnectionFailure() from e
        except SQLAlchemyError as e:
            raise TransactionFailure() from e
        except Exception as e:
            raise RepositoryException() from e

    # ----------------------------------------------------
    @override
    def delete_country(self, country_id: int) -> bool:
        try:
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
        except OperationalError as e:
            raise ConnectionFailure() from e
        except SQLAlchemyError as e:
            raise TransactionFailure() from e
        except Exception as e:
            raise RepositoryException() from e

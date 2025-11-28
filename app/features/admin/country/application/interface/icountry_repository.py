from abc import ABC, abstractmethod

from app.features.admin.country.domain.country_entity import CountryEntity


class ICountryRepository(ABC):
    """
    Interface for Country Repository
    """

    @abstractmethod
    def get_all_countries(self) -> list[CountryEntity]:
        """
        Get all countries
        """
        pass

    @abstractmethod
    def get_country_by_id(self, country_id: int) -> CountryEntity:
        """
        Get Country by ID
        """
        pass

    @abstractmethod
    def create_country(self, country: CountryEntity) -> CountryEntity:
        """
        Create a new Country
        """
        pass

    @abstractmethod
    def update_country(self, country_id: int, country: CountryEntity) -> CountryEntity:
        """
        Update a Country
        """
        pass

    @abstractmethod
    def delete_country(self, country_id: int) -> bool:
        """
        Delete a Country
        """
        pass

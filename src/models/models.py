from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import Integer, String, ForeignKey



class Base(DeclarativeBase):
    """
    Базовый класс для всех моделей.
    Все модели должны наследоваться от этого класса.
    """
    pass

class CountryModel(Base):
    """
    Модель для таблицы "country".
    Хранит информацию о странах..
    Модель имеет связь с городами (CityModel) указывая какие города принадлежат каждой стране
    """
    __tablename__ = "country"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String)
    iata: Mapped[str] = mapped_column(String)

    # Связь с моделью "CityModel"
    city: Mapped["CityModel"] = relationship("CityModel", back_populates="country")

class CityModel(Base):
    """
        Модель для таблицы "city".
        Хранит информацию о городах.
        Связана с таблицей CountryModel через country_id
        """
    __tablename__ = "city"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    country_id: Mapped[int] = mapped_column(ForeignKey("country.id")) # Внешний ключ на таблицу "country"
    name: Mapped[str] = mapped_column(String)
    iata: Mapped[str] = mapped_column(String)

    # Связь с моделью "CountryModel"
    country: Mapped["CountryModel"] = relationship("CountryModel", back_populates="city")

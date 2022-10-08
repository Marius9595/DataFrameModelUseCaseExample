from typing import List

from DataFrameModel.dataframe_model import DataFrameModel
from pandera import Column


class PeninsularData(DataFrameModel):
    col_date = Column(name='date', dtype=str)
    col_demand = Column(name='demand', dtype=float)
    col_nuclear = Column(name='nuclear', dtype=float)
    col_hydro = Column(name='hydro', dtype=float)
    col_solar_pv = Column(name='solar_pv', dtype=float)
    col_solar_thermal = Column(name='solar_thermal', dtype=float)
    col_wind_turbines = Column(name='wind_turbines', dtype=float)
    col_thermal_renewable = Column(name='thermal_renewable', dtype=float)
    col_cogeneration_and_waste = Column(name='cogeneration_and_waste', dtype=float)
    col_fuel_gas = Column(name='fuel_gas', dtype=float)
    col_coal = Column(name='coal', dtype=float)
    col_combined_cycle = Column(name='combined_cycle', dtype=float)
    col_international_interchanges = Column(name='international_interchanges', dtype=float)
    col_balear_link = Column(name='balear_link', dtype=float)
    col_auxiliar_generation = Column(name='auxiliar_generation', dtype=float)

    def conventionals(self) -> List[str]:
        return [
            self.col_coal.name, self.col_combined_cycle.name,
            self.col_fuel_gas.name, self.col_nuclear.name,
            self.col_auxiliar_generation.name
        ]

    def renewables(self) -> List[str]:
        return [
            self.col_solar_thermal.name, self.col_solar_pv.name,
            self.col_thermal_renewable.name, self.col_wind_turbines.name,
            self.col_cogeneration_and_waste.name, self.col_hydro.name
        ]

    def zero_emissions(self)->List[str]:
        return self.renewables() + [self.col_hydro.name, self.col_nuclear.name]

    def interchanges(self) -> List[str]:
        return [self.col_balear_link.name, self.col_international_interchanges.name]
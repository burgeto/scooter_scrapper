from providers.provider import Provider, ScooterPositionLog
import requests
import json
import logging
import uuid


class Hive(Provider):
    provider = "hive"
    _base_url = "https://hive.frontend.fleetbird.eu/api/prod/v1.06/map/cars/"

    def get_scooters(self):
        r = requests.get(self._base_url)
        spls = []
        if r.status_code == 200:
            scooters = r.json()
            for scooter in scooters:
                spls.append(ScooterPositionLog(
                    provider=self.provider,
                    vehicle_id=scooter["carId"],
                    licence_plate=scooter["licencePlate"],
                    city=str.lower(scooter["city"]),
                    lat=scooter["lat"],
                    lng=scooter["lon"],
                    battery_level=scooter["fuelLevel"],
                    raw_data=scooter
                ))
        else:
            logging.warning(f"{r.status_code} received from {self.provider}, body: {r.content}")
        return spls





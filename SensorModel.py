import obd



connection = ""

def initConnection():
    global connection
    connection = obd.OBD()

def sample_sensor_values():
     # auto-connects to available OBD-II adapter
    global connection
    sensors = {
        'oil_pressure': obd.commands.FUEL_PRESSURE,
        'oil_temperature': obd.commands.OIL_TEMP,
        'water_temperature': obd.commands.COOLANT_TEMP,
        'speed': obd.commands.SPEED,
        'rpm': obd.commands.RPM,
        'fuel_level': obd.commands.FUEL_LEVEL,
        'battery_volts': obd.commands.ELM_VOLTAGE,
        'air_fuel_ratio': obd.commands.MAF,
        'selected_gear': obd.commands.TIMING_ADVANCE  # Note: Not all vehicles support this
    }

    sensor_values = {}

    for sensor, command in sensors.items():
        response = connection.query(command)
        if response.is_null():  # Checking if the response is valid
            sensor_values[sensor] = None
        else:
            sensor_values[sensor] = response.value

    return sensor_values


class SensorModel:
    oil_pressure = 0.0
    oil_temperature = 0.0
    water_temperature = 0.0
    speed = 0.0
    rpm = 0.0
    uel_level = 0.0
    battery_volts = 0.0
    air_fuel_ratio = 0.0
    selected_gear = 0.0

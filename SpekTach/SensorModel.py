import obd



connection = ""

def initConnection():
    global connection
    connection = obd.OBD()
    obd.logger.removeHandler(obd.console_handler)

def sample_fast_sensor_values():
     # auto-connects to available OBD-II adapter
    global connection
    sensors = {

        'rpm': obd.commands.RPM,
        'timing_advance': obd.commands.TIMING_ADVANCE  # Note: Not all vehicles support this
    }

    sensor_values = {}

    for sensor, command in sensors.items():
        response = connection.query(command)
        if response.is_null():  # Checking if the response is valid
            sensor_values[sensor] = None
        else:
            if sensor == 'water_temperature':
                sensor_values[sensor] = response.value.to('degF')
            else:
                sensor_values[sensor] = response.value

    return sensor_values

def sampleMedSensorValues():
    sensors = {
        'battery_volts': obd.commands.ELM_VOLTAGE
    }
    sensor_values = {}
    for sensor, command in sensors.items():
        response = connection.query(command)
        if response.is_null():  # Checking if the response is valid
            sensor_values[sensor] = None
        else:
            if sensor == 'water_temperature':
                sensor_values[sensor] = response.value.to('degF')
            else:
                sensor_values[sensor] = response.value

    return sensor_values
def sampleSlowSensorValues():
    sensors = {
        'water_temperature': obd.commands.COOLANT_TEMP,
        'fuel_level': obd.commands.FUEL_LEVEL,
    }
    sensor_values = {}
    for sensor, command in sensors.items():
        response = connection.query(command)
        if response.is_null():  # Checking if the response is valid
            sensor_values[sensor] = None
        else:
            if sensor == 'water_temperature':
                sensor_values[sensor] = response.value.to('degF')
            else:
                sensor_values[sensor] = response.value

    return sensor_values

def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit
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

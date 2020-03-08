
light_entity_id = data.get("light_entity_id")
duration = float(data.get("duration"))
max_brightness = int(data.get("max_brightness"))

BRIGHTNESS_INCREMENT = 1

# Increase brightness by one step at a time (Brightness: int 0..255)
# Calculate dwell time in seconds from max_brightness and duration
dwell_time = 60.0 * duration / (float(max_brightness) / BRIGHTNESS_INCREMENT)

current_brightness = 0
while current_brightness < max_brightness:
    current_brightness = current_brightness + BRIGHTNESS_INCREMENT
    logger.info("Setting {} brightness to {}.".format(light_entity_id, current_brightness))
    data = {
        "entity_id": light_entity_id,
        "brightness": current_brightness
    }
    hass.services.call("light", "turn_on", data)
    time.sleep(dwell_time)


speaker_entity_id = data.get("speaker_entity_id")
speaker_friendly_name = data.get("speaker_friendly_name")
spotify_uri = data.get("spotify_uri")
duration = float(data.get("duration"))
max_volume = float(data.get("max_volume"))

VOLUME_INCREMENT = 0.01
SILENT_TRACK_URI = "spotify:track:5XSKC4d0y0DfcGbvDOiL93"

# Play silent track and then mute
data = {
    "device_name": speaker_friendly_name,
    "uri": SILENT_TRACK_URI
}
hass.services.call("spotcast", "start", data)
# Mute
data = {
    "entity_id": speaker_entity_id,
    "volume_level": 0
}
hass.services.call("media_player", "volume_set", data)

time.sleep(3)

# Play actual playlist
data = {
    "device_name": speaker_friendly_name,
    "uri": spotify_uri,
    "random_song": True,
    "shuffle": True
}
hass.services.call("spotcast", "start", data)

# Increase volume by 0.01 at a time (Volume: float 0..1)
# Calculate dwell time in seconds from max_volume and duration
dwell_time = 60.0 * duration / (max_volume / VOLUME_INCREMENT)

current_volume = 0
while current_volume < max_volume:
    current_volume = current_volume + VOLUME_INCREMENT
    logger.info("Setting {} volume to {}.".format(speaker_entity_id, current_volume))
    data = {
        "entity_id": speaker_entity_id,
        "volume_level": current_volume
    }
    hass.services.call("media_player", "volume_set", data)
    time.sleep(dwell_time)

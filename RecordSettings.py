from dataclasses import dataclass

# TODO: Offload this part to a different service and pass in speed factor and res directly as cli arguments

@dataclass
class RecordSettings:
    clan_name: str
    date: str
    speed_factor: int
    resolution: str
    day: int | None

tier_to_settings = {
    1 : {
        "speed_factor" : 4,
        "resolution" : "720p"
    },
    2 : {
        "speed_factor" : 2,
        "resolution" : "1080p"
    },
    3 : {
        "speed_factor" : 2,
        "resolution" : "1440p"
    },
    4 : {
        "speed_factor" : 1,
        "resolution" : "1440p"
    },
    5 : {
        "speed_factor" : 1,
        "resolution" : "1440p"
    },
}

def get_settings(clan_name: str, date: str, tier: int, day: int | None = None):
    return RecordSettings(
        clan_name=clan_name,
        date=date,
        **tier_to_settings[tier],
        day=day
    )
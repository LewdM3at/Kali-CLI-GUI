menu_structure = \
{
    "main": 
    {
        "title": "Main Menu",
        "items": ["wifi", "settings", "exit"],
        "parent": None,   # root has no parent
    },
    "wifi": 
    {
        "title": "WiFi Attacks",
        "items": ["auto_audit", "pmkid", "handshake", "pixie", "pin", "back"],
        "parent": "main", # back goes here
    },
    "settings": 
    {
        "title": "Settings",
        "items": ["wifi_settings", "back"],
        "parent": "main", # back goes here
    },
}
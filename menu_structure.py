menu_structure = \
{
    "main": 
    {
        "title": "Main Menu",
        "items": ["wifi", "exit"],
        "parent": None,   # root has no parent
    },
    "wifi": 
    {
        "title": "WiFi Attacks",
        "items": ["auto_audit", "pmkid", "handshake", "pixie", "pin", "back"],
        "parent": "main", # back goes here
    },
}
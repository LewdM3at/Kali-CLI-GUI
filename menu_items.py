import ascii_art
import actions

def wifi_toggle_action(stdscr):
    actions.toggle_wifi()

def get_wifi_art():
    return ascii_art.wifi_art if actions.is_wifi_up() else ascii_art.wifi_off_art

menu_items = \
{
    "wifi":
    {
        "label": "Wi-Fi",
        "art": ascii_art.wifi_art,
        "submenu": "wifi",
    },
    "exit":
    {
        "label": "Exit",
        "art": ascii_art.exit_art,
        "action": actions.exit_menu,
    },
    "auto_audit":
    {
        "label": "Automatic Auditing",
        "art": ascii_art.auto_audit_art,
        "action": actions.auto_audit_attack,
    },
    "pmkid":
    {
        "label": "PMKID Attack",
        "art": ascii_art.PMKID_art,
        "action": actions.pmkid_attack,
    },
    "handshake":
    {
        "label": "Handshake Capture",
        "art": ascii_art.handshake_art,
        "action": actions.handshake_attack,
    },
    "pixie":
    {
        "label": "PixieDust Attack",
        "art": ascii_art.pixie_art,
        "action": actions.pixiedust_attack,
    },
    "pin":
    {
        "label": "WPS PIN Attack",
        "art": ascii_art.PIN_art,
        "action": actions.pin_attack,
    },
    "back":
    {
        "label": "Back",
        "art": ascii_art.back_art,
    },
    "settings":
    {
        "label": "Settings",
        "art": ascii_art.settings_art,
    },
    "wifi_settings":
    {
        "label": "Wi-Fi",
        "art": get_wifi_art,
        "action": wifi_toggle_action,
    },
}
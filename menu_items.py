import ascii_art
import actions

menu_items = \
{
    "wifi":
    {
        "label": "WiFi Attacks",
        "art": ascii_art.wifi_art,
    },
    "exit":
    {
        "label": "Exit",
        "art": ascii_art.exit_art,
        "action": actions.exit_menu,
    },
    "pmkid":
    {
        "label": "PMKID Attack",
        "art": ascii_art.PMKID_art,
        "action": actions.pmkid_attack,
    },
    "back":
    {
        "label": "Back",
        "art": ascii_art.back_art,
    },
}
# List of source URLs to fetch proxy configurations from.
SOURCE_URLS = [
    "https://raw.githubusercontent.com/Rayan-Config/C-Sub/refs/heads/main/configs/proxy.txt",
    "https://raw.githubusercontent.com/DiDiten/HiN-VPN/main/subscription/normal/mix",
    "https://raw.githubusercontent.com/Epodonios/v2ray-configs/refs/heads/main/All_Configs_Sub.txt",
    "https://raw.githubusercontent.com/MatinGhanbari/v2ray-configs/refs/heads/main/subscriptions/v2ray/all_sub.txt",
    "https://raw.githubusercontent.com/mahdibland/V2RayAggregator/refs/heads/master/Eternity.txt",
    "https://dev1.irdevs.sbs",
    "https://raw.githubusercontent.com/DarknessShade/Sub/main/V2mix",
    "https://raw.githubusercontent.com/arshiacomplus/v2rayExtractor/refs/heads/main/mix/sub.html",
    "https://raw.githubusercontent.com/lagzian/SS-Collector/refs/heads/main/SS/TrinityBase",
    "https://raw.githubusercontent.com/hamedcode/port-based-v2ray-configs/refs/heads/main/sub/vless.txt",
    "https://raw.githubusercontent.com/nscl5/5/refs/heads/main/configs/all.txt",
    "https://raw.githubusercontent.com/roosterkid/openproxylist/refs/heads/main/V2RAY_RAW.txt",
    "https://raw.githubusercontent.com/Freedom-Guard-Builder/Freedom-Finder/refs/heads/main/out/mixed_configs.txt",

"https://t.me/s/v2ray_Extractor",
"https://t.me/s/BINNER_IRAN",
"https://t.me/s/DeamNet",
"https://t.me/s/AzadNet",
"https://t.me/s/freeconfigsplus",
"https://t.me/s/configshubplus",
"https://t.me/s/ConfigWireguard",
"https://t.me/s/WireVpnGuard",
"https://t.me/s/Config_Vortex55",
"https://t.me/s/configshubplus",
"https://t.me/s/APPXA",
"https://t.me/s/arshia_mod_fun",
"https://t.me/s/lightning6",
"https://t.me/s/spotify_porteghali",
"https://t.me/s/kvetch_matin",
"https://t.me/s/hacknashid",
"https://t.me/s/lnrbymaa",
"https://t.me/s/lyricpixelart",
"https://t.me/s/madshopx",
"https://t.me/s/movie10_oficial",
"https://t.me/s/mbtiuniverse",
"https://t.me/s/mitivpn",
"https://t.me/s/mrsoulb",
"https://t.me/s/prooofsor",
"https://t.me/s/soskeynet",
"https://t.me/s/speeds_vpn1",
"https://t.me/s/surfboardv2ray",
"https://t.me/s/v2ray1_ng",
"https://t.me/s/v2ray_vpn_ir",
"https://t.me/s/vless_config",
"https://t.me/s/vlessconfight",
"https://t.me/s/vpn4everyone",
"https://t.me/s/vpnbaz",
"https://t.me/s/vpnserverrr",
"https://t.me/s/vpn_solve",
"https://t.me/s/xixv2ray",
"https://t.me/s/ahwazigamingshop",
"https://t.me/s/ar14n24b",
"https://t.me/s/betv2ray",
"https://t.me/s/bugfreenet",
"https://t.me/s/capoit",
"https://t.me/s/canfing_vpn",
"https://t.me/s/configfa",
"https://t.me/s/configshubplus",
"https://t.me/s/configx2ray",
"https://t.me/s/crypto_trad26",
"https://t.me/s/express_freevpn",
"https://t.me/s/gp_config",
"https://t.me/s/lrnbymaa",
"https://t.me/s/mrsoulb",
"https://t.me/s/proxy_confiig",
"https://t.me/s/proxyiranip",
"https://t.me/s/club_profsor",
"https://t.me/s/shadowproxy66",
"https://t.me/s/soskeynet",
"https://t.me/s/speeds_vpn1",
"https://t.me/s/vless_config",
"https://t.me/s/vpn_solve",
"https://t.me/s/vpnbaz"
]

# Set to True to fetch the maximum possible number of configurations.
# If True, SPECIFIC_CONFIG_COUNT will be ignored.
USE_MAXIMUM_POWER = False

# Desired number of configurations to fetch.
# This is used only if USE_MAXIMUM_POWER is False.
SPECIFIC_CONFIG_COUNT = 800

# Dictionary of protocols to enable or disable.
# Set each protocol to True to enable, False to disable.
ENABLED_PROTOCOLS = {
    "wireguard://": True,
    "hysteria2://": True,
    "vless://": True,
    "vmess://": True,
    "ss://": True,
    "trojan://": True,
    "tuic://": False,
}

# Maximum age of configurations in days.
# Configurations older than this will be considered invalid.
MAX_CONFIG_AGE_DAYS = 2

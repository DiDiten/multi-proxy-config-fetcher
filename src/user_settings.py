# Please modify the settings below according to your needs.

# List of source URLs to fetch proxy configurations from.
# Add or remove URLs as needed. All URLs in this list are automatically enabled.
SOURCE_URLS = [
        "https://raw.githubusercontent.com/4n0nymou3/ss-config-updater/refs/heads/main/configs.txt",
    "https://raw.githubusercontent.com/4n0nymou3/wg-config-fetcher/refs/heads/main/configs/wireguard_configs.txt",
    "https://raw.githubusercontent.com/mahsanet/MahsaFreeConfig/refs/heads/main/mci/sub_1.txt",
    "https://raw.githubusercontent.com/mahsanet/MahsaFreeConfig/refs/heads/main/mci/sub_2.txt",
    "https://raw.githubusercontent.com/mahsanet/MahsaFreeConfig/refs/heads/main/mci/sub_3.txt",
    "https://raw.githubusercontent.com/mahsanet/MahsaFreeConfig/refs/heads/main/mci/sub_4.txt",
    "https://raw.githubusercontent.com/mahsanet/MahsaFreeConfig/refs/heads/main/mtn/sub_1.txt",
    "https://raw.githubusercontent.com/mahsanet/MahsaFreeConfig/refs/heads/main/mtn/sub_2.txt",
    "https://raw.githubusercontent.com/mahsanet/MahsaFreeConfig/refs/heads/main/mtn/sub_3.txt",
    "https://raw.githubusercontent.com/mahsanet/MahsaFreeConfig/refs/heads/main/mtn/sub_4.txt",

"https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/countries/ir/mixed",
    

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
"https://t.me/s/prooofsor",
"https://t.me/s/shadowproxy66",
"https://t.me/s/soskeynet",
"https://t.me/s/speeds_vpn1",
"https://t.me/s/vless_config",
"https://t.me/s/vpn_solve",
"https://t.me/s/vpnbaz"
    # Add more URLs here if you want to include additional sources.
]

# Set to True to fetch the maximum possible number of configurations.
# If True, SPECIFIC_CONFIG_COUNT will be ignored.
USE_MAXIMUM_POWER = True

# Desired number of configurations to fetch.
# This is used only if USE_MAXIMUM_POWER is False.
SPECIFIC_CONFIG_COUNT = 500

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

import json
import base64
import uuid
import time
import socket
import requests
from typing import Dict, Optional, Tuple
from urllib.parse import urlparse, parse_qs
from collections import defaultdict

class ConfigToSingbox:
    def __init__(self):
        self.output_file = 'configs/singbox_configs.json'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        
    def get_location_from_ip_api(self, ip: str) -> Tuple[str, str]:
        try:
            response = requests.get(f'http://ip-api.com/json/{ip}', headers=self.headers, timeout=5)
            if response.status_code == 200:
                data = response.json()
                if data.get('status') == 'success' and data.get('countryCode'):
                    return data['countryCode'].lower(), data['country']
        except Exception:
            pass
        return '', ''

    def get_location_from_ipapi_co(self, ip: str) -> Tuple[str, str]:
        try:
            response = requests.get(f'https://ipapi.co/{ip}/json/', headers=self.headers, timeout=5)
            if response.status_code == 200:
                data = response.json()
                if data.get('country_code') and data.get('country_name'):
                    return data['country_code'].lower(), data['country_name']
        except Exception:
            pass
        return '', ''

    def get_location(self, address: str) -> tuple:
        try:
            ip = socket.gethostbyname(address)
            # For speed, we can just use one or two reliable APIs
            apis = [
                self.get_location_from_ip_api,
                self.get_location_from_ipapi_co,
            ]
            
            for api_func in apis:
                country_code, country = api_func(ip)
                if country_code and country and len(country_code) == 2:
                    flag = ''.join(chr(ord('🇦') + ord(c.upper()) - ord('A')) for c in country_code)
                    time.sleep(1) # Respect API rate limits
                    return flag, country
                time.sleep(1) # Respect API rate limits
                
        except Exception:
            pass
            
        return "🏳️", "Unknown"

    def decode_vmess(self, config: str) -> Optional[Dict]:
        try:
            encoded = config.replace('vmess://', '')
            decoded = base64.b64decode(encoded).decode('utf-8')
            return json.loads(decoded)
        except Exception:
            return None

    def parse_vless(self, config: str) -> Optional[Dict]:
        try:
            url = urlparse(config)
            if url.scheme.lower() != 'vless' or not url.hostname:
                return None
            netloc = url.netloc.split('@')[-1]
            address, port = netloc.split(':') if ':' in netloc else (netloc, '443')
            params = parse_qs(url.query)
            return {
                'uuid': url.username,
                'address': address,
                'port': int(port),
                'flow': params.get('flow', [''])[0],
                'sni': params.get('sni', [address])[0],
                'type': params.get('type', ['tcp'])[0],
                'path': params.get('path', ['/'])[0],
                'host': params.get('host', [''])[0]
            }
        except Exception:
            return None

    def parse_trojan(self, config: str) -> Optional[Dict]:
        try:
            url = urlparse(config)
            if url.scheme.lower() != 'trojan' or not url.hostname:
                return None
            port = url.port or 443
            params = parse_qs(url.query)
            return {
                'password': url.username,
                'address': url.hostname,
                'port': port,
                'sni': params.get('sni', [url.hostname])[0],
                'alpn': params.get('alpn', [''])[0],
                'type': params.get('type', ['tcp'])[0],
                'path': params.get('path', ['/'])[0]
            }
        except Exception:
            return None

    def parse_hysteria2(self, config: str) -> Optional[Dict]:
        try:
            url = urlparse(config)
            if url.scheme.lower() not in ['hysteria2', 'hy2'] or not url.hostname or not url.port:
                return None
            query = parse_qs(url.query)
            return {
                'address': url.hostname,
                'port': url.port,
                'password': url.username or query.get('password', [''])[0],
                'sni': query.get('sni', [url.hostname])[0]
            }
        except Exception:
            return None

    def parse_shadowsocks(self, config: str) -> Optional[Dict]:
        try:
            url = urlparse(config)
            if url.scheme.lower() != 'ss': return None
            
            if '@' in url.netloc:
                user_info, host_port = url.netloc.split('@', 1)
                user_info_decoded = base64.urlsafe_b64decode(user_info + '===').decode('utf-8')
            else:
                encoded_part = config.split('://')[1].split('@')[0]
                user_info_decoded = base64.urlsafe_b64decode(encoded_part + '===').decode('utf-8')
                host_port = config.split('@')[1].split('#')[0]

            method, password = user_info_decoded.split(':', 1)
            host, port = host_port.rsplit(':', 1)

            return { 'method': method, 'password': password, 'address': host, 'port': int(port) }
        except Exception:
            return None

    def convert_to_singbox(self, config: str) -> Optional[Dict]:
        try:
            config_lower = config.lower()
            if config_lower.startswith('vmess://'):
                vmess_data = self.decode_vmess(config)
                if not vmess_data: return None
                
                flag, country = self.get_location(vmess_data['add'])
                tag = f"{flag} {country} - VMess"
                
                tls_settings = { "enabled": vmess_data.get('tls') == 'tls' }
                if tls_settings["enabled"]:
                    tls_settings["server_name"] = vmess_data.get('sni') or vmess_data.get('host') or vmess_data['add']
                    tls_settings["insecure"] = True

                transport = {}
                net_type = vmess_data.get('net', 'tcp')
                if net_type in ['ws', 'h2']:
                    transport["type"] = net_type
                    transport["path"] = vmess_data.get('path', '/')
                    if vmess_data.get('host'):
                        transport["headers"] = {"Host": vmess_data['host']}

                return {
                    "type": "vmess", "tag": tag, "server": vmess_data['add'],
                    "server_port": int(vmess_data['port']), "uuid": vmess_data['id'],
                    "security": vmess_data.get('scy', 'auto'), "alter_id": int(vmess_data.get('aid', 0)),
                    "tls": tls_settings, "transport": transport if transport else None
                }
            elif config_lower.startswith('vless://'):
                vless_data = self.parse_vless(config)
                if not vless_data: return None
                
                flag, country = self.get_location(vless_data['address'])
                tag = f"{flag} {country} - VLess"
                
                transport = {}
                if vless_data['type'] == 'ws':
                    transport["type"] = "ws"
                    transport["path"] = vless_data.get('path')
                    if vless_data.get('host'):
                        transport["headers"] = {"Host": vless_data['host']}

                return {
                    "type": "vless", "tag": tag, "server": vless_data['address'],
                    "server_port": vless_data['port'], "uuid": vless_data['uuid'],
                    "flow": vless_data['flow'], "tls": { "enabled": True, "server_name": vless_data['sni'], "insecure": True },
                    "transport": transport if transport else None
                }

            return None
        except Exception:
            return None

    def process_configs(self):
        try:
            with open('configs/proxy_configs.txt', 'r', encoding='utf-8') as f:
                configs = f.read().strip().split('\n')

            individual_outbounds = []
            for config in configs:
                config = config.strip()
                if not config or config.startswith(('#', '//')):
                    continue
                converted = self.convert_to_singbox(config)
                if converted:
                    if "transport" in converted and not converted["transport"]:
                        del converted["transport"]
                    individual_outbounds.append(converted)

            if not individual_outbounds:
                print("No valid configs found.")
                return

            tag_counts = defaultdict(int)
            for outbound in individual_outbounds:
                original_tag = outbound['tag']
                tag_counts[original_tag] += 1
                if tag_counts[original_tag] > 1:
                    outbound['tag'] = f"{original_tag} ({tag_counts[original_tag]})"

            valid_tags = [outbound['tag'] for outbound in individual_outbounds]

            dns_config = {
                "servers": [
                    {"tag": "proxy-dns", "address": "8.8.8.8", "detour": "select"},
                    {"tag": "direct-dns", "address": "1.1.1.1", "detour": "direct"},
                ],
                "rules": [
                    {"clash_mode": "Global", "server": "proxy-dns"},
                    {"clash_mode": "Direct", "server": "direct-dns"},
                    {"rule_set": ["geosite-ir", "geoip-ir"], "server": "direct-dns"},
                ], "final": "proxy-dns"
            }
            inbounds_config = [
                { "type": "tun", "tag": "tun-in", "inet4_address": "172.19.0.1/30", "auto_route": True, "stack": "system", "sniff": True },
                { "type": "mixed", "tag": "mixed-in", "listen": "127.0.0.1", "listen_port": 2080, "sniff": True }
            ]
            outbounds_config = [
                { "type": "selector", "tag": "select", "outbounds": ["auto", "direct"] + valid_tags, "default": "auto" },
                { "type": "urltest", "tag": "auto", "outbounds": valid_tags, "url": "http://www.gstatic.com/generate_204", "interval": "10m0s"},
                {"type": "direct", "tag": "direct"}, {"type": "block", "tag": "block"}
            ] + individual_outbounds
            route_config = {
                "rules": [
                    {"protocol": "dns", "outbound": "direct-dns"},
                    {"clash_mode": "Direct", "outbound": "direct"},
                    {"clash_mode": "Global", "outbound": "select"},
                    {"rule_set": ["geoip-private", "geosite-ir", "geoip-ir"], "outbound": "direct"},
                    {"rule_set": "geosite-ads", "outbound": "block"}
                ],
                "rule_set": [
                    {"type": "remote", "tag": "geosite-ads", "format": "binary", "url": "https://testingcf.jsdelivr.net/gh/MetaCubeX/meta-rules-dat@sing/geo/geosite/category-ads-all.srs", "download_detour": "direct"},
                    {"type": "remote", "tag": "geosite-private", "format": "binary", "url": "https://testingcf.jsdelivr.net/gh/MetaCubeX/meta-rules-dat@sing/geo/geosite/private.srs", "download_detour": "direct"},
                    {"type": "remote", "tag": "geosite-ir", "format": "binary", "url": "https://testingcf.jsdelivr.net/gh/MetaCubeX/meta-rules-dat@sing/geo/geosite/category-ir.srs", "download_detour": "direct"},
                    {"type": "remote", "tag": "geoip-private", "format": "binary", "url": "https://testingcf.jsdelivr.net/gh/MetaCubeX/meta-rules-dat@sing/geo/geoip/private.srs", "download_detour": "direct"},
                    {"type": "remote", "tag": "geoip-ir", "format": "binary", "url": "https://testingcf.jsdelivr.net/gh/MetaCubeX/meta-rules-dat@sing/geo/geoip/ir.srs", "download_detour": "direct"}
                ], "final": "select"
            }

            singbox_config = {
                "log": {"level": "info", "timestamp": True}, "dns": dns_config,
                "inbounds": inbounds_config, "outbounds": outbounds_config, "route": route_config
            }

            with open(self.output_file, 'w', encoding='utf-8') as f:
                json.dump(singbox_config, f, indent=2, ensure_ascii=False)
            
            print(f"✅ Successfully generated sing-box config at: {self.output_file}")

        except Exception as e:
            print(f"❌ Error processing configs: {str(e)}")

def main():
    converter = ConfigToSingbox()
    converter.process_configs()

if __name__ == '__main__':
    main()

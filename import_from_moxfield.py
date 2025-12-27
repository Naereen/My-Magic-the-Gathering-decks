#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script pour exporter les decks Moxfield au format Cockatrice (.txt).

- Auteur: Lilian Besson (@Naereen), aidé par Google Gemini.
- Dépendances: cloudscraper browser-cookie3
- Date: 2025-12-26
- Licence: MIT License
"""

import cloudscraper
import browser_cookie3
import time
import re
from pathlib import Path
from typing import List, Dict, Optional

# On utilise cloudscraper à la place de requests.Session()
# pour contourner les protections Cloudflare (Erreur 403).
API_URL = "https://api.moxfield.com/v2"

class MoxfieldAutoExporter:
    def __init__(self, username: str):
        self.username = username
        # Création d'un scraper qui imite un navigateur (Chrome par défaut)
        self.scraper = cloudscraper.create_scraper(
            browser={
                'browser': 'chrome',
                'platform': 'windows',
                'mobile': False
            }
        )
        self._load_cookies()

    def _load_cookies(self):
        print("--- Récupération des cookies de session ---")
        try:
            # Récupération des cookies
            # cj = browser_cookie3.load(domain_name='moxfield.com')
            cj = browser_cookie3.firefox(domain_name='moxfield.com')
            # cj = browser_cookie3.chromium(domain_name='moxfield.com')
            # cj = browser_cookie3.chrome(domain_name='moxfield.com')
            self.scraper.cookies = cj
            print("✅ Cookies récupérés avec succès.")
        except Exception as e:
            print(f"❌ Erreur lors de la lecture des cookies : {e}")
            exit(1)

    def verify_connection(self) -> bool:
        """Vérifie la session avec un endpoint simple."""
        # On utilise l'URL de profil qui est moins protégée
        url = f"https://api.moxfield.com/v1/users/{self.username}"
        resp = self.scraper.get(url)
        
        if resp.status_code == 200:
            print(f"✅ Accès autorisé pour le profil : {self.username}")
            return True
        else:
            print(f"❌ Session invalide ou blocage Cloudflare (Code {resp.status_code}).")
            print("Essayez de rafraîchir votre page Moxfield dans votre navigateur.")
            return False

    def get_all_decks(self) -> List[Dict]:
        print(f"\nRécupération de la liste des decks pour {self.username}...")
        decks = []
        page = 1
        
        while True:
            url = f"{API_URL}/users/{self.username}/decks"
            params = {"pageNumber": page, "pageSize": 50}
            
            resp = self.scraper.get(url, params=params)
            if resp.status_code != 200:
                print(f"Erreur page {page} : {resp.status_code}")
                break
            
            data = resp.json()
            page_data = data.get('data', [])
            if not page_data: break
                
            decks.extend(page_data)
            print(f"Page {page} chargée ({len(page_data)} decks)...", end="\r")
            
            if page >= data.get('totalPages', 1): break
            page += 1
            time.sleep(0.5)

        print(f"\nTotal decks trouvés : {len(decks)}")
        return decks

    def fetch_deck_details(self, public_id: str) -> Optional[Dict]:
        url = f"{API_URL}/decks/all/{public_id}"
        resp = self.scraper.get(url)
        return resp.json() if resp.status_code == 200 else None

    def format_to_txt(self, deck_data: Dict) -> str:
        lines = []
        # Mainboard
        for name, info in deck_data.get('mainboard', {}).items():
            lines.append(f"{info.get('quantity', 1)} {name}")
        # Sideboard / Commander
        sb = deck_data.get('sideboard', {})
        for name, info in sb.items():
            lines.append(f"SB: {info.get('quantity', 1)} {name}")
        cmd = deck_data.get('commanders', {})
        for name, info in cmd.items():
            if name not in sb:
                lines.append(f"SB: {info.get('quantity', 1)} {name}")
        return "\n".join(lines)

    def run(self):
        if not self.verify_connection():
            return

        decks = self.get_all_decks()
        output_dir = Path("Moxfield_Backups")
        output_dir.mkdir(exist_ok=True)

        for i, d in enumerate(decks, 1):
            name = d.get('name', 'Untitled')
            pid = d.get('publicId')
            safe_name = re.sub(r'[<>:"/\\|?*]', '', name).strip()
            
            print(f"[{i}/{len(decks)}] Exportation : {name}...", end="\r")
            
            details = self.fetch_deck_details(pid)
            if details:
                content = self.format_to_txt(details)
                with open(output_dir / f"{safe_name}.txt", "w", encoding="utf-8") as f:
                    f.write(content)
            time.sleep(0.4) # Un peu plus de délai pour éviter d'être flaggé
        
        print(f"\n\n✅ Exportation terminée dans '{output_dir}'.")

if __name__ == "__main__":
    USER = input("Entrez votre nom d'utilisateur Moxfield : ")
    app = MoxfieldAutoExporter(USER)
    app.run()

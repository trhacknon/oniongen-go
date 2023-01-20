import os

#copie des cles
key_path = input("Entrez le chemin de l'ensemble de clés (hs_ed25519_secret_key, hs_ed25519_public_key et hostname) : ")
if os.path.exists(key_path):
    os.system(f"cp {key_path}/hs_ed25519_secret_key {key_path}/hs_ed25519_public_key {key_path}/hostname /var/lib/tor/hidden_service/")
    print(f"Les clés ont été copiées dans /var/lib/tor/hidden_service/")
else:
    print(f"Impossible de trouver les clés dans {key_path}")

# changement des propriétaires et permissions
os.system("chown -R debian-tor /var/lib/tor")
os.system("chmod 700 /var/lib/tor/hidden_service")

# redémarrage du service tor
os.system("sudo /etc/init.d/tor restart")
os.system("sudo -u debian-tor tor")

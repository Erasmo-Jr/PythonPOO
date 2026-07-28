from hashlib import sha256

# SHA = Secure Hash Algorithm

texto = "Gafanhoto"
cod = texto.encode("utf-8")
hash = sha256(cod).hexdigest()

print(hash)

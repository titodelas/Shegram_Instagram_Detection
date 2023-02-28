import instaloader

# Crea un objeto Instaloader
L = instaloader.Instaloader()

# Obtiene la ID de un usuario dado su nombre de usuario
profile = instaloader.Profile.from_username(L.context, 'nombre_de_usuario')
print(profile.userid)
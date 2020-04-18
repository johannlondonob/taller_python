# Vueltas por una llanta en una distancia de 1000 metros
diametro_llanta, metros_recorridos = 50, 1000
radio_llanta = diametro_llanta / 2
distancia_vuelta = 2 * 3.1416 * radio_llanta
total_vueltas = metros_recorridos / distancia_vuelta
print(total_vueltas)
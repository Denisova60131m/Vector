import numpy as np

def cosine_distance(a, b):
    dot_product = np.dot(a, b) # Вычисление скалярного произведения a и b
    
    norm_a = np.linalg.norm(a) # Вычисление нормы (длины) каждого вектора
    norm_b = np.linalg.norm(b)
    
    cos_theta = dot_product / (norm_a * norm_b) # Вычисление косинусного расстояния
    
    return cos_theta

Natalia = np.array([15, 50, 80, 30, 45])
Ksenia = np.array([56, 43, 14, 28, 65])
Alexandra = np.array([52, 77, 27, 92, 35])
Daria = np.array([77, 13, 54, 33, 66])
Artem = np.array([85, 18, 12, 57, 95])
Ilnur = np.array([57, 17, 37, 25, 77])

distances = {
    'Ksenia': cosine_distance(Natalia, Ksenia),
    'Alexandra': cosine_distance(Natalia, Alexandra),
    'Daria': cosine_distance(Natalia, Daria),
    'Artem': cosine_distance(Natalia, Artem),
    'Ilnur': cosine_distance(Natalia, Ilnur)
}

closest_vector = min(distances, key=distances.get)

print("Вектор, ближайший к вектору Natalia:", closest_vector)

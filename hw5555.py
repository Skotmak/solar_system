from vpython import sphere, vector, color, rotate, canvas
import math


# Константы
G = 6.667e-11  # гравитационная постоянная, м^3 кг^-1 с^-2

MS = 1.9885e30  # масса Солнца, кг
ME = 5.97e24  # масса Земли, кг
MM = 7.348e22  # масса Луны, кг
MMercury = 3.33e23 # масса Меркурия, кг
MVenus = 4.87e24 # масса Венеры, кг
MMars = 6.42e23 # масса Марса, кг
MJupiter = 1.89e27 # масса Юпитера, кг
MSaturn = 5.68e26 # масса Сатурна, кг
MUran = 8.68e25 # масса Урана, кг

REM = 384.4e6  # расстояние от Земли до Луны
RSE = 1.496e11 # среднее расстояние от Солнца до Земли, метры
RMercury = 0.58e11 # среднее расстояние от Солнца до Меркурия, метры
RVenus = 1.08e11 # среднее расстояние от Солнца до Венеры, метры
RMars = 2.28e11 # среднее расстояние от Солнца до Марса, метры
RJupiter = 7.78e11 # среднее расстояние от Солнца до Юпитера, метры
RSaturn = 14.30e11 # среднее расстояние от Солнца до Сатурна, метры
RUran = 19.19e11 # среднее расстояние от Солнца до Урана, метры

F_EM = G*ME*MM/(REM*REM) # Гравитационная сила между Землей и Луной, Н
F_SE = G*MS*ME/(RSE*RSE) # Гравитационная сила между Солнцем и Землей. Н
F_MERCURY = G*MS*MMercury/(RMercury*RMercury) # Гравитационная сила между Солнцем и Меркурием, Н
F_VENUS = G*MS*MVenus/(RVenus*RVenus) # Гравитационная сила между Солнцем и Венерой, Н
F_MARS = G*MS*MMars/(RMars*RMars) # Гравитационная сила между Солнцем и Марсом, Н
F_JUPITER = G*MS*MJupiter/(RJupiter*RJupiter) # Гравитационная сила между Солнцем и Юпитером, Н
F_SATURN = G*MS*MSaturn/(RSaturn*RSaturn) # Гравитационная сила между Солнцем и Сатурном, Н
F_URAN = G*MS*MUran/(RUran*RUran) # Гравитационная сила между Солнцем и Ураном, Н

wm = math.sqrt(F_EM/(MM*REM))# Угловая скорость Луны
we = math.sqrt(F_SE/(ME*RSE))# Угловая скорость Земли
wMercury = math.sqrt(F_MERCURY/(MMercury*RMercury))# Угловая скорость Меркурия
wVenus = math.sqrt(F_VENUS/(MVenus*RVenus))# Угловая скорость Венеры
wMars = math.sqrt(F_MARS/(MMars*RMars))# Угловая скорость Марса
wJupiter = math.sqrt(F_JUPITER/(MJupiter*RJupiter))# Угловая скорость Юпитера
wSaturn = math.sqrt(F_SATURN/(MSaturn*RSaturn))# Угловая скорость Сатурна
wUran = math.sqrt(F_URAN/(MUran*RUran))# Угловая скорость Урана

c2 = canvas(title='Solar system model', width=640, height=480,)

v = vector(0.5, 0, 0)
Sun = sphere(canvas=c2, pos=vector(0, 0, 0), texture='texture_sun.jpg', radius=5, make_trail=False)
Mercury = sphere(canvas=c2, pos=vector(7.5, 0, 0), texture='texture_mercury.jpg', radius=0.024, make_trail=True, trail_type='points', trail_radius=0.01)
Venus = sphere(canvas=c2, pos=vector(8, 0, 0), texture='texture_venus.jpg', radius=0.060, make_trail=True, trail_type='points', trail_radius=0.01)
Earth = sphere(canvas=c2, pos=vector(9, 0, 0), texture='earth_texture.jpg', radius=0.063, make_trail=True, trail_type='points', trail_radius=0.01)
Moon = sphere(canvas=c2, pos=Earth.pos+v, texture='texture_moon.jpg', radius=0.017, make_trail=True, trail_type='points', trail_radius=0.01)
Mars = sphere(canvas=c2, pos=vector(9.3, 0, 0), texture='texture_mars.jpg', radius=0.033, make_trail=True, trail_type='points', trail_radius=0.01)
Jupiter = sphere(canvas=c2, pos=vector(15.3, 0, 0), texture='texture_jupiter.jpg', radius=0.699, make_trail=True, trail_type='curve', trail_radius=0.04)
Saturn = sphere(canvas=c2, pos=vector(21.8, 0, 0), texture='texture_saturn.jpg', radius=0.582, make_trail=True, trail_type='curve', trail_radius=0.04)
Uran = sphere(canvas=c2, pos=vector(26.7, 0, 0), texture='texture_uran.jpg', radius=0.253, make_trail=True, trail_type='curve', trail_radius=0.04)

# Используем полярные координаты
# Шаг , от него зависит скорость полёта планет
dt = 100
# углы поворота за один шаг:
theta_earth = we*dt
theta_moon = wm*dt
theta_mercury = wMercury*dt
theta_venus = wVenus*dt
theta_mars = wMars*dt
theta_jupiter = wJupiter*dt
theta_saturn = wSaturn*dt
theta_uran = wUran*dt
while dt <= 86400*365:
    # Планеты поворачиваются вокруг оси z (0,0,1)
    Earth.pos = rotate(Earth.pos, angle=theta_earth, axis=vector(0, 0, 1))
    Mercury.pos = rotate(Mercury.pos, angle=theta_mercury, axis=vector(0, 0, 1))
    Venus.pos = rotate(Venus.pos, angle=theta_venus, axis=vector(0, 0, 1))
    Mars.pos = rotate(Mars.pos, angle=theta_mars, axis=vector(0, 0, 1))
    Jupiter.pos = rotate(Jupiter.pos, angle=theta_jupiter, axis=vector(0, 0, 1))
    Saturn.pos = rotate(Saturn.pos, angle=theta_saturn, axis=vector(0, 0, 1))
    Uran.pos = rotate(Uran.pos, angle=theta_uran, axis=vector(0, 0, 1))
    v = rotate(v, angle=theta_moon, axis=vector(0, 0, 1))
    Moon.pos = Earth.pos + v
    dt += 10
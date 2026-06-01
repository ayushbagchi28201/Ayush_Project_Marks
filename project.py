import time
import os
import pandas as pd
import matplotlib.pyplot as plt
import nltk

def bot(txt, t=0.03):
    for c in txt:
        print(c, end='', flush=True)
        time.sleep(t)
    print()

L = {
    "English": {
        "name": "Enter your name: ",
        "count": "How many student records do you want to enter?",
        "study": "Study hours: ",
        "sleep": "Sleep hours: ",
        "screen": "Screen time: ",
        "ex": "Exercise hours: ",
        "marks": "Marks obtained: ",
        "anal": "Analyzing data...",
        "res": "AI Analysis Results:",
        "s1": "Higher study hours generally improve marks.",
        "s2": "Adequate sleep has a positive impact on performance.",
        "s3": "Excessive screen time negatively affects marks.",
        "s4": "Physical activity supports better academic results.",
        "clean": "Temporary user data cleaned successfully.",
        "bye": "Thank you for using the AI system."
    },
    "French": {
        "name": "Entrez votre nom : ",
        "count": "Combien d'enregistrements voulez-vous saisir ?",
        "study": "Heures d'étude : ",
        "sleep": "Heures de sommeil : ",
        "screen": "Temps d'écran : ",
        "ex": "Heures d'exercice : ",
        "marks": "Notes obtenues : ",
        "anal": "Analyse des données...",
        "res": "Résultats de l'analyse IA :",
        "s1": "Plus d'heures d'étude améliorent généralement les notes.",
        "s2": "Un sommeil suffisant a un impact positif sur les performances.",
        "s3": "Un temps d'écran excessif nuit aux résultats.",
        "s4": "L'activité physique favorise de meilleurs résultats scolaires.",
        "clean": "Les données temporaires ont été supprimées.",
        "bye": "Merci d'utiliser le système IA."
    },
    "Spanish": {
        "name": "Ingrese su nombre: ",
        "count": "¿Cuántos registros desea ingresar?",
        "study": "Horas de estudio: ",
        "sleep": "Horas de sueño: ",
        "screen": "Tiempo de pantalla: ",
        "ex": "Horas de ejercicio: ",
        "marks": "Calificaciones obtenidas: ",
        "anal": "Analizando datos...",
        "res": "Resultados del análisis de IA:",
        "s1": "Más horas de estudio generalmente mejoran las calificaciones.",
        "s2": "Dormir adecuadamente mejora el rendimiento.",
        "s3": "Demasiado tiempo de pantalla afecta negativamente.",
        "s4": "La actividad física apoya mejores resultados académicos.",
        "clean": "Los datos temporales fueron eliminados.",
        "bye": "Gracias por usar el sistema de IA."
    },
    "German": {
        "name": "Geben Sie Ihren Namen ein: ",
        "count": "Wie viele Datensätze möchten Sie eingeben?",
        "study": "Lernstunden: ",
        "sleep": "Schlafstunden: ",
        "screen": "Bildschirmzeit: ",
        "ex": "Trainingsstunden: ",
        "marks": "Erhaltene Noten: ",
        "anal": "Daten werden analysiert...",
        "res": "KI-Analyseergebnisse:",
        "s1": "Mehr Lernstunden verbessern in der Regel die Noten.",
        "s2": "Ausreichender Schlaf wirkt sich positiv aus.",
        "s3": "Zu viel Bildschirmzeit wirkt sich negativ aus.",
        "s4": "Körperliche Aktivität unterstützt bessere Leistungen.",
        "clean": "Temporäre Daten wurden gelöscht.",
        "bye": "Danke für die Nutzung des KI-Systems."
    },
    "Russian": {
        "name": "Введите ваше имя: ",
        "count": "Сколько записей студентов вы хотите ввести?",
        "study": "Часы учёбы: ",
        "sleep": "Часы сна: ",
        "screen": "Время за экраном: ",
        "ex": "Часы упражнений: ",
        "marks": "Полученные оценки: ",
        "anal": "Анализ данных...",
        "res": "Результаты анализа ИИ:",
        "s1": "Большее количество часов учёбы обычно улучшает оценки.",
        "s2": "Достаточный сон положительно влияет на результаты.",
        "s3": "Чрезмерное время за экраном отрицательно влияет на оценки.",
        "s4": "Физическая активность способствует лучшим академическим результатам.",
        "clean": "Временные данные пользователя удалены.",
        "bye": "Спасибо за использование системы ИИ."
    }
}

print("=" * 50)
print("Available Languages")
print("=" * 50)

for i, k in enumerate(L.keys(), 1):
    print(f"{i}. {k}")

ch = int(input("\nSelect language number: "))
lang = list(L.values())[ch - 1]

name = input(lang["name"])

bot(f"\nHello {name}! AI Analysis System Activated.\n")

n = int(input(lang["count"]))

rows = []

for i in range(n):
    print("\n" + "=" * 40)
    bot(f"Student Record {i+1}")
    print("=" * 40)

    student_name = input("Student Name: ")
    study = float(input(lang["study"]))
    sleep = float(input(lang["sleep"]))
    screen = float(input(lang["screen"]))
    exercise = float(input(lang["ex"]))
    marks = float(input(lang["marks"]))

    rows.append([
        student_name,
        study,
        sleep,
        screen,
        exercise,
        marks
    ])

df = pd.DataFrame(
    rows,
    columns=[
        "Name",
        "Study",
        "Sleep",
        "Screen",
        "Exercise",
        "Marks"
    ]
)

df.to_csv("student_habits.csv", index=False)

bot("\n" + lang["anal"])

# =========================
# GRAPH 1: STUDENT MARKS
# =========================

plt.figure(figsize=(10, 5))
bars = plt.bar(df["Name"], df["Marks"])

for bar, mark in zip(bars, df["Marks"]):
    plt.text(
        bar.get_x() + bar.get_width()/2,
        mark + 1,
        f"{mark}",
        ha="center"
    )

plt.xlabel("Students")
plt.ylabel("Marks")
plt.title(f"Student Marks Report | Generated by {name}")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# =========================
# GRAPH 2: STUDY HOURS VS MARKS
# =========================

plt.figure(figsize=(10, 5))

plt.plot(
    df["Name"],
    df["Marks"],
    marker="o",
    linewidth=2,
    label="Marks"
)

plt.plot(
    df["Name"],
    df["Study"] * 10,
    marker="s",
    linewidth=2,
    label="Study Hours ×10"
)

plt.xlabel("Students")
plt.ylabel("Value")
plt.title(f"Study Hours and Marks Analysis | {name}")
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# =========================
# GRAPH 3: SLEEP HOURS VS MARKS
# =========================

plt.figure(figsize=(10, 5))

plt.scatter(
    df["Sleep"],
    df["Marks"],
    s=100
)

for i in range(len(df)):
    plt.annotate(
        df["Name"][i],
        (df["Sleep"][i], df["Marks"][i])
    )

plt.xlabel("Sleep Hours")
plt.ylabel("Marks")
plt.title(f"Sleep Hours vs Marks | {name}")
plt.grid(True)
plt.show()

# =========================
# GRAPH 4: DAILY ACTIVITY PIE
# =========================

mean_values = df[
    ["Study", "Sleep", "Screen", "Exercise"]
].mean()

plt.figure(figsize=(7, 7))

plt.pie(
    mean_values.values,
    labels=mean_values.index,
    autopct="%1.1f%%"
)

plt.title(
    f"Average Daily Activity Distribution\nPrepared for {name}"
)

plt.show()

# =========================
# GRAPH 5: MARKS DISTRIBUTION
# =========================

low = sum(df["Marks"] < 60)
mid = sum((df["Marks"] >= 60) & (df["Marks"] < 80))
high = sum(df["Marks"] >= 80)

plt.figure(figsize=(7, 7))

plt.pie(
    [low, mid, high],
    labels=["Low", "Medium", "High"],
    autopct="%1.1f%%"
)

plt.title(
    f"Marks Distribution\nGenerated by {name}"
)

plt.show()

# =========================
# AI ANALYSIS
# =========================

bot("\n" + lang["res"])

corr = df[["Study", "Sleep", "Screen", "Exercise", "Marks"]].corr()["Marks"]

print("\nCorrelation with Marks:")
print(corr)

print()

if corr["Study"] > 0:
    bot(lang["s1"])

if corr["Sleep"] > 0:
    bot(lang["s2"])

if corr["Screen"] < 0:
    bot(lang["s3"])

if corr["Exercise"] > 0:
    bot(lang["s4"])

# =========================
# CLEANUP
# =========================

if os.path.exists("student_habits.csv"):
    os.remove("student_habits.csv")

bot("\n" + lang["clean"])
bot(lang["bye"])

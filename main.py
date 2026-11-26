import os

LINE = "Twelve yogurts, zero spoons, zero meals, zero plan. Please place your crisis in the bagging area."

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(LINE)

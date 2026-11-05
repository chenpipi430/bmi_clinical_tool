# hello.py
def calculate_bmi(weight_kg, height_m):
    bmi = weight_kg / (height_m ** 2)
    return round(bmi, 2)

if __name__ == "__main__":
    print("=== 臨床 BMI 計算工具 v1.0 ===")
    w = 70
    h = 1.75
    print(f"病患體重 {w}kg, 身高 {h}m -> BMI: {calculate_bmi(w, h)}")
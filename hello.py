# hello.py
def calculate_bmi(weight_kg, height_m):
    bmi = weight_kg / (height_m ** 2)
    return round(bmi, 2)

def analyze_bmi(bmi):
    if bmi < 18.5:
        return "過輕"
    elif bmi < 24:
        return "正常"
    else:
        return "過重或異常"

if __name__ == "__main__":
    print("=== 臨床 BMI 計算工具 v2.0 (同學修改版) ===")
    w = 70
    h = 1.75
    bmi_val = calculate_bmi(w, h)
    
    print(f"病患體重 {w}kg, 身高 {h}m")
    print(f"計算結果 BMI: {bmi_val} -> 判定為: {analyze_bmi(bmi_val)}")
    print(f"=== 計算結束 (emily新增) ===")
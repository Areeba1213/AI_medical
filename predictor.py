class Predictor:
    def __init__(self, gender, age, symptoms):
        self.gender = gender
        self.age = age
        self.symptoms = symptoms

    def analyze(self):
        if self.gender == "Female" and "Lump" in self.symptoms and "Fatigue" in self.symptoms:
            return "Breast Cancer Risk", 82
        elif "Chest Pain" in self.symptoms:
            return "Heart Disease Risk", 75
        elif "Irregular Periods" in self.symptoms and self.gender == "Female":
            return "PCOS Risk", 78
        elif "Weight Loss" in self.symptoms and self.age > 40:
            return "Diabetes Risk", 69
        else:
            return "No Major Risk Detected", 50

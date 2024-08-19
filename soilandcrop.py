# Sample Python code for Crop and Soil Management System with Disease Detection

class CropRecommendationSystem:
    def __init__(self, soil_type, moisture_level, pH_level, symptoms):
        self.soil_type = soil_type
        self.moisture_level = moisture_level
        self.pH_level = pH_level
        self.symptoms = symptoms

    def recommend_crop(self):
        if self.soil_type == "loamy" and 6.0 <= self.pH_level <= 7.5 and self.moisture_level > 30:
            return "Wheat"
        elif self.soil_type == "clayey" and 5.5 <= self.pH_level <= 6.5 and self.moisture_level > 25:
            return "Rice"
        elif self.soil_type == "sandy" and 6.0 <= self.pH_level <= 7.5 and self.moisture_level > 20:
            return "Maize"
        else:
            return "No suitable crop found. Consider soil treatment."

    def detect_disease(self):
        if "yellow leaves" in self.symptoms:
            return "Possible disease: Nitrogen deficiency"
        elif "white powder" in self.symptoms:
            return "Possible disease: Powdery mildew"
        elif "wilting" in self.symptoms:
            return "Possible disease: Fusarium wilt"
        else:
            return "No disease detected."

# Example usage
soil_type = input("Enter soil type (loamy, clayey, sandy): ")
moisture_level = float(input("Enter moisture level (%): "))
pH_level = float(input("Enter pH level: "))
symptoms = input("Enter any symptoms observed in the crop (comma-separated): ").split(",")

crop_system = CropRecommendationSystem(soil_type, moisture_level, pH_level, symptoms)
recommended_crop = crop_system.recommend_crop()
detected_disease = crop_system.detect_disease()

print(f"Recommended Crop: {recommended_crop}")
print(f"Disease Diagnosis: {detected_disease}")

import tkinter as tk
from tkinter import messagebox, scrolledtext
import google.generativeai as genai

# Valid symptoms for the Expert System
def get_valid_symptoms():
    return {
        "fever", "cough", "sore_throat", "loss_of_smell", "fatigue", "muscle_pain",
        "sneezing", "runny_nose", "itchy_eyes", "rash", "joint_pain", "nausea",
        "vomiting", "yellow_skin", "chest_pain", "shortness_of_breath", "sweating",
        "dry_cough", "tiredness", "headache", "stiff_neck", "weight_loss",
        "night_sweats", "abdominal_pain", "diarrhea", "bloating", "heartburn",
        "indigestion", "burning_urination", "lower_abdominal_pain", "frequent_urination",
        "thirst", "depression", "weight_gain", "anxiety", "rapid_heartbeat",
        "dry_skin", "sensitivity_to_cold", "blurry_vision", "itchy_skin", "redness",
        "blisters", "itchy_throat", "watery_eyes", "joint_stiffness", "swelling",
        "morning_pain", "skin_rash", "ear_pain", "hearing_loss", "white_patches_on_tonsils",
        "toothache", "bad_breath", "insomnia", "irritability", "cold_intolerance",
        "constipation", "increased_hunger", "high_fever", "neck_pain",
        "sensitivity_to_light", "low_back_pain", "leg_pain", "numbness", "pelvic_pain",
        "abnormal_discharge", "wheezing", "yellowing_skin", "swollen_abdomen",
        "high_blood_pressure", "pain_while_walking", "cold_legs", "red_eye",
        "eye_pain", "blurred_vision", "swollen_lymph_nodes", "back_pain",
        "difficulty_urinating", "difficulty_swallowing", "hoarseness"
    }

# Diagnosis function based on symptoms
def diagnose(symptoms_set):
    rules = [
        ({"fever", "cough", "sore_throat"}, "influenza"),
        ({"fever", "cough", "loss_of_smell"}, "covid19"),
        ({"fever", "fatigue", "muscle_pain"}, "viral_fever"),
        ({"sneezing", "runny_nose", "itchy_eyes"}, "allergy"),
        ({"fever", "rash", "joint_pain"}, "dengue"),
        ({"nausea", "vomiting", "yellow_skin"}, "hepatitis"),
        ({"chest_pain", "shortness_of_breath", "sweating"}, "heart_attack"),
        ({"chest_pain", "dry_cough", "tiredness"}, "pneumonia"),
        ({"headache", "stiff_neck", "fever"}, "meningitis"),
        ({"weight_loss", "night_sweats", "cough"}, "tuberculosis"),
        ({"abdominal_pain", "diarrhea", "vomiting"}, "food_poisoning"),
        ({"bloating", "heartburn", "indigestion"}, "gastritis"),
        ({"burning_urination", "lower_abdominal_pain"}, "uti"),
        ({"frequent_urination", "thirst", "fatigue"}, "diabetes"),
        ({"fatigue", "depression", "weight_gain"}, "hypothyroidism"),
        ({"anxiety", "rapid_heartbeat", "sweating"}, "panic_attack"),
        ({"dry_skin", "sensitivity_to_cold"}, "hypothyroidism"),
        ({"blurry_vision", "frequent_urination"}, "diabetes"),
        ({"itchy_skin", "redness", "blisters"}, "eczema"),
        ({"itchy_throat", "sneezing", "watery_eyes"}, "hay_fever"),
        ({"joint_stiffness", "swelling", "morning_pain"}, "rheumatoid_arthritis"),
        ({"skin_rash", "fever", "cough"}, "measles"),
        ({"ear_pain", "hearing_loss", "fever"}, "ear_infection"),
        ({"sore_throat", "white_patches_on_tonsils"}, "strep_throat"),
        ({"toothache", "swelling", "bad_breath"}, "dental_abscess"),
        ({"insomnia", "irritability", "fatigue"}, "sleep_disorder"),
        ({"fatigue", "cold_intolerance", "constipation"}, "hypothyroidism"),
        ({"increased_hunger", "weight_loss", "fatigue"}, "type_1_diabetes"),
        ({"high_fever", "neck_pain", "sensitivity_to_light"}, "meningitis"),
        ({"low_back_pain", "leg_pain", "numbness"}, "sciatica"),
        ({"pelvic_pain", "abnormal_discharge"}, "pelvic_inflammatory_disease"),
        ({"shortness_of_breath", "wheezing"}, "asthma"),
        ({"fatigue", "yellowing_skin", "swollen_abdomen"}, "liver_disease"),
        ({"chest_pain", "high_blood_pressure"}, "angina"),
        ({"pain_while_walking", "cold_legs"}, "peripheral_artery_disease"),
        ({"red_eye", "eye_pain", "blurred_vision"}, "conjunctivitis"),
        ({"swollen_lymph_nodes", "fever", "fatigue"}, "mononucleosis"),
        ({"dry_cough", "weight_loss", "fever"}, "tuberculosis"),
        ({"back_pain", "difficulty_urinating"}, "kidney_stones"),
        ({"difficulty_swallowing", "hoarseness"}, "throat_cancer")
    ]
    for rule_symptoms, diagnosis in rules:
        if rule_symptoms.issubset(symptoms_set):
            return f"Diagnosis: {diagnosis.replace('_', ' ').title()}"
    return "No diagnosis found for the given symptoms. Please consult a healthcare professional."

# Welcome Screen
class WelcomeScreen:
    def __init__(self, root):
        self.root = root
        self.root.title("Medical Diagnosis System")
        self.root.geometry("400x300")
        
        # Set soothing background color
        self.root.configure(bg="#F5F6F5")
        
        # Centered content
        frame = tk.Frame(self.root, bg="#F5F6F5")
        frame.place(relx=0.5, rely=0.5, anchor="center")
        
        tk.Label(frame, text="Welcome to the Medical Diagnosis System", font=("Arial", 16, "bold"), bg="#F5F6F5", fg="#333333").pack(pady=20)
        tk.Label(frame, text="This tool is for informational purposes only.\nConsult a healthcare professional.", font=("Arial", 10), fg="#B22222", bg="#F5F6F5").pack(pady=10)
        
        tk.Button(frame, text="Expert System", command=self.open_expert_system, width=20, font=("Arial", 12), bg="#4682B4", fg="#FFFFFF").pack(pady=10)
        tk.Button(frame, text="Ask AI", command=self.open_chatbot, width=20, font=("Arial", 12), bg="#2E8B57", fg="#FFFFFF").pack(pady=10)
    
    def open_expert_system(self):
        self.root.destroy()
        root = tk.Tk()
        app = MedicalExpertSystemGUI(root)
        root.mainloop()
    
    def open_chatbot(self):
        self.root.destroy()
        root = tk.Tk()
        app = AIChatbotGUI(root)
        root.mainloop()

# Enhanced Expert System GUI with side-by-side symptom lists, better layout, and back button
class MedicalExpertSystemGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Medical Expert System")
        self.root.geometry("800x600")
        
        # Set soothing background color
        self.root.configure(bg="#F5F6F5")
        
        # Title and disclaimer at the top
        title_frame = tk.Frame(self.root, bg="#F5F6F5")
        title_frame.pack(pady=10)
        
        self.label = tk.Label(title_frame, text="Select your symptoms:", font=("Arial", 14, "bold"), bg="#F5F6F5", fg="#333333")
        self.label.pack()
        
        tk.Label(title_frame, text="Consult a doctor for accurate diagnosis.", font=("Arial", 10), fg="#B22222", bg="#F5F6F5").pack(pady=5)
        
        # Main frame for symptom lists
        main_frame = tk.Frame(self.root, bg="#FFFFFF", padx=20, pady=20, relief="ridge", borderwidth=2)
        main_frame.pack(pady=10, padx=20, fill="both", expand=True)
        
        # Left and right frames for symptom lists
        left_frame = tk.Frame(main_frame, bg="#FFFFFF", padx=10, pady=10, relief="ridge", borderwidth=2)
        right_frame = tk.Frame(main_frame, bg="#FFFFFF", padx=10, pady=10, relief="ridge", borderwidth=2)
        left_frame.pack(side="left", padx=20, fill="y")
        right_frame.pack(side="right", padx=20, fill="y")
        
        # Scrollable canvas for symptom lists
        left_canvas = tk.Canvas(left_frame, bg="#FFFFFF", highlightthickness=0)
        left_scrollbar = tk.Scrollbar(left_frame, orient="vertical", command=left_canvas.yview)
        left_scrollable_frame = tk.Frame(left_canvas, bg="#FFFFFF")
        
        left_scrollable_frame.bind(
            "<Configure>",
            lambda e: left_canvas.configure(scrollregion=left_canvas.bbox("all"))
        )
        
        left_canvas.configure(yscrollcommand=left_scrollbar.set)
        
        left_canvas.pack(side="left", fill="both", expand=True)
        left_scrollbar.pack(side="right", fill="y")
        left_canvas.create_window((0, 0), window=left_scrollable_frame, anchor="nw")
        
        right_canvas = tk.Canvas(right_frame, bg="#FFFFFF", highlightthickness=0)
        right_scrollbar = tk.Scrollbar(right_frame, orient="vertical", command=right_canvas.yview)
        right_scrollable_frame = tk.Frame(right_canvas, bg="#FFFFFF")
        
        right_scrollable_frame.bind(
            "<Configure>",
            lambda e: right_canvas.configure(scrollregion=right_canvas.bbox("all"))
        )
        
        right_canvas.configure(yscrollcommand=right_scrollbar.set)
        
        right_canvas.pack(side="left", fill="both", expand=True)
        right_scrollbar.pack(side="right", fill="y")
        right_canvas.create_window((0, 0), window=right_scrollable_frame, anchor="nw")
        
        self.valid_symptoms = sorted(get_valid_symptoms())
        mid_point = len(self.valid_symptoms) // 2
        left_symptoms = self.valid_symptoms[:mid_point]
        right_symptoms = self.valid_symptoms[mid_point:]
        
        self.symptom_vars = {symptom: tk.BooleanVar() for symptom in self.valid_symptoms}
        
        for symptom in left_symptoms:
            cb = tk.Checkbutton(left_scrollable_frame, text=symptom.replace('_', ' ').title(), variable=self.symptom_vars[symptom], font=("Arial", 10), bg="#FFFFFF", fg="#333333", activebackground="#F5F6F5", selectcolor="#E8ECEF", padx=5, pady=2)
            cb.pack(anchor="w")
        
        for symptom in right_symptoms:
            cb = tk.Checkbutton(right_scrollable_frame, text=symptom.replace('_', ' ').title(), variable=self.symptom_vars[symptom], font=("Arial", 10), bg="#FFFFFF", fg="#333333", activebackground="#F5F6F5", selectcolor="#E8ECEF", padx=5, pady=2)
            cb.pack(anchor="w")
        
        # Frame for buttons
        button_frame = tk.Frame(self.root, bg="#F5F6F5")
        button_frame.pack(pady=20)
        
        self.diagnose_button = tk.Button(button_frame, text="Diagnose", command=self.show_diagnosis, width=15, font=("Arial", 12, "bold"), bg="#4682B4", fg="#FFFFFF")
        self.diagnose_button.pack(side="left", padx=10)
        
        self.back_button = tk.Button(button_frame, text="Back", command=self.go_back, width=15, font=("Arial", 12, "bold"), bg="#DC143C", fg="#FFFFFF")
        self.back_button.pack(side="left", padx=10)
    
    def show_diagnosis(self):
        symptoms_set = {symptom for symptom, var in self.symptom_vars.items() if var.get()}
        if not symptoms_set:
            result = "No symptoms selected. Unable to make a diagnosis.\nPlease consult a healthcare professional."
        else:
            result = diagnose(symptoms_set)
        messagebox.showinfo("Diagnosis", result)
    
    def go_back(self):
        self.root.destroy()
        root = tk.Tk()
        app = WelcomeScreen(root)
        root.mainloop()

# Enhanced AI Chatbot GUI with input field above chat display and soothing colors
class AIChatbotGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("AI Medical Chatbot")
        self.root.geometry("600x600")
        
        genai.configure(api_key="AIzaSyDd-I74-40aLxaNQh8Hk9dwoqNNi_hdBUE")
        
        # Set soothing background color
        self.root.configure(bg="#F5F6F5")
        
        main_frame = tk.Frame(self.root, bg="#FFFFFF", padx=20, pady=20, relief="raised", borderwidth=2)
        main_frame.place(relx=0.5, rely=0.5, anchor="center")
        
        # Title and disclaimer
        tk.Label(main_frame, text="Ask a medical question:", font=("Arial", 14, "bold"), bg="#FFFFFF", fg="#333333").pack(pady=10)
        tk.Label(main_frame, text="AI responses are for informational purposes only.\nConsult a doctor for accurate advice.", font=("Arial", 10), fg="#B22222", bg="#FFFFFF").pack(pady=5)
        
        # Input frame (above chat display)
        input_frame = tk.Frame(main_frame, bg="#FFFFFF")
        input_frame.pack(fill="x", padx=10, pady=10)
        
        self.query_entry = tk.Entry(input_frame, font=("Arial", 12), bg="#E8ECEF", fg="#333333", relief="flat", bd=2)
        self.query_entry.pack(side="left", fill="x", expand=True, padx=5)
        self.query_entry.bind("<Return>", self.send_query)
        
        tk.Button(input_frame, text="Send", command=self.send_query, width=10, font=("Arial", 12, "bold"), bg="#4682B4", fg="#FFFFFF").pack(side="right", padx=5)
        
        # Chat display (below input field)
        self.chat_display = scrolledtext.ScrolledText(main_frame, wrap=tk.WORD, height=20, font=("Arial", 12), bg="#E8ECEF", fg="#333333", relief="flat", bd=2)
        self.chat_display.pack(padx=10, pady=10, fill="both", expand=True)
        self.chat_display.config(state="disabled")
        
        # Back button
        tk.Button(main_frame, text="Back", command=self.go_back, width=10, font=("Arial", 12, "bold"), bg="#DC143C", fg="#FFFFFF").pack(pady=10)
    
    def send_query(self, event=None):
        query = self.query_entry.get().strip()
        if not query:
            messagebox.showwarning("Input Error", "Please enter a question.")
            return
        
        self.chat_display.config(state="normal")
        self.chat_display.insert(tk.END, f"You: {query}\n")
        self.chat_display.config(state="disabled")
        self.query_entry.delete(0, tk.END)
        
        response = self.get_ai_response(query)
        
        self.chat_display.config(state="normal")
        self.chat_display.insert(tk.END, f"AI: {response}\n\n")
        self.chat_display.config(state="disabled")
        self.chat_display.yview(tk.END)
    
    def get_ai_response(self, query):
        try:
            model = genai.GenerativeModel('gemini-1.5-flash')
            prompt = f"You are a medical assistant. Provide accurate and safe medical advice, but always recommend consulting a doctor.\n\nUser: {query}"
            response = model.generate_content(prompt)
            if response and response.text:
                return response.text + "\n\nConsult a healthcare professional for accurate advice."
            return "Error: No response from AI."
        except Exception as e:
            return f"Error: {str(e)}"
    
    def go_back(self):
        self.root.destroy()
        root = tk.Tk()
        app = WelcomeScreen(root)
        root.mainloop()

# Main function
def main():
    root = tk.Tk()
    app = WelcomeScreen(root)
    root.mainloop()

if __name__ == "__main__":
    main()
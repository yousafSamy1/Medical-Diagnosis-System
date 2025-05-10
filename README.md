# Medical Diagnosis System 🏥

## Description
The **Medical Diagnosis System** is a Python-based desktop application designed to provide preliminary medical diagnosis suggestions based on user-reported symptoms. This project integrates a rule-based expert system and an AI-powered chatbot to assist users in identifying potential health conditions. The application features a user-friendly graphical user interface (GUI) built with `tkinter` and leverages the Google Generative AI API for intelligent chatbot responses. It is intended for informational purposes only and strongly recommends consulting healthcare professionals for accurate diagnoses.

### Features
- **Expert System**: Allows users to select from a comprehensive list of symptoms and receive a suggested diagnosis based on predefined rules.
- **AI Chatbot**: Provides interactive and informative responses to medical questions using the Google Generative AI model, with a focus on safety and professional consultation advice.
- **Eye-Friendly Design**: Utilizes soothing colors and a well-organized layout to enhance user comfort during prolonged use.
- **Multi-Page Navigation**: Includes a welcome screen, expert system page, and chatbot page with seamless navigation via "Back" buttons.
- **Customizable Interface**: Features adjustable button colors and layouts for an improved user experience.

## Knowledge Base: Supported Diseases and Symptoms
The expert system uses a rule-based approach to diagnose the following conditions based on symptom combinations. Below is a list of supported diseases along with the symptoms that trigger each diagnosis:

- **Influenza**: Fever, Cough, Sore Throat
- **COVID-19**: Fever, Cough, Loss of Smell
- **Viral Fever**: Fever, Fatigue, Muscle Pain
- **Allergy**: Sneezing, Runny Nose, Itchy Eyes
- **Dengue**: Fever, Rash, Joint Pain
- **Hepatitis**: Nausea, Vomiting, Yellow Skin
- **Heart Attack**: Chest Pain, Shortness of Breath, Sweating
- **Pneumonia**: Chest Pain, Dry Cough, Tiredness
- **Meningitis**: Headache, Stiff Neck, Fever (also High Fever, Neck Pain, Sensitivity to Light)
- **Tuberculosis**: Weight Loss, Night Sweats, Cough (also Dry Cough, Weight Loss, Fever)
- **Food Poisoning**: Abdominal Pain, Diarrhea, Vomiting
- **Gastritis**: Bloating, Heartburn, Indigestion
- **Urinary Tract Infection (UTI)**: Burning Urination, Lower Abdominal Pain
- **Diabetes**: Frequent Urination, Thirst, Fatigue (also Blurry Vision, Frequent Urination)
- **Hypothyroidism**: Fatigue, Depression, Weight Gain (also Dry Skin, Sensitivity to Cold; Fatigue, Cold Intolerance, Constipation)
- **Panic Attack**: Anxiety, Rapid Heartbeat, Sweating
- **Eczema**: Itchy Skin, Redness, Blisters
- **Hay Fever**: Itchy Throat, Sneezing, Watery Eyes
- **Rheumatoid Arthritis**: Joint Stiffness, Swelling, Morning Pain
- **Measles**: Skin Rash, Fever, Cough
- **Ear Infection**: Ear Pain, Hearing Loss, Fever
- **Strep Throat**: Sore Throat, White Patches on Tonsils
- **Dental Abscess**: Toothache, Swelling, Bad Breath
- **Sleep Disorder**: Insomnia, Irritability, Fatigue
- **Type 1 Diabetes**: Increased Hunger, Weight Loss, Fatigue
- **Sciatica**: Low Back Pain, Leg Pain, Numbness
- **Pelvic Inflammatory Disease**: Pelvic Pain, Abnormal Discharge
- **Asthma**: Shortness of Breath, Wheezing
- **Liver Disease**: Fatigue, Yellowing Skin, Swollen Abdomen
- **Angina**: Chest Pain, High Blood Pressure
- **Peripheral Artery Disease**: Pain While Walking, Cold Legs
- **Conjunctivitis**: Red Eye, Eye Pain, Blurred Vision
- **Mononucleosis**: Swollen Lymph Nodes, Fever, Fatigue
- **Kidney Stones**: Back Pain, Difficulty Urinating
- **Throat Cancer**: Difficulty Swallowing, Hoarseness

If no matching diagnosis is found, the system advises consulting a healthcare professional.

## Tools and Technologies Used
- **Python 3.x**: Core programming language for the application.
- **tkinter**: Used to create the graphical user interface (GUI).
- **google-generativeai**: Python library for integrating the Google Generative AI API (Gemini 1.5 Flash model) to power the chatbot.
- **Visual Studio Code** (or any preferred IDE): For development and debugging.

## Prerequisites
- Python 3.x
- Required libraries:
  - `tkinter` (typically included with Python)
  - `google-generativeai` (`pip install google-generativeai`)
- A valid Google API key for the Generative AI model.

## Installation
   ```
2. Install the required dependencies:
   ```bash
   pip install google-generativeai
   ```
3. Replace the placeholder API key in the code with your own Google Generative AI API key:
   - Open `medical_diagnosis_system.py` and update the `api_key` in the `genai.configure()` line with your key (e.g., replace `"AIzaSyDd-I74-40aLxaNQh8Hk9dwoqNNi_hdBUE"` with your API key).

## Usage
1. Run the application:
   ```bash
   python medical_diagnosis_system.py
   ```
2. On the welcome screen, select one of the following options:
   - **Expert System**: Click to select symptoms and view a suggested diagnosis.
   - **Ask AI**: Click to type a medical question and receive an AI-generated response.
3. Use the "Back" button to return to the welcome screen from any page.

## Contributing
Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a new branch for your feature or bug fix:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Description of your changes"
   ```
4. Push to the branch:
   ```bash
   git push origin feature-name
   ```
5. Open a pull request. For major changes, please open an issue first to discuss the proposed changes.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments
- Built with `tkinter` for the GUI.
- Powered by Google Generative AI for chatbot functionality.
- Inspired by the need for accessible and user-friendly health information tools.

## Contact
For questions, feedback, or support, please open an issue in the repository or contact the maintainer at (yousafsamy50@example.com).


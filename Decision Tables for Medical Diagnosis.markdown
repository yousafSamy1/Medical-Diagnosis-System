# Decision Tables for Medical Diagnosis

## Decision Table 1: Respiratory and Fever-Related Conditions

| Conditions/Rules | Rule 1 | Rule 2 | Rule 3 | Rule 4 | Rule 5 | Rule 6 | Rule 7 | Rule 8 |
|------------------|--------|--------|--------|--------|--------|--------|--------|--------|
| Fever            | Y      | Y      | -      | Y      | Y      | Y      | Y      | Y      |
| Cough            | Y      | Y      | -      | Y      | -      | -      | -      | -      |
| Sore Throat      | -      | Y      | -      | -      | -      | -      | -      | -      |
| Loss of Smell    | -      | -      | Y      | -      | -      | -      | -      | -      |
| Rash             | -      | -      | -      | -      | Y      | -      | -      | -      |
| Joint Pain       | -      | -      | -      | -      | -      | Y      | -      | -      |
| Weight Loss      | -      | -      | -      | -      | -      | -      | Y      | -      |
| Night Sweats     | -      | -      | -      | -      | -      | -      | Y      | -      |
| Dry Cough        | -      | -      | -      | -      | -      | Y      | -      | -      |
| Fatigue          | -      | -      | -      | Y      | -      | -      | -      | -      |
| Muscle Pain      | -      | -      | -      | -      | Y      | -      | -      | -      |
| **Diagnosis**    | Influenza | Influenza | Viral Fever | COVID19 | Dengue | Tuberculosis | Tuberculosis | Tuberculosis |
| **Severity**     | Moderate | Moderate | Moderate | Severe | Severe | Severe | Severe | Severe |

## Decision Table 2: Systemic and Gastrointestinal Conditions

| Conditions/Rules    | Rule 1 | Rule 2 | Rule 3 | Rule 4 | Rule 5 |
|---------------------|--------|--------|--------|--------|--------|
| Nausea              | -      | -      | -      | -      | Y      |
| Vomiting            | -      | -      | -      | -      | Y      |
| Yellow Skin         | -      | -      | -      | Y      | Y      |
| Abdominal Pain      | -      | -      | -      | Y      | -      |
| Diarrhea            | -      | -      | -      | Y      | -      |
| Bloating            | -      | Y      | -      | -      | -      |
| Heartburn           | -      | Y      | -      | -      | -      |
| Indigestion         | -      | Y      | -      | -      | -      |
| Fatigue             | -      | -      | Y      | -      | -      |
| Swollen Abdomen     | -      | -      | Y      | -      | -      |
| Back Pain           | Y      | -      | -      | -      | -      |
| Difficulty Urinating| Y      | -      | -      | -      | -      |
| **Diagnosis**       | Kidney Stones | Gastritis | Liver Disease | Food Poisoning | Hepatitis |
| **Severity**        | Moderate | Mild | Severe | Moderate | Severe |

## Decision Table 3: Allergic and Skin-Related Conditions

| Conditions/Rules | Rule 1 | Rule 2 | Rule 3 | Rule 4 | Rule 5 |
|------------------|--------|--------|--------|--------|--------|
| Sneezing         | -      | -      | -      | -      | Y      |
| Runny Nose       | -      | -      | -      | -      | Y      |
| Itchy Eyes       | -      | -      | -      | -      | Y      |
| Itchy Throat     | -      | -      | -      | Y      | -      |
| Watery Eyes      | -      | -      | -      | Y      | -      |
| Itchy Skin       | -      | -      | Y      | -      | -      |
| Redness          | -      | -      | Y      | -      | -      |
| Blisters         | -      | -      | Y      | -      | -      |
| Red Eye          | -      | Y      | -      | -      | -      |
| Eye Pain         | -      | Y      | -      | -      | -      |
| Blurred Vision   | -      | Y      | -      | -      | -      |
| Skin Rash        | Y      | -      | -      | -      | -      |
| Fever            | Y      | -      | -      | -      | -      |
| Cough            | Y      | -      | -      | -      | -      |
| **Diagnosis**    | Measles | Conjunctivitis | Eczema | Hay Fever | Allergy |
| **Severity**     | Severe | Mid | Mid | Mid | Mid |

## Decision Table 4: Cardiovascular and Respiratory Conditions

| Conditions/Rules  | Rule 1 | Rule 2 | Rule 3 | Rule 4 |
|-------------------|--------|--------|--------|--------|
| Chest Pain        | Y      | Y      | Y      | Y      |
| Shortness of Breath | -      | -      | -      | Y      |
| Sweating          | -      | -      | -      | Y      |
| Dry Cough         | -      | -      | Y      | -      |
| Tiredness         | -      | -      | Y      | -      |
| High Blood Pressure | -      | Y      | -      | -      |
| Wheezing          | Y      | -      | -      | -      |
| **Diagnosis**     | Asthma | Angina | Pneumonia | Heart Attack |
| **Severity**      | Moderate | Severe | Severe | Severe |

## Decision Table 5: Neurological and Endocrine Conditions

| Conditions/Rules   | Rule 1 | Rule 2 | Rule 3 | Rule 4 | Rule 5 |
|--------------------|--------|--------|--------|--------|--------|
| Headache           | -      | -      | -      | Y      | Y      |
| Stiff Neck         | -      | -      | -      | -      | Y      |
| Fever              | -      | -      | -      | Y      | -      |
| Sensitivity to Light| -      | -      | -      | Y      | -      |
| Frequent Urination | -      | -      | Y      | -      | -      |
| Thirst             | -      | -      | Y      | -      | -      |
| Fatigue            | -      | -      | Y      | -      | -      |
| Blurry Vision      | -      | Y      | -      | -      | -      |
| Depression         | Y      | -      | -      | -      | -      |
| Weight Gain        | Y      | -      | -      | -      | -      |
| **Diagnosis**      | Hypothyroidism | Diabetes | Diabetes | Meningitis | Meningitis |
| **Severity**       | Moderate | Moderate | Moderate | Severe | Severe |




----------------------------------------------------------------Notes------------------------------------------------------------------
Table 1: 
Respiratory and Fever-Related Conditions
Rule 1: Must have Fever and Cough together.
Rule 2: Must have Fever, Cough, and Sore Throat together.
Rule 3: Must have Loss of Smell only.
Rule 4: Must have Fever and Fatigue together.
Rule 5: Must have Fever, Rash, and Muscle Pain together.
Rule 6: Must have Fever, Dry Cough, and Joint Pain together.
Rule 7: Must have Fever, Weight Loss, and Night Sweats together.
Rule 8: Must have Fever only.


Table 2:
Systemic and Gastrointestinal Conditions
Rule 1: Must have Back Pain and Difficulty Urinating together.
Rule 2: Must have Bloating, Heartburn, and Indigestion together.
Rule 3: Must have Fatigue and Swollen Abdomen together.
Rule 4: Must have Abdominal Pain, Diarrhea, and Yellow Skin together.
Rule 5: Must have Nausea, Vomiting, and Yellow Skin together.


Table 3: 
Allergic and Skin-Related Conditions
Rule 1: Must have Skin Rash, Fever, and Cough together.
Rule 2: Must have Red Eye, Eye Pain, and Blurred Vision together.
Rule 3: Must have Itchy Skin, Redness, and Blisters together.
Rule 4: Must have Itchy Throat and Watery Eyes together.
Rule 5: Must have Sneezing, Runny Nose, and Itchy Eyes together.


Table 4:
 Cardiovascular and Respiratory Conditions
Rule 1: Must have Chest Pain and Wheezing together.
Rule 2: Must have Chest Pain and High Blood Pressure together.
Rule 3: Must have Chest Pain, Dry Cough, and Tiredness together.
Rule 4: Must have Chest Pain, Shortness of Breath, and Sweating together.


Table 5:
 Neurological and Endocrine Conditions
Rule 1: Must have Depression and Weight Gain together.
Rule 2: Must have Blurry Vision only.
Rule 3: Must have Frequent Urination, Thirst, and Fatigue together.
Rule 4: Must have Headache, Fever, and Sensitivity to Light together.
Rule 5: Must have Headache and Stiff Neck together.

# Resume Job Prediction & Skill Gap Analysis Documentation

## 1. Project Overview  
This project aims to analyze resumes and predict the most suitable job title based on the resume content. Additionally, it identifies missing key skills for the predicted job to help individuals focus on improving those areas.

---

## 2. Input Data

- **Resume Dataset:** Contains resumes and their associated job titles. Each row corresponds to a resume and the relevant job title.
- **Job Description Dataset:** Contains detailed job descriptions including required skills, responsibilities, and qualifications. This dataset is used to extract key skills for each job.

---

## 3. Data Preprocessing

- **Purpose:** To convert raw textual resumes into a format understandable by machine learning algorithms.
- **Steps:**
  - Convert all text to lowercase to avoid case sensitivity.
  - Remove punctuation, numbers, and any irrelevant characters.
  - Tokenize text into individual words using a specialized tokenizer to correctly separate words.
  - Remove common stopwords (e.g., "and", "the", "is") that carry little semantic value, improving model performance.

---

## 4. Feature Extraction

- We use **TF-IDF (Term Frequency-Inverse Document Frequency)** vectorization to convert text into numeric features.
- **TF-IDF** highlights important words in resumes relative to the entire dataset by giving higher weights to words that are unique and relevant.
- The vectorizer limits features to the top 5000 most frequent meaningful words to reduce dimensionality and noise.

---

## 5. Label Encoding

- Job titles (target variable) are categorical text labels.
- We convert them into numeric labels using **Label Encoding**, enabling the model to process job titles as numbers internally.

---

## 6. Model Training

- The model chosen is **Logistic Regression**:
  - Suitable for multi-class classification problems like job prediction.
  - Robust and efficient for text classification when combined with TF-IDF features.
- The dataset is split into training and testing sets (80%-20%) to evaluate model performance fairly.
- The model is trained on the training set with a maximum of 1000 iterations to ensure convergence.

---

## 7. Model Evaluation

- After training, predictions are made on the test set.
- Evaluation metrics used:
  - **Accuracy Score:** Percentage of correct predictions.
  - **Classification Report:** Includes precision, recall, and F1-score for each job class.
- These metrics help understand how well the model predicts job titles based on resume text.

---

## 8. Keyword Extraction for Missing Skills

- We extract the top keywords (skills) from the job descriptions using TF-IDF again.
- By comparing keywords from the job description to the candidate's resume tokens, we identify skills missing from the resume.
- This helps generate a "roadmap" for skill improvement tailored to the predicted job.

---

## 9. Key Variables and Their Roles

- **df_resume:** DataFrame containing resume data.
- **df_jobs:** DataFrame containing job description data.
- **clean_resume / clean_description:** Processed text columns with cleaned, tokenized, and stopword-removed content.
- **X:** Features (cleaned resumes) used for training.
- **y:** Labels (job titles) corresponding to resumes.
- **vectorizer:** TF-IDF vectorizer converting text to numeric features.
- **label_encoder:** Encodes job titles to numeric labels.
- **model:** Trained Logistic Regression classifier.
- **stop_words:** Set of common words removed to improve text quality.
- **tokenizer:** Tokenizer used to split text into words.

---

## 10. Functions Overview

- **get_top_keywords(texts, top_n=30):**  
  Extracts the top `n` keywords from a list of texts using TF-IDF.  
  *Purpose:* Identify most relevant words representing skills or important concepts in job descriptions or resumes.

- **predict_job_and_missing_skills_v2(resume_text):**  
  Given a raw resume text:  
  1. Cleans and tokenizes the input.  
  2. Transforms text into TF-IDF features.  
  3. Predicts the job title using the trained model.  
  4. Finds corresponding job descriptions and extracts top keywords.  
  5. Compares candidate’s resume words with job keywords to detect missing skills.  
  *Purpose:* Provide both a predicted job and a personalized skill improvement list.

---

## 11. Model Persistence

- The entire pipeline components (model, vectorizer, label encoder, tokenizer, stop words, job data) are saved together in a single file using **joblib**.  
- This allows reusing the trained model later without retraining, ensuring consistent predictions.

---

## Summary

This project builds a pipeline to process textual resumes, predict the most fitting job title, and provide actionable feedback on missing skills. Each step — from text cleaning to feature extraction, model training, and keyword analysis — is carefully chosen to maximize accuracy and practical usability. The modular design allows easy updates or expansions, such as adding more data or switching classification algorithms.


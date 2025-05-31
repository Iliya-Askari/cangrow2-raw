# Resume Job Prediction & Skill Gap Analysis Documentation

## 1. Project Overview  
This project aims to analyze resumes and predict the most suitable job title based on the resume content. Additionally, it identifies missing key skills for the predicted job to help individuals focus on improving those areas.

---

## 2. Input Data

- **Resume Dataset:** Contains resumes and their associated job titles. Each row corresponds to a resume and the relevant job title.
- **Job Description Dataset:** Contains detailed job descriptions including required skills, responsibilities, and qualifications. This dataset is used to extract key skills for each job.

---

## 3. Exploratory Data Analysis (EDA)

### Basic Information

- Checked dataset structure, data types, and summary statistics for both datasets.
- Assessed missing values and duplicate records to ensure data quality.

### Visualizations

- **Job Title Distribution:** Bar plot showing the frequency of each job title in the resume dataset.
- **Word Count Distributions:** Histograms with KDE for word counts in resumes and job descriptions, helping understand text length variability.
- **Average Word Count per Job Title:** Horizontal bar chart illustrating average resume length by job title.
- **Frequent Words:** Top 20 most common words in resumes visualized with a bar chart to reveal common terms and domain-specific vocabulary.
- **Longest and Shortest Resumes:** Samples extracted to review extremes in text length and content.

These analyses helped identify data imbalances, outliers, and key textual characteristics for better preprocessing and modeling decisions.

---

## 4. Data Preprocessing

- **Text Cleaning:**  
  - Lowercased all text to reduce case sensitivity.  
  - Removed punctuation, numbers, and non-alphabetic characters via regex.  
- **Tokenization:**  
  - Applied the `TreebankWordTokenizer` to split text into meaningful tokens.  
- **Stopword Removal:**  
  - Used a predefined list of English stopwords (`sklearn`'s ENGLISH_STOP_WORDS) to remove common but uninformative words.  
- **Rejoining Tokens:**  
  - Tokens were joined back into cleaned strings suitable for vectorization.

---

## 5. Feature Extraction

- Used **TF-IDF Vectorization** to convert cleaned resumes into numeric feature vectors, focusing on the top 5000 features for efficiency.
- This method emphasizes words important in individual documents relative to the corpus.

---

## 6. Label Encoding

- Converted categorical job titles into numeric labels using **LabelEncoder** for compatibility with machine learning algorithms.

---

## 7. Model Training

- Selected **Logistic Regression** as the classification model for its robustness in multi-class text classification.
- Split the data into training (80%) and testing (20%) sets with fixed random state for reproducibility.
- Trained the model with up to 1000 iterations to ensure convergence.

---

## 8. Model Evaluation

- Evaluated the trained model on the test set.
- Metrics included:  
  - **Accuracy Score:** Overall correctness percentage.  
  - **Classification Report:** Detailed precision, recall, and F1-score per class.
- These metrics assess the model’s ability to predict job titles accurately.

---

## 9. Keyword Extraction for Missing Skills

- Extracted top keywords (skills) from job descriptions using TF-IDF.
- Compared these keywords with candidate resume tokens to find missing skills.
- Generated personalized suggestions for skill improvement aligned with predicted job roles.

---

## 10. Key Variables and Their Roles

- **df_resume:** DataFrame containing resume data.
- **df_jobs:** DataFrame containing job description data.
- **clean_resume / clean_description:** Text columns after cleaning, tokenization, and stopword removal.
- **X:** Feature matrix (cleaned resume texts).
- **y:** Target labels (encoded job titles).
- **vectorizer:** TF-IDF vectorizer.
- **label_encoder:** Converts job titles to numeric labels.
- **model:** Trained Logistic Regression classifier.
- **stop_words:** Set of common words filtered out.
- **tokenizer:** Tokenizer used for splitting text into tokens.

---

## 11. Functions Overview

- **get_top_keywords(texts, top_n=30):**  
  Extracts the most relevant keywords from given texts based on TF-IDF scores. Useful for identifying important skills and concepts in job descriptions or resumes.

- **predict_job_and_missing_skills_v2(resume_text):**  
  Given a raw resume text, this function:  
  1. Cleans and tokenizes the text.  
  2. Vectorizes the cleaned text with TF-IDF.  
  3. Predicts the most suitable job title using the trained model.  
  4. Extracts top keywords from related job descriptions.  
  5. Identifies skills missing from the resume compared to job requirements.  
  Returns the predicted job title and a list of suggested skills for improvement.

---

## 12. Model Persistence

- The trained model, vectorizer, label encoder, tokenizer, stop words, and job description data are bundled together and saved with **joblib** for easy loading and reuse without retraining.

---

## Summary

This project provides an end-to-end pipeline for resume analysis: from cleaning raw text data and exploring dataset characteristics, through training a classification model, to suggesting personalized skill gaps for career development. The addition of detailed EDA ensures data quality and better insights, improving model reliability and practical value.


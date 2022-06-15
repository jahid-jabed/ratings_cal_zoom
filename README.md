# Actual Rating Calculation of the Zoom Cloud Meetings App using User Reviews on Google Play Store with Sentiment Annotation of BERT and Hybridization of RNN and LSTM
** **

**A. Environment**
+ [Google Colaboratory](https://colab.research.google.com "Google Colab"): This project use Google Colaboratory for compute purpose.
+ RAM: 12 GB, Disk Space: 80 GB
+ Compute Engine: GPU
+ Language: Python

**B. Datasets**
+ The datsets used in this work and the saved model data will found in this [link](https://drive.google.com/drive/folders/1EeeV4jOpoJgqoj0v_tdMSoXvNcPgV3hn).
+ `Reviews.csv` - includes all the raw reviews collected with other information.
+ `App_Reviews.csv(/.xlsx)` - includes only used raw reviews.
+ `Zoom_Reviews` - includes only the zoom app reviews collected.
+ `/Pickle Data` - includes process datasets and models saved data.
+ `/Pickle Data/Models` - includes model saved data for Dataset #1.
+ `/Pickle Data/Model_2` - includes model saved data for Dataset #2.
+ `/Pickle Data/Model_3` - includes model saved data for Dataset #3.
+ `/Pickle Data/Model_4` - includes model saved data for Dataset #4.

**C. Codes**
+ [`ds1_sentiment_analysis_for_rating_calculation.py`](https://github.com/jahid-jabed/ratings_cal_zoom/blob/main/codes/ds1_sentiment_analysis_for_rating_calculation.py)
+ [`ds2_sentiment_analysis_for_rating_calculation.py`](https://github.com/jahid-jabed/ratings_cal_zoom/blob/main/codes/ds2_sentiment_analysis_for_rating_calculation.py)
+ [`ds3_sentiment_analysis_for_rating_calculation.py`](https://github.com/jahid-jabed/ratings_cal_zoom/blob/main/codes/ds3_sentiment_analysis_for_rating_calculation.py)
+ [`ds4_sentiment_analysis_for_rating_calculation.py`](https://github.com/jahid-jabed/ratings_cal_zoom/blob/main/codes/ds4_sentiment_analysis_for_rating_calculation.py)
+ [`zoom_app_reviews_star_calculation.py`](https://github.com/jahid-jabed/ratings_cal_zoom/blob/main/codes/zoom_app_reviews_star_calculation.py)

**D. Results and Performance**


**E. Dependencies**
+ The dataset importation from Google Drive and saving model data into Google Drive required permission of drive.

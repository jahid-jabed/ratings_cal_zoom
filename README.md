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
  + Model preparation, training, and testing using DS - 1
+ [`ds2_sentiment_analysis_for_rating_calculation.py`](https://github.com/jahid-jabed/ratings_cal_zoom/blob/main/codes/ds2_sentiment_analysis_for_rating_calculation.py)
  + Model preparation, training, and testing using DS - 2
+ [`ds3_sentiment_analysis_for_rating_calculation.py`](https://github.com/jahid-jabed/ratings_cal_zoom/blob/main/codes/ds3_sentiment_analysis_for_rating_calculation.py)
  + Model preparation, training, and testing using DS - 3
+ [`ds4_sentiment_analysis_for_rating_calculation.py`](https://github.com/jahid-jabed/ratings_cal_zoom/blob/main/codes/ds4_sentiment_analysis_for_rating_calculation.py)
  + Model preparation, training, and testing using DS - 4
+ [`zoom_app_reviews_star_calculation.py`](https://github.com/jahid-jabed/ratings_cal_zoom/blob/main/codes/zoom_app_reviews_star_calculation.py)
  + Actual rating calculation using models discussed for the Zoom Cloud Meetings App
+ [`all_app_reviews_star_calculation.py`](https://github.com/jahid-jabed/ratings_cal_zoom/blob/main/codes/all_app_reviews_star_calculation.py)
  + Actual rating calculation of All reviews colled using discussed models.
+ [`bert_sentiment_analysis_for_rating_calculations.py`](https://github.com/jahid-jabed/ratings_cal_zoom/blob/main/codes/bert_sentiment_analysis_for_rating_calculations.py)
  + Performance Analysis of BERT Base on Pre-Processed Reviews.
+ [`rnn_sentiment_analysis.py`](https://github.com/jahid-jabed/ratings_cal_zoom/blob/main/codes/rnn_sentiment_analysis.py)
  + Performance Analysis of RNN.
+ [`lstm_sentiment_analysis.py`](https://github.com/jahid-jabed/ratings_cal_zoom/blob/main/codes/lstm_sentiment_analysis.py)
  + Performance Analysis of LSTM.
+ [`bert_sentiment_analysis`](https://github.com/jahid-jabed/ratings_cal_zoom/blob/main/codes/bert_sentiment_analysis.py)
  + Performance Analysis on All Reviews using BERT Base

**D. Results and Performance**
+ Summary of precisions (P), recalls (R), f1-scores (F1), and accuracies (A) of DS - 1, DS - 2, DS - 3, and DS - 4.

|      || Ratings | | DS - 1 |      |      |      | |DS - 2 |      |      |      | | DS - 3 |      |      |      || DS - 4 |      |      |      |
|:----:|:-:|:-------:|:-:|:----:|:----:|:----:|:----:|:-:|:----:|:----:|:----:|:----:|:-:|:----:|:----:|:----:|:----:|:-:|:----:|:----:|:----:|:----:|
|      | |           | |   **P**  |   **R**  |  **F1**  |   **A**  ||   **P**  |   **R**  |  **F1**  |   **A**  ||   **P**  |   **R**  |  **F1**  |   **A**  ||   **P**  |   **R**  |  **F1**  |   **A**  |
|      |  |  ☆     |  | 0.61 | 0.58 | 0.59 |      || 0.54 | 0.67 | 0.60 |      || **0.68** | **0.71** | **0.69** |      | |0.48 | 0.67 | 0.56 |      |
|      |   | ☆☆    | | **0.41** | **0.30** | **0.35** |      | |0.32 | 0.12 | 0.18 |      | |0.00 | 0.00 | 0.00 |      | |0.00 | 0.00 | 0.00 |      |
|**Our Models**||   ☆☆☆ |     | **0.47** | 0.28 | 0.35 | 0.61 || 0.38 | 0.29 | 0.33 | 0.45 || 0.33 | 0.25 | 0.29 | **0.71** || 0.35 | 0.21 | 0.27 | 0.54 |
|      |   |☆☆☆☆  | | **0.43** | 0.20 | 0.27 |      | |0.37 | 0.38 | **0.37** |      | |0.38 | 0.11 | 0.17 |      || 0.41 | 0.10 | 0.16 |      |
|      |  |☆☆☆☆☆ | | 0.67 | 0.89 | 0.76 |      | |0.49 | 0.65 | 0.56 |      | |0.76 | **0.94** | **0.84** |      | |0.60 | 0.87 | 0.71 |      |
|      |   |        | |  |      |      |      |  |   |   |      |      |  |      | |      |      |  |      |   |   |      |
|      |    |       | | _**BERT Base #**_|      |      |      | |**BERT Base** |      |      |      | |**RNN** |      |      |      |  | **LSTM**|     |      |      |
|      |    |☆      | | _0.81_ | _0.82_ | _0.82_ |      || 0.53 | 0.68 | 0.59 |      || 0.40 | 0.42 | 0.41 |      | | 0.38|0.51 | 0.44 |      |
|      |    |☆☆    | | _0.51_ | _0.59_ | _0.55_ |      | |0.30 | 0.28 | 0.29 |      | |0.00 | 0.00 | 0.00 |      |  |0.00| 0.00 | 0.00 |      |
|**Pretrained Models**||   ☆☆☆ |    | _0.33_ | _0.47_ | _0.39_ | _0.67_| | 0.43 | **0.35** | 0.38 | 0.53 || 0.39 | **0.35** | **0.47** | 0.45| | 0.34 | 0.29 | 0.31 | 0.47 |
|      |  | ☆☆☆☆  | | _0.60_ | _0.61_ | _0.60_ |      | |0.31 | **0.40** | 0.35 |      || 0.36 | 0.06 | 0.11 |      |  | 0.36 |0.11 | 0.17 |    |
|      |  |☆☆☆☆☆ | | _0.71_ | _0.67_ | _0.69_ |      | |**0.77** | 0.67 | 0.72 |      | |0.55 | 0.83 | 0.66 |      |  | 0.55 | 0.83 | 0.66 |    |

_# Use pre-processed unbiased dataset based on BERT Base_

+ Calculated average rating of the Zoom Cloud Meetings App and All Apps with actual average rating.

| Model Trained on Dataset | Calculated Average Ratings |          |  Pooled Average Rating  |          |Average Rating on Dataset|          |
|:------------------------:|:--------------------------:|:--------:|:-----------------------:|:--------:|:-----------------------:|:--------:|
|                          | **Zoom Cloud Meetings App**| **All Apps** | **Zoom Cloud Meetings App** | **All Apps** | **Zoom Cloud Meetings App** | **All Apps** |
|          **DS - 1**          |            3.70            |   3.97   |                         |          |                         |          |
|          **DS - 2**          |            3.01            |   3.03   |           3.60          |   3.73   |           3.08          |   3.42   |
|          **DS - 3**          |            3.96            |   4.21   |                         |          |                         |          |
|          **DS - 4**          |            3.71            |   3.70   |                         |          |                         |          |


**E. Dependencies**
+ The dataset importation from Google Drive and saving model data into Google Drive required permission of drive.


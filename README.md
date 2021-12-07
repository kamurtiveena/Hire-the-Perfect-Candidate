<p> <img src="https://komarev.com/ghpvc/?username=Alok-Ranjan23&label=Project%20views&color=ce9927&style=flat" alt="Hire-the-Best-Fit" /> </p>

# Hire-the-Perfect-Candidate
Application to shortlist resume from the bulk of resumes

### Problem Statement
* Hiring employees effectively is essential to the survival of any organization. The hiring process consists of soliciting potential candidates during the recruitment and then determining the best candidates to be employees during the selection process. The selection process, in particular, enables organizations to build and maintain a productive and motivated workforce that will be the key to their success. 
* Organization wants to hire a Machine Learning Engineer, and has provided a job description and resumes of various candidates. The responsibility is to filter the candidates that fit the most based on the provided job description for the first interview round.
* Dataset is provided(taken from HackerEarth challenge) that contains the resumes of various candidates, and job description for Machine Learning Engineer. The responsibility is to determine the percentage that a candidate fits the job role based on the job description.

### Data Description
* Dataset is taken from HackerEarth Machine Learning Challenge([A Perfect Fit](https://www.hackerearth.com/challenges/competitive/hackerearth-machine-learning-challenge-resume-shortlisting/)). 
* The dataset folder contains the following files:
    *  train.csv: 90 x 2
    *  trainResumes(a folder): 90 resumes that you must use for training your model
    *  test.csv: 60 x 1
    *  testResumes(a folder): 60 resumes that you must use for testing your model
    *  sample_submission.csv: 5 x 2
    *  Job description.pdf: PDF file that represents the job description of a Machine Learning engineer
* The dataset contains the following columns:
    *  Column name      | Column description
       ------------     | -------------
       CandidateID      | Represents the unique identification number of a candidate
       Match Percentage | Represents the percentage that a candidate fits based on the job description

### Evaluation Metric
* score = 100*max(0, 1 - metrics.mean_squared_log_error(actual, predicted))

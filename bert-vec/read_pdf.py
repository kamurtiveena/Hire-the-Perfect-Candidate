import os
import numpy as np
import pandas as pd
from pdfminer import high_level

train = pd.read_csv('../dataset/train.csv')
test = pd.read_csv('../dataset/test.csv')

train_path = "../dataset/trainResumes/"
test_path = "../dataset/testResumes/"

# empty list for resumes text
train_resumes = []
test_resumes = []

# ids
ids = list(train.CandidateID)
test_ids = list(test.CandidateID)

# pdf2string
def pdf2string_train(path, ids, resumes):
    for i in ids:
        main_path = path+i+'.pdf'
        text = high_level.extract_text(main_path)
        str_list = text.split()
        str_list = str_list[:]
        string = ' '.join(str_list)
        resumes.append(string)
        

def pdf2string_test(path, test_ids, resumes):
    for i in test_ids:
        main_path = path+i+'.pdf'
        text = high_level.extract_text(main_path)
        str_list = text.split()
        str_list = str_list[:]
        string = ' '.join(str_list)
        resumes.append(string)

# Job requirement
job_requirement = high_level.extract_text("../dataset/Job description.pdf")
job_req_list = job_requirement.split()[:]
job_req_str = ' '.join(job_req_list)
    
pdf2string_train(train_path, ids, train_resumes)
pdf2string_test(test_path,  test_ids, test_resumes)
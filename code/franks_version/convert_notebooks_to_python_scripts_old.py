import jupyter
import nbconvert
import os

os.system("jupyter nbconvert --to script '01_Set_Up_Dependencies.ipynb' --output-dir='CI_CD'")
os.system("jupyter nbconvert --to script '02_Set_Up_S3.ipynb' --output-dir='CI_CD'")
os.system("jupyter nbconvert --to script '03_Preprocess_Data.ipynb' --output-dir='CI_CD'")
os.system("jupyter nbconvert --to script '04_Set_Up_Athena.ipynb' --output-dir='CI_CD'")
os.system("jupyter nbconvert --to script '06_Split_Data_and_Set_Up_Feature_Store.ipynb' --output-dir='CI_CD' --output '05_Split_Data_and_Set_Up_Feature_Store'")
os.system("jupyter nbconvert --to script '07_Build_Train_Deploy_Model_and_Perform_Model_Monitoring.ipynb' --output-dir='CI_CD' --output '06_Build_Train_Deploy_Model_and_Perform_Model_Monitoring'")
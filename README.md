# Network Security (MLops)

This machine learning project detects network threats with a strong accuracy of 𝟿𝟽.𝟾𝟽% using 𝙍𝙖𝙣𝙙𝙤𝙢 𝙁𝙤𝙧𝙚𝙨𝙩. What makes this project special is how I brought together both machine learning and modern deployment practices through 𝙈𝙇𝙤𝙥𝙨.

## Index
- [Project Structure](#Project-Structure)
- [Technical Stuff](#Technical-Stuff )

## Architecture

![]()




> ## Project Structure 📦
  ```
📦ProjectStructure
 ┣ 📂.github
 ┃ ┗ 📂workflows
 ┃ ┃ ┗ 📜main.yaml
 ┣ 📂data_schema
 ┃ ┗ 📜schema.yaml
 ┣ 📂final_model
 ┃ ┣ 📜model.pkl
 ┃ ┗ 📜preprocessor.pkl
 ┣ 📂networksecurity
 ┃ ┣ 📂cloud
 ┃ ┃ ┣ 📜s3_syncer.py
 ┃ ┃ ┗ 📜__init__.py
 ┃ ┣ 📂components
 ┃ ┃ ┣ 📜data_ingestion.py
 ┃ ┃ ┣ 📜data_transformation.py
 ┃ ┃ ┣ 📜data_validation.py
 ┃ ┃ ┣ 📜model_trainer.py
 ┃ ┃ ┗ 📜__init__.py
 ┃ ┣ 📂constant
 ┃ ┃ ┣ 📂training_pipeline
 ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┗ 📜__init__.py
 ┃ ┣ 📂entity
 ┃ ┃ ┣ 📜artifact_entity.py
 ┃ ┃ ┣ 📜config_entity.py
 ┃ ┃ ┗ 📜__init__.py
 ┃ ┣ 📂exception
 ┃ ┃ ┣ 📜execption.py
 ┃ ┃ ┗ 📜__init__.py
 ┃ ┣ 📂logging
 ┃ ┃ ┣ 📜logger.py
 ┃ ┃ ┗ 📜__init__.py
 ┃ ┣ 📂pipeline
 ┃ ┃ ┣ 📜batch_prediction.py
 ┃ ┃ ┣ 📜training_pipeline.py
 ┃ ┃ ┗ 📜__init__.py
 ┃ ┣ 📂utils
 ┃ ┃ ┣ 📂main_utils
 ┃ ┃ ┃ ┣ 📜utils.py
 ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┣ 📂ml_utils
 ┃ ┃ ┃ ┣ 📂metric
 ┃ ┃ ┃ ┃ ┣ 📜classification_metric.py
 ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┣ 📂model
 ┃ ┃ ┃ ┃ ┣ 📜estimator.py
 ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┗ 📜__init__.py
 ┃ ┗ 📜__init__.py
 ┣ 📂Network_Data
 ┃ ┗ 📜NetworkData.csv
 ┣ 📂notebooks
 ┣ 📂prediction_output
 ┃ ┗ 📜output.csv
 ┣ 📂templates
 ┃ ┗ 📜table.html
 ┣ 📂valid_data
 ┃ ┗ 📜test.csv
 ┣ 📜.env
 ┣ 📜.gitignore
 ┣ 📜app.py
 ┣ 📜Dockerfile
 ┣ 📜main.py
 ┣ 📜push_data.py
 ┣ 📜README.md
 ┣ 📜requirements.txt
 ┣ 📜setup.py
 ┗ 📜test_mongodb.py
  ```

## Technical Stuff 

<div align="center">
  <code><img width="50" src="https://github.com/devicons/devicon/blob/master/icons/scikitlearn/scikitlearn-original.svg" alt="Sklern" title="SkLearn"/></code>
  <code><img width="50" src="https://blog.ippon.fr/content/images/size/w1200/format/webp/2021/10/logo-teal.png" alt="FastAPI" title="FastAPI"/></code>
	<code><img width="50" src="https://raw.githubusercontent.com/marwin1991/profile-technology-icons/refs/heads/main/icons/github.png" alt="GitHub" title="GitHub"/></code>
	<code><img width="50" src="https://raw.githubusercontent.com/marwin1991/profile-technology-icons/refs/heads/main/icons/html.png" alt="HTML" title="HTML"/></code>
	<code><img width="50" src="https://raw.githubusercontent.com/marwin1991/profile-technology-icons/refs/heads/main/icons/numpy.png" alt="NumPy" title="NumPy"/></code>
	<code><img width="50" src="https://raw.githubusercontent.com/marwin1991/profile-technology-icons/refs/heads/main/icons/pandas.png" alt="Pandas" title="Pandas"/></code>
	<code><img width="50" src="https://raw.githubusercontent.com/marwin1991/profile-technology-icons/refs/heads/main/icons/mongodb.png" alt="mongoDB" title="mongoDB"/></code>
	<code><img width="50" src="https://raw.githubusercontent.com/marwin1991/profile-technology-icons/refs/heads/main/icons/docker.png" alt="Docker" title="Docker"/></code>
	<code><img width="50" src="https://mlops.community/wp-content/uploads/2021/09/MLflow-logo.png" alt="MLFlow" title="MLFlow"/></code>
	<code><img width="50" src="https://images.crunchbase.com/image/upload/c_pad,h_256,w_256,f_auto,q_auto:eco,dpr_1/c6ibcshe3uxmg56dtc6t" alt="DagsHub" title="DagsHub"/> 
  </code>
	<code><img width="50" src="https://raw.githubusercontent.com/marwin1991/profile-technology-icons/refs/heads/main/icons/ci_cd.png" alt="CI/CD" title="CI/CD"/></code>
	<code><img width="50" src="https://github.com/tandpfun/skill-icons/blob/main/icons/GithubActions-Dark.svg" alt="GitHubActions" title="GitHubActions"/></code>
	<code><img width="50" src="https://raw.githubusercontent.com/marwin1991/profile-technology-icons/refs/heads/main/icons/aws.png" alt="AWS" title="AWS"/></code>
</div>


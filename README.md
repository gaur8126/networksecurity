# Network Security (MLops)

This machine learning project detects network threats with a strong accuracy of 𝟿𝟽.𝟾𝟽% using 𝙍𝙖𝙣𝙙𝙤𝙢 𝙁𝙤𝙧𝙚𝙨𝙩. What makes this project special is how I brought together both machine learning and modern deployment practices through 𝙈𝙇𝙤𝙥𝙨.


## How I started this project :- 

* First, I had to choose a plateform where i could start it ,so started with `VSCode`(an integrated development environment). <a href="https://skillicons.dev">
  <img src="https://skillicons.dev/icons?i=vscode&perline=3" width="20"/>
  </a>
* Created `conda Environment`(Virtual Environment which separates the local environment and development environment). <a href="https://skillicons.dev">
  <img src="https://skillicons.dev/icons?i=anaconda&perline=3" width="20"/>
  </a>
* Installed all necessary packages in `requirements.txt`. <a href="https://skillicons.dev">
  <img src="https://skillicons.dev/icons?i=python&perline=3" width="20"/>
</a>
  
* Considered the project as a whole package create `setup.py`(a module used to build and distribute python packages and contains the information about the packages)
* Initailized `git` <a href="https://skillicons.dev">
  <img src="https://skillicons.dev/icons?i=github&perline=3" width="20"/>
  </a>
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
 ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┣ 📜s3_syncer.cpython-310.pyc
 ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┣ 📜s3_syncer.py
 ┃ ┃ ┗ 📜__init__.py
 ┃ ┣ 📂components
 ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┣ 📜data_ingestion.cpython-310.pyc
 ┃ ┃ ┃ ┣ 📜data_transformation.cpython-310.pyc
 ┃ ┃ ┃ ┣ 📜data_validation.cpython-310.pyc
 ┃ ┃ ┃ ┣ 📜model_trainer.cpython-310.pyc
 ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┣ 📜data_ingestion.py
 ┃ ┃ ┣ 📜data_transformation.py
 ┃ ┃ ┣ 📜data_validation.py
 ┃ ┃ ┣ 📜model_trainer.py
 ┃ ┃ ┗ 📜__init__.py
 ┃ ┣ 📂constant
 ┃ ┃ ┣ 📂training_pipeline
 ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┗ 📜__init__.py
 ┃ ┣ 📂entity
 ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┣ 📜artifact_entity.cpython-310.pyc
 ┃ ┃ ┃ ┣ 📜config_entity.cpython-310.pyc
 ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┣ 📜artifact_entity.py
 ┃ ┃ ┣ 📜config_entity.py
 ┃ ┃ ┗ 📜__init__.py
 ┃ ┣ 📂exception
 ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┣ 📜execption.cpython-310.pyc
 ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┣ 📜execption.py
 ┃ ┃ ┗ 📜__init__.py
 ┃ ┣ 📂logging
 ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┣ 📜logger.cpython-310.pyc
 ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┣ 📜logger.py
 ┃ ┃ ┗ 📜__init__.py
 ┃ ┣ 📂pipeline
 ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┣ 📜training_pipeline.cpython-310.pyc
 ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┣ 📜batch_prediction.py
 ┃ ┃ ┣ 📜training_pipeline.py
 ┃ ┃ ┗ 📜__init__.py
 ┃ ┣ 📂utils
 ┃ ┃ ┣ 📂main_utils
 ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┣ 📜utils.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┣ 📜utils.py
 ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┣ 📂ml_utils
 ┃ ┃ ┃ ┣ 📂metric
 ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┣ 📜classification_metric.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┣ 📜classification_metric.py
 ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┣ 📂model
 ┃ ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┃ ┣ 📜estimator.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┣ 📜estimator.py
 ┃ ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┗ 📜__init__.cpython-310.pyc
 ┃ ┃ ┗ 📜__init__.py
 ┃ ┣ 📂__pycache__
 ┃ ┃ ┗ 📜__init__.cpython-310.pyc
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
 ┣ 📂__pycache__
 ┃ ┗ 📜app.cpython-310.pyc
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



from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.components.data_validation import DataValidation
from networksecurity.components.data_transformation import DataTransformation
from networksecurity.logging.logger import logging
from networksecurity.exception.execption import NetworkSecurityException
from networksecurity.entity.config_entity import DataIngestionConfig,DataValidationConfig,DataTransformationConfig
from networksecurity.entity.config_entity import TrainingPipelineConfig
import sys

if __name__ == "__main__":
    try:
        ## Data Ingestion 
        trainingpipelineconfig = TrainingPipelineConfig()
        dataingestionconfig = DataIngestionConfig(trainingpipelineconfig)
        data_ingestion = DataIngestion(dataingestionconfig)
        logging.info("Initiate the data ingestion")
        dataingestionatifact = data_ingestion.initiate_data_ingestion()
        logging.info("Data Ingestion completed")
        print(dataingestionatifact)

        # Data Validation
        data_validation_config = DataValidationConfig(trainingpipelineconfig)
        data_validation = DataValidation(dataingestionatifact,data_validation_config=data_validation_config)
        logging.info("Initiate the data validation")
        data_validation_artifact = data_validation.initiate_data_validation()
        logging.info("Data Validation completed")
        print(data_validation_artifact)

        # Data Transformation 
        data_transformation_config = DataTransformationConfig(trainingpipelineconfig)
        data_transformation = DataTransformation(data_validation_artifact,data_transformation_config)
        logging.info("Data Transformation started")
        data_transformation_artifact = data_transformation.initiate_data_transformation()
        logging.info("Data Transformation completed")
        print(data_transformation_artifact)
        

    except Exception as e:
        raise NetworkSecurityException(e,sys)
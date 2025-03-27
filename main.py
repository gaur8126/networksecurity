from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.logging.logger import logging
from networksecurity.exception.execption import NetworkSecurityException
from networksecurity.entity.config_entity import DataIngestionConfig
from networksecurity.entity.config_entity import TrainingPipelineConfig
import sys

if __name__ == "__main__":
    try:
        trainingpipelineconfig = TrainingPipelineConfig()
        dataingestionconfig = DataIngestionConfig(trainingpipelineconfig)
        data_ingestion = DataIngestion(dataingestionconfig)
        logging.info("Initiate the data ingestion")
        dataingestionatifact = data_ingestion.initiate_data_ingestion()
        print(dataingestionatifact)

    except Exception as e:
        raise NetworkSecurityException(e,sys)
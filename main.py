from mlProject.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from mlProject import logger


STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n")
except Exception as e:
    logger.exception(e)
    raise e

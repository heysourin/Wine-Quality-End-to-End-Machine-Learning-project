from mlProject import logger
from mlProject.components.model_evaluation import ModelEvaluation
from mlProject.config.configuration import ConfigurationManager

STAGE_NAME = "Model evaluation stage"


class ModelEvaluationTrainingPipeline:
    def __init__(self) -> None:
        pass

    def main(self):
        config = ConfigurationManager()
        model_evaluation_config = config.get_model_evaluation_config()
        model_evaluation_config = ModelEvaluation(
            config=model_evaluation_config)
        model_evaluation_config.save_results()

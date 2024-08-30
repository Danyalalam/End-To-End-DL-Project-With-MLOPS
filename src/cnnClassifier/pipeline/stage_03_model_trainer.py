from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier.components.model_trainer import Training
from cnnClassifier import logger

STAGE_NAME = "Training"

class ModelTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        # Initialize the Configuration Manager
        config = ConfigurationManager()
        
        # Get the training configuration
        training_config = config.get_training_config()
        
        # Initialize the Training component with the configuration
        training = Training(config=training_config)
        
        # Load the base model
        training.get_base_model()
        
        # Set up the data generators for training and validation
        training.train_valid_generator()
        
        # Start the training process
        training.train()

if __name__ == '__main__':
    try:
        logger.info(f"*******************")
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        
        # Create and run the pipeline
        obj = ModelTrainingPipeline()
        obj.main()
        
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e

import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.FileHandler("training.log"), logging.StreamHandler()],
)
logger = logging.getLogger(__name__)

def demo_logging():
    logger.info("Training started: lr=0.001, batch_size=32, epochs=10")
    logger.info("Step 100: loss=2.3026, accuracy=0.10")
    logger.warning("Loss spike detected: 15.7 at step 450")
    logger.info("Step 1000: loss=0.4512, accuracy=0.87")
    logger.info("Training complete: best_loss=0.3201")

demo_logging()

import logging

from . import Experimentation

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    logging.info("Experimentation Started...")
    experimentation = Experimentation('benchmark-v1')
    logging.info("Running Experiments...")
    experimentation.run_experiments()

import logging
import colorlog

def setup_logger():
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    
    # console handler color)
    console_handler = colorlog.StreamHandler()
    
    console_formatter = colorlog.ColoredFormatter(
        "%(log_color)s%(asctime)s | %(levelname)s | %(message)s",
        log_colors={
            "DEBUG": "cyan",
            "INFO": "green",
            "WARNING": "yellow",
            "ERROR": "red",
            "CRITICAL": "bold_red"
        }
    )
    
    console_handler.setFormatter(console_formatter)
    
    # file handler
    file_handler = logging.FileHandler("pipeline.log")
    
    file_formatter = logging.Formatter("%(asctime)s | %(levelname)s | %(message)s", datefmt="%Y-%m-%d %H:%M:%S")
    file_handler.setFormatter(file_formatter)
    
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)
    
    return logger



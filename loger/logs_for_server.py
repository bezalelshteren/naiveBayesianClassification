import logging
import os

log_dir = "logs_into_a_file"
log_file = os.path.join(log_dir, "logs_for_naiveBaysian.log")

os.makedirs(log_dir, exist_ok=True)

logging.basicConfig(
    filename=log_file,
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

# בדיקה פשוטה
logging.debug("בדיקת לוגים — DEBUG")
logging.info("בדיקת לוגים — INFO")
logging.warning("בדיקת לוגים — WARNING")

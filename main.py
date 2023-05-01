
from .log import set_log

if __name__ == "__main__":
    log = set_log(__name__)

    log.debug("debug to stdout?")
    log.info("info to stdout?")
    log.warning("warning to stdout?")
    log.error("error to stdout?")
    raise ValueError("Broken file")


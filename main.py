import logging
import sys

if __name__ == "__main__":
    print("print to stdout")


    log = logging.getLogger()
    log.setLevel(level=logging.DEBUG)
    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(logging.DEBUG)
    log.addHandler(handler)

    log.debug("debug to stdout?")
    log.info("info to stdout?")
    log.warning("warning to stdout?")
    log.error("error to stdout?")
    raise ValueError("Broken file")


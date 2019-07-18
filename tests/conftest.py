import os

import pytest

from daopy import dao, model


@pytest.fixture(scope="module")
def dao_config():

    return _fixture_file("dao_config.ini")


@pytest.fixture(scope="function")
@pytest.mark.usefixtures("dao_config")
def dao_detection(dao_config):
    """
    Instantiates and returns a DAO for model.Detection objects, assumed to be
    based on an in-memory SQLite database, whcih is populated with three dummy
    detection records.

    :param dao_config:
    :return:
    """

    # instantiate the DAO and load it with three data model objects
    detection_dao = dao.DetectionDao(dao_config)
    detection = model.Detection(category="label1",
                                probability=0.75,
                                start_x=5,
                                start_y=4,
                                end_x=24,
                                end_y=18)
    detection_dao.insert(detection)
    detection = model.Detection(category="label1",
                                probability=0.95,
                                start_x=15,
                                start_y=14,
                                end_x=24,
                                end_y=18)
    detection_dao.insert(detection)
    detection = model.Detection(category="label2",
                                probability=0.85,
                                start_x=5,
                                start_y=4,
                                end_x=24,
                                end_y=18)
    detection_dao.insert(detection)
    yield detection_dao


def _fixture_file(file_name):
    """
    Helper function used to locate a fixtures file.

    :param file_name:
    :return:
    """
    return os.path.join(os.path.split(__file__)[0], "fixtures", file_name)

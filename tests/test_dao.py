import pytest

from daopy import model


@pytest.mark.usefixtures("dao_detection")
def test_delete(dao_detection):

    dao_detection.delete(1)
    pass


@pytest.mark.usefixtures("dao_detection")
def test_find(dao_detection):

    # get the first detection object inserted within conftest.dao_detection
    detection = dao_detection.find(1)

    # make sure the found object looks the way we expect it to
    assert detection.id == 1
    assert detection.probability == 0.75
    assert detection.start_x == 5
    assert detection.start_y == 4
    assert detection.end_x == 24
    assert detection.end_y == 18


@pytest.mark.usefixtures("dao_detection")
def test_insert(dao_detection):

    detection = model.Detection(category="labelX",
                                probability=0.75,
                                start_x=25,
                                start_y=24,
                                end_x=124,
                                end_y=118)
    dao_detection.insert(detection)


@pytest.mark.usefixtures("dao_detection")
def test_insert_all(dao_detection):

    # create a couple of detection objects for insertion
    detection1 = model.Detection(category="labelY",
                                 probability=0.25,
                                 start_x=35,
                                 start_y=34,
                                 end_x=124,
                                 end_y=118)
    detection2 = model.Detection(category="labelZ",
                                 probability=0.45,
                                 start_x=25,
                                 start_y=24,
                                 end_x=124,
                                 end_y=118)

    # insert both objects at once
    dao_detection.insert_all([detection1, detection2])


@pytest.mark.usefixtures("dao_detection")
def test_update(dao_detection):

    # get the first detection object inserted in conftest.dao_detection
    detection = dao_detection.find(1)

    attributes = {
        "category": "label3",
        "probability": 0.35,
    }

    dao_detection.update(detection.id, attributes)

    # TODO the above just tests that the update happens without an error,
    #   we should next test to see if the updates actually took
    # detection = dao_detection.find(1)
    # assert detection.category == "label3"
    # assert detection.probability == 0.35

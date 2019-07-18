import pytest

from daopy import dao


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

    pass


@pytest.mark.usefixtures("dao_detection")
def test_insert_all(dao_detection):

    pass


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
